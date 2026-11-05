import asyncio
import os
import base64
from PIL import Image, ImageEnhance, ImageFilter
from playwright.async_api import async_playwright

BASE_DIR = r"C:/Users/soyma/OneDrive/Documents/ANTIGRAVITY/MARCA/Episodios/EP64_Estar_de_Tu_Lado/02_Podcast_Guion_y_Grabacion"
USER_UPLOADS = r"C:/Users/soyma/.gemini/antigravity/brain/bbafa8ef-f61b-4b86-8547-df9408e3e6a2/.user_uploaded"

def enhance_and_crop(src_path, crop_box=None):
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    
    # Resize 2x with high quality Lanczos
    img_hd = img.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
    
    # Enhance sharpness, vibrance, contrast
    img_hd = ImageEnhance.Sharpness(img_hd).enhance(1.65)
    img_hd = ImageEnhance.Color(img_hd).enhance(1.15)
    img_hd = ImageEnhance.Contrast(img_hd).enhance(1.10)
    
    if crop_box:
        # crop_box is in 2x coordinates
        img_hd = img_hd.crop(crop_box)
        
    return img_hd

def to_base64_src(pil_img):
    import io
    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

# Prepare Enhanced Photos
# Photo 2: (1024, 576) -> (2048, 1152). 
# Marbelis is center-left. We want waist up, face prominent, avoiding laptop and table clutter.
p2_path = os.path.join(USER_UPLOADS, "media_1793822015230.png")
# Crop: x from 480 to 1480 (width 1000), y from 50 to 1150 (height 1100)
img2_hd = enhance_and_crop(p2_path, crop_box=(460, 40, 1500, 1150))
b64_foto2 = to_base64_src(img2_hd)

# Photo 1: (1024, 576) -> (2048, 1152).
# Hand extends left.
p1_path = os.path.join(USER_UPLOADS, "media_1793821895317.png")
img1_hd = enhance_and_crop(p1_path, crop_box=(260, 40, 1460, 1150))
b64_foto1 = to_base64_src(img1_hd)

