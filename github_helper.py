import sys
import os
import json
import base64
import urllib.request
import urllib.error
import urllib.parse
import ssl
import argparse
import hashlib
import time
from datetime import datetime

# Config file path
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".github_config.json")

# Ensure stdout uses UTF-8 encoding on Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Files and extensions to ignore during project sync
IGNORED_DIRS = {".git", "__pycache__", ".vscode", ".idea", ".vercel"}
IGNORED_FILES = {".env", ".github_config.json", ".vercel_config.json", "desktop.ini", "Thumbs.db", ".DS_Store"}
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

def compute_git_blob_sha(content_bytes):
    """Calcula el SHA-1 oficial de Git Blob para comparar con GitHub."""
    header = f"blob {len(content_bytes)}\0".encode("ascii")
    return hashlib.sha1(header + content_bytes).hexdigest()

def get_remote_tree(repo_name, branch="main", token=None):
    """Obtiene el árbol completo de blobs de un repositorio en una sola petición."""
    username, t = load_credentials()
    token = token or t
    url = f"https://api.github.com/repos/{username}/{repo_name}/git/trees/{branch}?recursive=1"
    res = github_request(url, token=token, silent_404=True)
    if not res or "tree" not in res:
        return {}
    return {item["path"]: item["sha"] for item in res["tree"] if item["type"] == "blob"}

def get_local_files(base_dir=None):
    """Escanea los archivos locales del proyecto calculando sus SHAs y marcas de tiempo."""
    if not base_dir:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    local_files = {}
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            if f in IGNORED_FILES:
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext in IGNORED_EXTS:
                continue
            
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir).replace("\\", "/")
            try:
                with open(full_path, "rb") as fp:
                    data = fp.read()
                sha = compute_git_blob_sha(data)
                mtime = os.path.getmtime(full_path)
                local_files[rel_path] = {
                    "full_path": full_path,
                    "sha": sha,
                    "mtime": mtime,
                    "size": len(data)
                }
            except Exception as e:
                print(f"[!] No se pudo leer {rel_path}: {e}")
    return local_files

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

def upload_file(repo_name, file_path, target_rel_path=None, message=None, branch="main", sha=None):
    username, token = load_credentials()
    if not os.path.exists(file_path):
        print(f"[X] El archivo local '{file_path}' no existe.")
        return False
        
    if not target_rel_path:
        target_rel_path = os.path.basename(file_path)
        
    target_rel_path = target_rel_path.replace("\\", "/")
    quoted_path = urllib.parse.quote(target_rel_path, safe="/")
    
    with open(file_path, "rb") as f:
        content_bytes = f.read()
    content_b64 = base64.b64encode(content_bytes).decode("utf-8")
    
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{quoted_path}"
    
    if sha is None:
        existing = github_request(f"{url}?ref={branch}", token=token, silent_404=True)
        if existing and "sha" in existing:
            sha = existing["sha"]
            
    if not message:
        prefix = "actualizar" if sha else "agregar"
        if target_rel_path.startswith(".agents/") or target_rel_path.startswith("skill_") or target_rel_path.endswith(".md"):
            message = f"docs: {prefix} {target_rel_path}"
        elif target_rel_path.endswith((".html", ".png", ".jpg", ".jpeg", ".pdf")):
            message = f"feat: {prefix} {target_rel_path}"
        else:
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
        print(f"  [↑] Subido: {target_rel_path} (Commit: {res.get('commit', {}).get('sha', '')[:7]})")
        return True
    else:
        print(f"  [X] Error al subir '{target_rel_path}'.")
        return False

def download_file(repo_name, rel_path, sha=None, branch="main", base_dir=None):
    """Descarga un archivo desde GitHub al workspace local."""
    username, token = load_credentials()
    if not base_dir:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    local_path = os.path.join(base_dir, rel_path.replace("/", os.sep))
    
    # Obtener el blob por SHA (rápido y hasta 100MB) o por contents
    data_bytes = None
    if sha:
        blob_url = f"https://api.github.com/repos/{username}/{repo_name}/git/blobs/{sha}"
        res = github_request(blob_url, token=token, silent_404=True)
        if res and "content" in res:
            data_bytes = base64.b64decode(res["content"])
            
    if data_bytes is None:
        quoted_rel = urllib.parse.quote(rel_path, safe="/")
        content_url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{quoted_rel}?ref={branch}"
        res = github_request(content_url, token=token, silent_404=True)
        if res and "content" in res:
            data_bytes = base64.b64decode(res["content"])
            
    if data_bytes is None:
        print(f"  [X] No se pudo descargar {rel_path} desde GitHub.")
        return False
        
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, "wb") as f:
        f.write(data_bytes)
    print(f"  [↓] Descargado: {rel_path} ({len(data_bytes)} bytes)")
    return True

