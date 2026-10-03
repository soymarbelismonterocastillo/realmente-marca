import sys
import os
import json
import urllib.request
import urllib.error
import ssl
import argparse
from datetime import datetime

# Path to local Vercel credentials config
CONFIG_FILE = os.path.join(os.path.dirname(__file__), ".vercel_config.json")

# Ensure UTF-8 encoding on Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def load_credentials():
    """Carga las credenciales de Vercel desde .vercel_config.json o variables de entorno."""
    token = os.environ.get("VERCEL_TOKEN")
    username = os.environ.get("VERCEL_USER")
    email = os.environ.get("VERCEL_EMAIL")
    team_id = os.environ.get("VERCEL_TEAM_ID")

    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                token = data.get("token", token)
                username = data.get("username", username)
                email = data.get("email", email)
                team_id = data.get("default_team_id", team_id)
        except Exception as e:
            print(f"[!] Advertencia al leer {CONFIG_FILE}: {e}")

    if not token:
        print("[X] ERROR: No se encontró el token de acceso de Vercel.")
        print("    Asegúrate de configurar .vercel_config.json o la variable VERCEL_TOKEN.")
        sys.exit(1)

    return {
        "token": token,
        "username": username or "Desconocido",
        "email": email or "N/A",
        "team_id": team_id
    }

