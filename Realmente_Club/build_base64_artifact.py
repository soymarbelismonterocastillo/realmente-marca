import os
import base64
from PIL import Image

ARTIFACT_DIR = r"C:\Users\soyma\.gemini\antigravity\brain\d7d58a4c-2e8e-4b53-9cc8-4d992040c3ac"
TARGET_MD = os.path.join(ARTIFACT_DIR, "diapositivas_clase_ep57_diseno.md")

slides_data = []

for i in range(1, 14):
    png_path = os.path.join(ARTIFACT_DIR, f"slide_{i}.png")
    if os.path.exists(png_path):
        # Resize slightly for fast rendering in markdown panel
        img = Image.open(png_path)
        img_resized = img.resize((960, 540), Image.Resampling.LANCZOS)
        
        tmp_jpg = os.path.join(ARTIFACT_DIR, f"slide_{i}_opt.jpg")
        img_resized.convert("RGB").save(tmp_jpg, "JPEG", quality=85)
        
        with open(tmp_jpg, "rb") as f:
            b64_str = base64.b64encode(f.read()).decode("utf-8")
            slides_data.append((i, f"data:image/jpeg;base64,{b64_str}"))

# Build Markdown with embedded Base64 images
md_lines = [
    "# 🎴 DIAPOSITIVAS DE LA CLASE (EPISODIO 57)",
    "### Marbelis Montero · RealMente Club",
    "**Tema:** Tu vida no cambia cuando lo entiendes, cambia cuando lo ejecutas (De la Teoría a la Acción)",
    "",
    "---",
    "",
    "````carousel"
]

for idx, b64 in slides_data:
    md_lines.append(f"![Slide {idx}]( {b64} )".replace(" ( ", "(").replace(" )", ")"))
    if idx < len(slides_data):
        md_lines.append("<!-- slide -->")

md_lines.append("````")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 🖼️ Vista Desplegada Diapositiva por Diapositiva")
md_lines.append("")

slide_titles = [
    "Portada Principal",
    "Frase de Apertura (Cita Gigante)",
    "El Encuadre (Saber vs. Hacer)",
    "El Mapa del Saboteo (Las 2 Trampas)",
    "Patrón 1: La Analista del Pasado",
    "Patrón 2: La Sanadora Eterna",
    "Patrón 3: La Esperadora del Momento Perfecto",
    "Patrón 4: La Protectora del Potencial",
    "La Metáfora de Nadar",
    "La Acción es Fría (Desmitificando la Motivación)",
    "Ejercicio Práctico en Vivo",
    "El Salto de Identidad y Compromiso",
    "Pausa de Grabación & Espacio Privado 1 a 1"
]

for idx, b64 in slides_data:
    title = slide_titles[idx - 1] if idx <= len(slide_titles) else f"Diapositiva {idx}"
    md_lines.append(f"### Slide {idx}: {title}")
    md_lines.append(f"![Slide {idx}: {title}]({b64})")
    md_lines.append("")

content = "\n".join(md_lines)

with open(TARGET_MD, "w", encoding="utf-8") as f:
    f.write(content)

print("Markdown artifact updated with embedded Base64 image data!")
