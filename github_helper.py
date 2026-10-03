import sys
import os
import json
import base64
import urllib.request
import urllib.error
import ssl
import argparse

# Config file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), ".github_config.json")

# Ensure stdout uses UTF-8 encoding on Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Files and extensions to ignore during project sync
IGNORED_DIRS = {".git", "__pycache__", ".vscode", ".idea"}
IGNORED_FILES = {".env", ".github_config.json", "desktop.ini", "Thumbs.db"}
IGNORED_EXTS = {".pyc", ".log", ".tmp"}

def load_credentials():
    username = os.environ.get("GITHUB_USER")
    token = os.environ.get("GITHUB_TOKEN")
    
    if not username or not token:
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    username = data.get("username", username)
                    token = data.get("token", token)
            except Exception as e:
                print(f"[!] Error al cargar {CONFIG_FILE}: {e}")
                
    if not username or not token:
        print("[X] ERROR: No se encontraron credenciales de GitHub.")
        print("    Asegúrate de configurar .github_config.json o las variables GITHUB_USER y GITHUB_TOKEN.")
        sys.exit(1)
        
    return username, token

def get_ssl_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def github_request(url, method="GET", data=None, token=None, silent_404=False):
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "RealMente-GitHub-Skill",
        "Accept": "application/vnd.github.v3+json"
    }
    
    body = None
    if data is not None:
        headers["Content-Type"] = "application/json"
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
        print(f"[X] Error HTTP {e.code}: {err_msg}")
        return None
    except Exception as e:
        print(f"[X] Error de conexión: {e}")
        return None

def check_status():
    username, token = load_credentials()
    print(f"[*] Verificando conexión para el usuario: @{username}...")
    user_info = github_request("https://api.github.com/user", token=token)
    if user_info:
        print(f"[✓] Conexión Exitosa!")
        print(f"    Nombre: {user_info.get('name', 'N/A')}")
        print(f"    Usuario: {user_info.get('login')}")
        print(f"    Repos Públicos: {user_info.get('public_repos')}")
        print(f"    Repos Privados: {user_info.get('total_private_repos', 0)}")
        
        repos = github_request("https://api.github.com/user/repos?per_page=100", token=token)
        if repos is not None:
            print(f"\n[*] Repositorios existentes ({len(repos)}):")
            if not repos:
                print("    (No hay repositorios aún)")
            for r in repos:
                privacy = "🔒 Privado" if r.get('private') else "🌐 Público"
                print(f"    - {r['name']} ({privacy}) -> {r['html_url']}")
    else:
        print("[X] Falló la verificación de credenciales.")

def create_repository(repo_name, description="", private=False):
    username, token = load_credentials()
    print(f"[*] Creando repositorio '{repo_name}' en GitHub...")
    payload = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True
    }
    res = github_request("https://api.github.com/user/repos", method="POST", data=payload, token=token)
    if res and "html_url" in res:
        print(f"[✓] Repositorio creado exitosamente!")
        print(f"    URL: {res['html_url']}")
        return res
    else:
        print(f"[X] No se pudo crear el repositorio.")
        return None

def upload_file(repo_name, file_path, target_rel_path=None, message=None, branch="main"):
    username, token = load_credentials()
    if not os.path.exists(file_path):
        print(f"[X] El archivo local '{file_path}' no existe.")
        return False
        
    if not target_rel_path:
        target_rel_path = os.path.basename(file_path)
        
    # Convert windows backslashes to forward slashes for URL
    target_rel_path = target_rel_path.replace("\\", "/")
    
    with open(file_path, "rb") as f:
        content_bytes = f.read()
    content_b64 = base64.b64encode(content_bytes).decode("utf-8")
    
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{target_rel_path}"
    
    # Check if file exists to get sha
    sha = None
    existing = github_request(f"{url}?ref={branch}", token=token, silent_404=True)
    if existing and "sha" in existing:
        sha = existing["sha"]
        
    if not message:
        prefix = "update" if sha else "add"
        message = f"chore: {prefix} {target_rel_path}"
        
    payload = {
        "message": message,
        "content": content_b64,
        "branch": branch
    }
    if sha:
        payload["sha"] = sha
        
    res = github_request(url, method="PUT", data=payload, token=token)
    if res and "content" in res:
        print(f"[✓] Subido: {target_rel_path} (Commit: {res.get('commit', {}).get('sha', '')[:7]})")
        return True
    else:
        print(f"[X] Error al subir '{target_rel_path}'.")
        return False