def pull_project(repo_name="realmente-marca", branch="main"):
    """Descarga de GitHub los archivos nuevos o actualizados en el repositorio remoto."""
    username, token = load_credentials()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"[*] Verificando actualizaciones en GitHub (https://github.com/{username}/{repo_name}) -> Local...")
    
    remote_tree = get_remote_tree(repo_name, branch=branch, token=token)
    if not remote_tree:
        print(f"[!] Repositorio remoto vacío o no encontrado.")
        return
        
    local_files = get_local_files(base_dir)
    downloaded_count = 0
    
    for rel_path, remote_sha in remote_tree.items():
        if rel_path in IGNORED_FILES:
            continue
        ext = os.path.splitext(rel_path)[1].lower()
        if ext in IGNORED_EXTS:
            continue
            
        if rel_path not in local_files:
            print(f"[*] Archivo nuevo detectado en GitHub: {rel_path}")
            if download_file(repo_name, rel_path, sha=remote_sha, branch=branch, base_dir=base_dir):
                downloaded_count += 1
        else:
            if local_files[rel_path]["sha"] != remote_sha:
                # Comprobar fecha de commit remoto vs mtime local
                quoted_rel = urllib.parse.quote(rel_path, safe="")
                commit_info = github_request(
                    f"https://api.github.com/repos/{username}/{repo_name}/commits?path={quoted_rel}&page=1&per_page=1",
                    token=token, silent_404=True
                )
                remote_is_newer = False
                if commit_info and len(commit_info) > 0:
                    remote_date_str = commit_info[0]["commit"]["committer"]["date"]
                    remote_ts = datetime.fromisoformat(remote_date_str.replace("Z", "+00:00")).timestamp()
                    if remote_ts > local_files[rel_path]["mtime"]:
                        remote_is_newer = True
                
                if remote_is_newer:
                    print(f"[*] Archivo más reciente en GitHub: {rel_path}")
                    if download_file(repo_name, rel_path, sha=remote_sha, branch=branch, base_dir=base_dir):
                        downloaded_count += 1
                else:
                    print(f"[-] {rel_path}: Versión local es más reciente que en GitHub (se preservará).")
                    
    if downloaded_count == 0:
        print("[✓] Espacio local completamente actualizado con GitHub. No hay descargas pendientes.")
    else:
        print(f"[✓] Se descargaron {downloaded_count} archivos actualizados desde GitHub.")

def push_project(repo_name="realmente-marca", branch="main"):
    """Sube a GitHub todos los archivos locales nuevos o modificados (Copia de Seguridad Exacta)."""
    username, token = load_credentials()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"[*] Iniciando respaldo completo: Local -> GitHub (https://github.com/{username}/{repo_name})...")
    
    # Asegurar que el repo existe
    existing_repo = github_request(f"https://api.github.com/repos/{username}/{repo_name}", token=token, silent_404=True)
    if not existing_repo:
        print(f"[*] Repositorio '{repo_name}' no encontrado. Creándolo automáticamente...")
        create_repository(repo_name, description="Repositorio oficial de marca, recursos y contenidos de RealMente", private=False)

    remote_tree = get_remote_tree(repo_name, branch=branch, token=token)
    local_files = get_local_files(base_dir)
    
    to_upload = []
    already_synced = 0
    
    for rel_path, info in local_files.items():
        remote_sha = remote_tree.get(rel_path)
        if remote_sha == info["sha"]:
            already_synced += 1
        else:
            to_upload.append((rel_path, info["full_path"], remote_sha))
            
    print(f"[*] Total archivos locales evaluados: {len(local_files)}")
    print(f"[*] Archivos ya sincronizados e idénticos en GitHub: {already_synced}")
    print(f"[*] Archivos pendientes por subir/actualizar: {len(to_upload)}")
    
    if not to_upload:
        print("[✓] Todo el repositorio en GitHub ya es una copia exacta e idéntica.")
        return
        
    uploaded_count = 0
    for rel_path, full_path, remote_sha in to_upload:
        action = "actualizar" if remote_sha else "agregar"
        if rel_path.startswith(".agents/") or rel_path.startswith("skill_") or rel_path.endswith(".md"):
            msg = f"docs: {action} {rel_path}"
        elif rel_path.endswith((".html", ".png", ".jpg", ".jpeg", ".pdf")):
            msg = f"feat: {action} {rel_path}"
        else:
            msg = f"chore: {action} {rel_path}"
            
        if upload_file(repo_name, full_path, target_rel_path=rel_path, message=msg, branch=branch, sha=remote_sha):
            uploaded_count += 1
        # Pequeña pausa para evitar rate limit secundario de GitHub
        time.sleep(0.15)
        
    print(f"\n[✓] Respaldo finalizado: {uploaded_count}/{len(to_upload)} archivos subidos.")
    print(f"    Ver en: https://github.com/{username}/{repo_name}")