def get_ssl_context():
    """Genera contexto SSL para peticiones HTTPS seguras."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def vercel_request(endpoint, method="GET", data=None, silent_404=False):
    """Ejecuta peticiones HTTP a la REST API de Vercel v2/v6/v9/v10."""
    creds = load_credentials()
    url = f"https://api.vercel.com{endpoint}"

    # Adjuntar teamId si existe y no está presente en la query
    if creds["team_id"] and "teamId=" not in url:
        sep = "&" if "?" in url else "?"
        url += f"{sep}teamId={creds['team_id']}"

    headers = {
        "Authorization": f"Bearer {creds['token']}",
        "User-Agent": "RealMente-Vercel-Skill/1.0",
        "Content-Type": "application/json"
    }

    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    ctx = get_ssl_context()

    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            res_body = response.read().decode("utf-8")
            if res_body:
                return json.loads(res_body)
            return {}
    except urllib.error.HTTPError as e:
        if e.code == 404 and silent_404:
            return None
        err_msg = e.read().decode("utf-8")
        print(f"[X] Error HTTP {e.code} en {endpoint}: {err_msg}")
        return None
    except Exception as e:
        print(f"[X] Error de conexión con Vercel API: {e}")
        return None

def check_status():
    """Verifica el estado del usuario autenticado y resumen de la cuenta Vercel."""
    creds = load_credentials()
    print(f"[*] Verificando credenciales de Vercel en la API oficial...")

    user_info = vercel_request("/v2/user")
    if user_info and "user" in user_info:
        u = user_info["user"]
        print("\n[✓] Autenticación Exitosa en Vercel!")
        print(f"    • Usuario:    @{u.get('username')}")
        print(f"    • Email:      {u.get('email')}")
        print(f"    • User ID:    {u.get('id')}")
        print(f"    • Team ID:    {u.get('defaultTeamId') or creds['team_id'] or 'Personal (Sin equipo)'}")

        projects = vercel_request("/v9/projects")
        proj_count = len(projects.get("projects", [])) if projects else 0
        print(f"    • Proyectos Totales: {proj_count}")

        deployments = vercel_request("/v6/deployments?limit=5")
        dep_count = len(deployments.get("deployments", [])) if deployments else 0
        print(f"    • Despliegues Recientes: {dep_count}")
    else:
        print("[X] Falló la verificación de credenciales de Vercel.")

def list_projects():
    """Lista todos los proyectos registrados en la cuenta de Vercel."""
    print("[*] Obteniendo lista de proyectos desde Vercel...")
    res = vercel_request("/v9/projects")
    if res and "projects" in res:
        projects = res["projects"]
        print(f"\n[✓] Se encontraron {len(projects)} proyectos en Vercel:\n")
        if not projects:
            print("    (No hay proyectos creados aún en esta cuenta/equipo)")
            return

        for p in projects:
            framework = p.get("framework") or "static / html"
            updated_at = p.get("updatedAt")
            date_str = ""
            if updated_at:
                try:
                    dt = datetime.fromtimestamp(updated_at / 1000)
                    date_str = dt.strftime("%Y-%m-%d %H:%M")
                except Exception:
                    date_str = str(updated_at)
            
            targets = p.get("targets", {}).get("production", {})
            url = targets.get("url", "Sin URL de despliegue")
            if url != "Sin URL de despliegue" and not url.startswith("http"):
                url = f"https://{url}"

            print(f"  📌 Nombre:      {p['name']}")
            print(f"     ID:          {p['id']}")
            print(f"     Framework:   {framework}")
            print(f"     Última Act.: {date_str}")
            print(f"     URL Prod:    {url}")
            print(f"     ----------------------------------------")
    else:
        print("[X] Error al obtener la lista de proyectos.")

def create_project(name, framework=None):
    """Crea un nuevo proyecto en Vercel."""
    print(f"[*] Creando nuevo proyecto '{name}' en Vercel...")
    payload = {
        "name": name
    }
    if framework:
        payload["framework"] = framework

    res = vercel_request("/v9/projects", method="POST", data=payload)
    if res and "id" in res:
        print(f"[✓] Proyecto creado con éxito!")
        print(f"    • Nombre:    {res['name']}")
        print(f"    • ID:        {res['id']}")
        print(f"    • Framework: {res.get('framework', 'Auto-detectado')}")
        return res
    else:
        print(f"[X] No se pudo crear el proyecto '{name}'.")
        return None

def delete_project(name_or_id):
    """Elimina un proyecto en Vercel por nombre o ID."""
    print(f"[*] Eliminando proyecto '{name_or_id}' de Vercel...")
    res = vercel_request(f"/v9/projects/{name_or_id}", method="DELETE")
    if res is not None:
        print(f"[✓] Proyecto '{name_or_id}' eliminado correctamente de Vercel.")
    else:
        print(f"[X] Error al intentar eliminar el proyecto.")

def list_deployments(limit=10):
    """Obtiene los despliegues más recientes en Vercel."""
    print(f"[*] Obteniendo los últimos {limit} despliegues...")
    res = vercel_request(f"/v6/deployments?limit={limit}")
    if res and "deployments" in res:
        deps = res["deployments"]
        print(f"\n[✓] {len(deps)} despliegues encontrados:\n")
        if not deps:
            print("    (Sin despliegues registrados)")
            return

        for d in deps:
            state = d.get("state", "UNKNOWN")
            icon = "🟢" if state == "READY" else ("🟡" if state == "BUILDING" else "🔴")
            url = f"https://{d.get('url')}" if d.get('url') else "N/A"
            name = d.get("name", "N/A")
            target = d.get("target") or "preview"

            print(f"  {icon} [{state}] {name} ({target.upper()})")
            print(f"     URL: {url}")
            print(f"     ID:  {d.get('uid')}")
            print(f"     ----------------------------------------")
    else:
        print("[X] No se pudieron recuperar los despliegues.")

def list_env_vars(project_name):
    """Lista las variables de entorno de un proyecto."""
    print(f"[*] Consultando variables de entorno del proyecto '{project_name}'...")
    res = vercel_request(f"/v9/projects/{project_name}/env")
    if res and "envs" in res:
        envs = res["envs"]
        print(f"\n[✓] {len(envs)} variables de entorno encontradas para '{project_name}':\n")
        if not envs:
            print("    (No hay variables de entorno configuradas)")
            return

        for e in envs:
            targets = ", ".join(e.get("target", []))
            print(f"  🔑 Clave:   {e['key']}")
            print(f"     ID:      {e['id']}")
            print(f"     Tipo:    {e.get('type', 'plain')}")
            print(f"     Entornos:{targets}")
            print(f"     ----------------------------------------")
    else:
        print(f"[X] No se pudieron obtener las variables del proyecto '{project_name}'.")

def add_env_var(project_name, key, value, targets=["production", "preview", "development"]):
    """Agrega una variable de entorno a un proyecto en Vercel."""
    print(f"[*] Añadiendo variable '{key}' al proyecto '{project_name}'...")
    payload = {
        "key": key,
        "value": value,
        "type": "plain",
        "target": targets
    }
    res = vercel_request(f"/v10/projects/{project_name}/env", method="POST", data=payload)
    if res:
        print(f"[✓] Variable '{key}' añadida con éxito al proyecto '{project_name}'.")
    else:
        print(f"[X] Error al añadir la variable de entorno.")

def ai_gateway_info():
    """Muestra la información de configuración y guía técnica del Vercel AI Gateway."""
    print("=" * 70)
    print(" 🚀 GUÍA Y CONFIGURACIÓN DE VERCEL AI GATEWAY - REALMENTE")
    print("=" * 70)
    print("""
