import os
import shutil

base_dir = r"c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Realmente_Club"
clases_dir = os.path.join(base_dir, "Clases")
os.makedirs(clases_dir, exist_ok=True)

files_to_copy = [
    "Diapositivas_Clase_Sabado_EP57.pptx",
    "diapositivas_clase_sabado_ep57.html",
    "Clase_Sabado_EP57_Diapositivas_Estructura.md",
    "Clase_Sabado_EP57_Guia.md"
]

copied = []
for fname in files_to_copy:
    src = os.path.join(base_dir, fname)
    if os.path.exists(src):
        dst = os.path.join(clases_dir, fname)
        shutil.copy2(src, dst)
        copied.append(fname)
        print(f"Copied {fname} -> {dst}")

# Also check for Google Drive sync folder if present on system
user_home = os.path.expanduser("~")
possible_gdrive = [
    os.path.join(user_home, "Google Drive"),
    os.path.join(user_home, "My Drive"),
    os.path.join(user_home, "OneDrive - Personal"),
    os.path.join(user_home, "OneDrive")
]

print("Organized files in Clases directory:", copied)