# HTML Templates for 3 Thumbnail Options (1920x1080)
def generate_html(option_num, hook_html, subtitle_text, badge_text, b64_img, accent_color="#2AD2C5"):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;600;700;800;900&family=Mulish:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #0C0414;
      font-family: 'Jost', sans-serif;
      position: relative;
      display: flex;
    }}

    /* Fondo ambiental profundo */
    .bg-canvas {{
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 20% 30%, rgba(76, 7, 140, 0.55) 0%, rgba(12, 4, 20, 0.98) 70%),
                  radial-gradient(circle at 85% 75%, rgba(42, 210, 197, 0.15) 0%, transparent 60%),
                  #0C0414;
      z-index: 1;
    }}

    /* Glow de marca detrás de Marbelis */
    .ambient-glow {{
      position: absolute;
      right: 120px;
      top: 150px;
      width: 700px;
      height: 700px;
      background: radial-gradient(circle, rgba(166, 105, 218, 0.28) 0%, rgba(46, 9, 129, 0.15) 50%, transparent 70%);
      filter: blur(60px);
      z-index: 2;
    }}

    /* Contenedor de la foto de Marbelis */
    .photo-wrapper {{
      position: absolute;
      right: -20px;
      bottom: 0;
      width: 1050px;
      height: 1080px;
      z-index: 3;
      display: flex;
      align-items: flex-end;
      justify-content: flex-end;
    }}

    .marbelis-img {{
      height: 1040px;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(-20px 10px 40px rgba(0,0,0,0.7));
    }}

    /* Máscaras de degradado para fundir suavemente con el fondo */
    .photo-fade-left {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, #0C0414 0%, rgba(12, 4, 20, 0.9) 12%, rgba(12, 4, 20, 0.4) 28%, transparent 48%);
      z-index: 4;
    }}

    .photo-fade-bottom {{
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      height: 240px;
      background: linear-gradient(to top, #0C0414 0%, rgba(12, 4, 20, 0.85) 40%, transparent 100%);
      z-index: 4;
    }}

    /* Viñeta general sutil */
    .vignette {{
      position: absolute;
      inset: 0;
      box-shadow: inset 0 0 120px rgba(0,0,0,0.85);
      z-index: 5;
      pointer-events: none;
    }}

    /* Contenedor del texto (Columna Izquierda) */
    .content-box {{
      position: relative;
      z-index: 6;
      width: 1050px;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-left: 110px;
      padding-right: 40px;
    }}

    /* Badge superior */
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: rgba(76, 7, 140, 0.45);
      border: 1.5px solid rgba(42, 210, 197, 0.7);
      backdrop-filter: blur(12px);
      padding: 10px 24px;
      border-radius: 50px;
      width: fit-content;
      margin-bottom: 28px;
    }}

    .badge-dot {{
      width: 10px;
      height: 10px;
      background: #2AD2C5;
      border-radius: 50%;
      box-shadow: 0 0 10px #2AD2C5;
    }}

    .badge-text {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 3px;
      color: #FFFFFF;
      text-transform: uppercase;
    }}

    /* Gran Titular Gancho */
    .hook-title {{
      font-size: 102px;
      line-height: 0.98;
      font-weight: 900;
      color: #FFFFFF;
      letter-spacing: -1.5px;
      text-transform: uppercase;
      text-shadow: 0 10px 30px rgba(0, 0, 0, 0.9), 0 2px 10px rgba(0, 0, 0, 0.8);
      margin-bottom: 28px;
    }}

    .hook-title .highlight {{
      color: {accent_color};
      text-shadow: 0 0 45px rgba(42, 210, 197, 0.4), 0 10px 25px rgba(0, 0, 0, 0.9);
      display: inline-block;
    }}

    /* Barra decorativa de separación */
    .accent-bar {{
      width: 120px;
      height: 6px;
      background: linear-gradient(to right, {accent_color}, #A669DA);
      border-radius: 3px;
      margin-bottom: 24px;
      box-shadow: 0 0 15px rgba(42, 210, 197, 0.5);
    }}

    /* Subtítulo pequeño (Título del episodio) */
    .subtitle-box {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .subtitle-icon {{
      color: {accent_color};
      font-size: 22px;
    }}

    .subtitle-text {{
      font-family: 'Mulish', sans-serif;
      font-size: 27px;
      font-weight: 700;
      color: #E6DCF5;
      letter-spacing: 0.5px;
      line-height: 1.35;
      max-width: 720px;
      text-shadow: 0 2px 8px rgba(0,0,0,0.8);
    }}

    /* Logo sutil en la esquina inferior izquierda */
    .brand-signature {{
      position: absolute;
      bottom: 55px;
      left: 110px;
      z-index: 6;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .signature-text {{
      font-size: 19px;
      font-weight: 700;
      letter-spacing: 4px;
      color: rgba(255, 255, 255, 0.45);
      text-transform: uppercase;
    }}

    /* Zona segura de YouTube (esquina inferior derecha) */
    /* YouTube coloca el timestamp en la esquina inferior derecha */
    .safe-zone-marker {{
      position: absolute;
      bottom: 24px;
      right: 24px;
      width: 160px;
      height: 48px;
      pointer-events: none;
      z-index: 10;
    }}
  </style>
</head>
<body>
  <div class="bg-canvas"></div>
  <div class="ambient-glow"></div>

  <!-- Foto de Marbelis -->
  <div class="photo-wrapper">
    <img src="{b64_img}" class="marbelis-img" alt="Marbelis Montero">
    <div class="photo-fade-left"></div>
    <div class="photo-fade-bottom"></div>
  </div>

  <div class="vignette"></div>

  <!-- Contenido de Texto -->
  <div class="content-box">
    <div class="badge-pill">
      <div class="badge-dot"></div>
      <div class="badge-text">{badge_text}</div>
    </div>

    <h1 class="hook-title">
      {hook_html}
    </h1>

    <div class="accent-bar"></div>

    <div class="subtitle-box">
      <div class="subtitle-text">{subtitle_text}</div>
    </div>
  </div>

  <div class="brand-signature">
    <div class="signature-text">REALMENTE · MARBELIS MONTERO</div>
  </div>
</body>
</html>"""

options = [
    {
        "id": "opcion_1_recomendada",
        "title": "Opción 1: Confrontación Empática (Recomendada)",
        "badge": "🎙️ EPISODIO #64",
        "hook": '¿POR QUÉ<br><span class="highlight">TE FALLAS?</span>',
        "subtitle": "El arte de no volverte a fallar",
        "img": b64_foto2,
        "accent": "#2AD2C5",
        "desc": "Con Foto 2 (sonrisa cálida y gesto de precisión). Conecta el dolor inmediato con la solución humana y cercana."
    },
    {
        "id": "opcion_2_accion",
        "title": "Opción 2: Llamado Tajante a la Lealtad Propia",
        "badge": "🎙️ EPISODIO #64",
        "hook": 'DEJA DE<br><span class="highlight">TRAICIONARTE</span>',
        "subtitle": "Aprende a estar de tu lado",
        "img": b64_foto1,
        "accent": "#FFD166", # Dorado de alto contraste
        "desc": "Con Foto 1 (mano abierta expresiva, intensidad conversacional). Impacto directo al autosabotaje."
    },
    {
        "id": "opcion_3_dilema",
        "title": "Opción 3: El Gran Dilema de Identidad",
        "badge": "🎙️ EPISODIO #64",
        "hook": '¿DE TU LADO<br>O EN TU <span class="highlight">CONTRA?</span>',
        "subtitle": "El arte de no volverte a fallar",
        "img": b64_foto2,
        "accent": "#2AD2C5",
        "desc": "Con Foto 2. Plantea la pregunta central del podcast para despertar curiosidad inmediata."
    }
]

async def render_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for opt in options:
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            html_content = generate_html(
                opt["id"],
                opt["hook"],
                opt["subtitle"],
                opt["badge"],
                opt["img"],
                accent_color=opt["accent"]
            )
            html_file = os.path.join(BASE_DIR, f"miniatura_ep64_{opt['id']}.html")
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            await page.set_content(html_content)
            await page.wait_for_timeout(600) # Ensure fonts and styles render
            
            png_file = os.path.join(BASE_DIR, f"miniatura_ep64_{opt['id']}.png")
            await page.screenshot(path=png_file, type="png")
            print(f"Rendered: {png_file}")
            await page.close()
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(render_all())
