import os
import shutil

src_dir = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas"
root_dir = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA"

# Files to sync
pres_html = os.path.join(root_dir, "presentacion_episodio_62.html")
table_img = os.path.join(root_dir, "mesa_metafora_culpa.png")
autoeval_html = os.path.join(src_dir, "autoevaluacion_culpa_inconsciente_ep62.html")
autoeval_pdf = os.path.join(src_dir, "autoevaluacion_culpa_inconsciente_ep62.pdf")
autoeval_md = os.path.join(src_dir, "autoevaluacion_culpa_inconsciente_ep62.md")

# 1. Targets in Google Drive
gdrive_club = r"G:\Mi unidad\MARCA\Realmente_Club"
gdrive_entregables = r"G:\Mi unidad\MARCA\Entregables"
gdrive_ep62 = r"G:\Mi unidad\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas"
gdrive_podcast_club = r"G:\Mi unidad\MARCA\Podcast_Club\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas"

for d in [gdrive_club, gdrive_entregables, gdrive_ep62, gdrive_podcast_club]:
    os.makedirs(d, exist_ok=True)

# Copy Presentation slides to GDrive
for d in [gdrive_club, gdrive_ep62, gdrive_podcast_club]:
    shutil.copy2(pres_html, os.path.join(d, "presentacion_episodio_62.html"))
    shutil.copy2(table_img, os.path.join(d, "mesa_metafora_culpa.png"))
    print(f"Copied presentation to: {d}")

# Copy with official naming
shutil.copy2(pres_html, os.path.join(gdrive_club, "Presentacion_Clase_Sabado_EP62_Marbelis_Montero.html"))
shutil.copy2(autoeval_html, os.path.join(gdrive_club, "Instrumento_Autoevaluacion_Culpa_Inconsciente_EP62_Marbelis_Montero.html"))
shutil.copy2(autoeval_pdf, os.path.join(gdrive_club, "Instrumento_Autoevaluacion_Culpa_Inconsciente_EP62_Marbelis_Montero.pdf"))
shutil.copy2(autoeval_md, os.path.join(gdrive_club, "Autoevaluacion_Culpa_Inconsciente_EP62.md"))
print("Copied all official files to GDrive Realmente_Club")

# Copy all files from src_dir
for f in os.listdir(src_dir):
    f_path = os.path.join(src_dir, f)
    if os.path.isfile(f_path):
        shutil.copy2(f_path, os.path.join(gdrive_ep62, f))
        shutil.copy2(f_path, os.path.join(gdrive_podcast_club, f))
print("Copied all episode files to GDrive Episodios and Podcast_Club")

# 2. Desktops
desktops = [r"C:\Users\soyma\OneDrive\Desktop", r"C:\Users\soyma\Desktop"]
for dt in desktops:
    if os.path.exists(dt):
        # Direct presentation html copy on desktop
        shutil.copy2(pres_html, os.path.join(dt, "CLASE_SABADO_EP62.html"))
        shutil.copy2(table_img, os.path.join(dt, "mesa_metafora_culpa.png"))
        
        # Internet shortcut .url for presentation
        url_file = os.path.join(dt, "CLASE_SABADO_EP62.url")
        with open(url_file, "w", encoding="utf-8") as f:
            f.write("[InternetShortcut]\nURL=file:///c:/Users/soyma/OneDrive/Documents/ANTIGRAVITY/MARCA/presentacion_episodio_62.html\n")
            
        # .bat launcher for presentation
        bat_file = os.path.join(dt, "ABRIR_CLASE_SABADO_EP62.bat")
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(f'@echo off\nstart "" "{pres_html}"\n')
        print("Created Desktop shortcuts for presentation on:", dt)

print("SYNC AND SHORTCUTS COMPLETED SUCCESSFULLY!")