Vercel AI Gateway permite centralizar, monitorear, asegurar y optimizar
el consumo de modelos de Inteligencia Artificial (OpenAI, Gemini, Anthropic, etc.)
en todas tus aplicaciones web y servicios de RealMente.

📌 1. CARACTERÍSTICAS PRINCIPALES DE VERCEL AI GATEWAY:
   • Endpoint unificado con balanceo, almacenamiento en caché y fallback.
   • Gestión centralizada de Tokens y Rate Limiting por proyecto.
   • Telemetría en tiempo real y logs unificados en el dashboard de Vercel.
   • Integración nativa con Vercel AI SDK (`ai` de npm / Next.js / React / Node).

📌 2. ENDPOINTS Y RUTAS OFICIALES:
   • Endpoint General de AI Gateway: https://ai-gateway.vercel.sh/v1
   • OIDC Authorization URL:          https://api.vercel.com/v1/ai/token

📌 3. EJEMPLO DE CONFIGURACIÓN EN VERCEL AI SDK (TypeScript / JavaScript):
   ```typescript
   import { createOpenAI } from '@ai-sdk/openai';
   import { generateText } from 'ai';

   const vercelAiGateway = createOpenAI({
     baseURL: 'https://ai-gateway.vercel.sh/v1',
     apiKey: process.env.VERCEL_AI_GATEWAY_KEY || process.env.AI_GATEWAY_TOKEN,
   });

   const { text } = await generateText({
     model: vercelAiGateway('gpt-4o'),
     prompt: 'Genera 3 ganchos para el podcast RealMente',
   });
   ```

📌 4. COMANDO DE SETUP CON VERCEL CLI (Si Node.js está disponible):
   ```bash
   npx vercel ai-gateway setup
   ```

📌 5. CREAR CLAVE DE AI GATEWAY EN PROYECTOS:
   ```bash
   python vercel_helper.py env-add --project realmente-club --key VERCEL_AI_GATEWAY_KEY --value tu_clave_aqui
   ```
""")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Asistente Automatizado de la Skill de Vercel - RealMente")
    subparsers = parser.add_subparsers(dest="command")

    # Status
    subparsers.add_parser("status", help="Verificar conexión a Vercel y resumen de la cuenta")

    # List Projects
    subparsers.add_parser("list-projects", help="Listar todos los proyectos en Vercel")

    # Create Project
    create_parser = subparsers.add_parser("create-project", help="Crear un nuevo proyecto en Vercel")
    create_parser.add_argument("--name", required=True, help="Nombre del proyecto en Vercel (kebab-case)")
    create_parser.add_argument("--framework", help="Framework objetivo (ej: nextjs, vite, nuxt, svelte, html)")

    # Delete Project
    del_parser = subparsers.add_parser("delete-project", help="Eliminar un proyecto en Vercel")
    del_parser.add_argument("--name", required=True, help="Nombre o ID del proyecto")

    # Deployments
    dep_parser = subparsers.add_parser("deployments", help="Ver despliegues recientes")
    dep_parser.add_argument("--limit", type=int, default=10, help="Número de despliegues a mostrar (def: 10)")

    # Env List
    env_list_parser = subparsers.add_parser("env-list", help="Listar variables de entorno de un proyecto")
    env_list_parser.add_argument("--project", required=True, help="Nombre del proyecto")

    # Env Add
    env_add_parser = subparsers.add_parser("env-add", help="Añadir una variable de entorno a un proyecto")
    env_add_parser.add_argument("--project", required=True, help="Nombre del proyecto")
    env_add_parser.add_argument("--key", required=True, help="Nombre de la variable")
    env_add_parser.add_argument("--value", required=True, help="Valor de la variable")

    # AI Gateway
    subparsers.add_parser("ai-gateway", help="Ver guía y configuración de Vercel AI Gateway")

    args = parser.parse_args()

    if args.command == "status":
        check_status()
    elif args.command == "list-projects":
        list_projects()
    elif args.command == "create-project":
        create_project(args.name, framework=args.framework)
    elif args.command == "delete-project":
        delete_project(args.name)
    elif args.command == "deployments":
        list_deployments(limit=args.limit)
    elif args.command == "env-list":
        list_env_vars(args.project)
    elif args.command == "env-add":
        add_env_var(args.project, args.key, args.value)
    elif args.command == "ai-gateway":
        ai_gateway_info()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