def sync_project(repo_name="realmente-marca", branch="main"):
    """Sincronización Bidireccional Completa: GitHub <-> Workspace Local."""
    print("==================================================================")
    print(f"🔄 SINCRONIZACIÓN BIDIRECCIONAL: REALMENTE <-> GITHUB ({repo_name})")
    print("==================================================================")
    print("\n>>> FASE 1: DESCARGA DE CAMBIOS DESDE GITHUB (PULL)...")
    pull_project(repo_name=repo_name, branch=branch)
    
    print("\n>>> FASE 2: SUBIDA Y RESPALDO EXACTO A GITHUB (PUSH)...")
    push_project(repo_name=repo_name, branch=branch)
    print("\n==================================================================")
    print("🎉 SINCRONIZACIÓN Y COPIA DE SEGURIDAD COMPLETADAS CON ÉXITO")
    print("==================================================================")

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
    parser = argparse.ArgumentParser(description="Asistente de Sincronización y Respaldo en GitHub para RealMente")
    subparsers = parser.add_subparsers(dest="command")
    
    # Status
    subparsers.add_parser("status", help="Verificar conexión y listar repositorios")
    
    # Push (Local -> GitHub)
    push_parser = subparsers.add_parser("push", help="Subir archivos locales a GitHub (copia exacta de seguridad)")
    push_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio de destino")
    push_parser.add_argument("--branch", default="main", help="Rama de destino")
    
    # Pull (GitHub -> Local)
    pull_parser = subparsers.add_parser("pull", help="Descargar cambios de GitHub al workspace local")
    pull_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio remoto")
    pull_parser.add_argument("--branch", default="main", help="Rama remota")

    # Sync (Bidireccional)
    sync_parser = subparsers.add_parser("sync", help="Sincronización bidireccional completa (Pull + Push)")
    sync_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio")
    sync_parser.add_argument("--branch", default="main", help="Rama")

    # Sync Project (Legacy Alias)
    sync_proj_parser = subparsers.add_parser("sync-project", help="Alias de sync")
    sync_proj_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio")
    sync_proj_parser.add_argument("--branch", default="main", help="Rama")
    
    # Create Repo
    create_parser = subparsers.add_parser("create-repo", help="Crear un nuevo repositorio en GitHub")
    create_parser.add_argument("--name", required=True, help="Nombre del repositorio (kebab-case)")
    create_parser.add_argument("--desc", default="", help="Descripción del repositorio")
    create_parser.add_argument("--private", action="store_true", help="Si el repositorio debe ser privado")
    
    # Upload Single File
    upload_parser = subparsers.add_parser("upload", help="Subir un archivo específico a un repositorio")
    upload_parser.add_argument("--repo", required=True, help="Nombre del repositorio")
    upload_parser.add_argument("--file", required=True, help="Ruta del archivo local")
    upload_parser.add_argument("--target", help="Ruta de destino en el repo")
    upload_parser.add_argument("--message", help="Mensaje de commit (semántico)")
    upload_parser.add_argument("--branch", default="main", help="Rama")
    
    # Add Collaborator
    collab_parser = subparsers.add_parser("add-collaborator", help="Invitar a un colaborador al repositorio")
    collab_parser.add_argument("--repo", default="realmente-marca", help="Nombre del repositorio")
    collab_parser.add_argument("--user", required=True, help="Nombre de usuario del colaborador en GitHub")
    collab_parser.add_argument("--permission", default="push", choices=["pull", "push", "admin", "maintain", "triage"], help="Permisos")

    args = parser.parse_args()
    
    if args.command == "status":
        check_status()
    elif args.command == "push":
        push_project(args.repo, branch=args.branch)
    elif args.command == "pull":
        pull_project(args.repo, branch=args.branch)
    elif args.command in ["sync", "sync-project"]:
        sync_project(args.repo, branch=args.branch)
    elif args.command == "create-repo":
        create_repository(args.name, description=args.desc, private=args.private)
    elif args.command == "upload":
        upload_file(args.repo, args.file, target_rel_path=args.target, message=args.message, branch=args.branch)
    elif args.command == "add-collaborator":
        add_collaborator(args.repo, args.user, permission=args.permission)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