def sync_project(repo_name="realmente-marca"):
    username, token = load_credentials()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"[*] Iniciando sincronización completa del proyecto en '{base_dir}' a GitHub ('{repo_name}')...")
    
    # Ensure repo exists
    existing_repo = github_request(f"https://api.github.com/repos/{username}/{repo_name}", token=token, silent_404=True)
    if not existing_repo:
        print(f"[*] Repositorio '{repo_name}' no encontrado. Creándolo automáticamente...")
        create_repository(repo_name, description="Repositorio oficial de marca, recursos y contenidos de RealMente", private=False)

    files_to_upload = []
    for root, dirs, files in os.walk(base_dir):
        # Prune ignored dirs
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            if f in IGNORED_FILES:
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext in IGNORED_EXTS:
                continue
            
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir)
            files_to_upload.append((full_path, rel_path))

    print(f"[*] Se encontraron {len(files_to_upload)} archivos para sincronizar.")
    success_count = 0
    for full_path, rel_path in files_to_upload:
        # Determine semantic message prefix
        if rel_path.startswith("skill_") or rel_path.endswith(".md"):
            msg = f"docs: actualizar {rel_path}"
        elif rel_path.endswith(".html") or rel_path.endswith(".png") or rel_path.endswith(".pdf"):
            msg = f"feat: actualizar recurso visual {rel_path}"
        else:
            msg = f"chore: sincronizar {rel_path}"
            
        if upload_file(repo_name, full_path, target_rel_path=rel_path, message=msg):
            success_count += 1

    print(f"\n[✓] Sincronización completa finalizada: {success_count}/{len(files_to_upload)} archivos subidos a https://github.com/{username}/{repo_name}")

def add_collaborator(repo_name, collaborator_user, permission="push"):
    username, token = load_credentials()
    print(f"[*] Enviando invitación de colaborador a @{collaborator_user} para el repositorio '{repo_name}'...")
    url = f"https://api.github.com/repos/{username}/{repo_name}/collaborators/{collaborator_user}"
    payload = {"permission": permission}
    res = github_request(url, method="PUT", data=payload, token=token)
    if res is not None:
        print(f"[✓] Invitación enviada exitosamente a @{collaborator_user}!")
        if "html_url" in res:
            print(f"    Enlace de invitación: {res['html_url']}")
        return True
    else:
        print(f"[X] No se pudo enviar la invitación a @{collaborator_user}.")
        return False

def main():
    parser = argparse.ArgumentParser(description="Asistente de la Skill de GitHub para RealMente")
    subparsers = parser.add_subparsers(dest="command")
    
    # Status
    subparsers.add_parser("status", help="Verificar conexión y listar repositorios")
    
    # Create Repo
    create_parser = subparsers.add_parser("create-repo", help="Crear un nuevo repositorio en GitHub")
    create_parser.add_argument("--name", required=True, help="Nombre del repositorio (kebab-case)")
    create_parser.add_argument("--desc", default="", help="Descripción del repositorio")
    create_parser.add_argument("--private", action="store_true", help="Si el repositorio debe ser privado")
    
    # Upload File
    upload_parser = subparsers.add_parser("upload", help="Subir un archivo a un repositorio")
    upload_parser.add_argument("--repo", required=True, help="Nombre del repositorio")
    upload_parser.add_argument("--file", required=True, help="Ruta del archivo local")
    upload_parser.add_argument("--target", help="Ruta de destino en el repo")
    upload_parser.add_argument("--message", help="Mensaje de commit (semántico)")
    
    # Add Collaborator
    collab_parser = subparsers.add_parser("add-collaborator", help="Invitar a un colaborador al repositorio")
    collab_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio")
    collab_parser.add_argument("--user", required=True, help="Nombre de usuario del colaborador en GitHub")
    collab_parser.add_argument("--permission", default="push", choices=["pull", "push", "admin", "maintain", "triage"], help="Permisos (push = escritura)")

    # Sync Project (All workspace files)
    sync_proj_parser = subparsers.add_parser("sync-project", help="Sincronizar todo el espacio de trabajo con el repositorio de marca")
    sync_proj_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio de destino")
    
    # Sync All (legacy alias for sync-project)
    sync_parser = subparsers.add_parser("sync-all", help="Sincronizar todo el proyecto de marca")
    sync_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio de destino")

    args = parser.parse_args()
    
    if args.command == "status":
        check_status()
    elif args.command == "create-repo":
        create_repository(args.name, description=args.desc, private=args.private)
    elif args.command == "upload":
        upload_file(args.repo, args.file, target_rel_path=args.target, message=args.message)
    elif args.command == "add-collaborator":
        add_collaborator(args.repo, args.user, permission=args.permission)
    elif args.command in ["sync-project", "sync-all"]:
        sync_project(args.repo)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
