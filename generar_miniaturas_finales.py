import asyncio
import os
import base64
from playwright.async_api import async_playwright

BASE_DIR = r"C:/Users/soyma/OneDrive/Documents/ANTIGRAVITY/MARCA/Episodios/EP64_Estar_de_Tu_Lado/02_Podcast_Guion_y_Grabacion"

with open(os.path.join(BASE_DIR, "marbelis_tight_crop.png"), "rb") as f:
    b64_marbelis = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

def build_html(hook_html, subtitle_text, badge_text="EPISODIO #64", accent_color="#2AD2C5"):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;700;800;900&family=Mulish:wght@600;700;800&display=swap" rel="stylesheet">
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
      background: #0E031A;
      font-family: 'Jost', sans-serif;
      position: relative;
      display: flex;
    }}

    /* Fondo degradado envolvente RealMente */
    .bg-canvas {{
      position: absolute;
      inset: 0;
      background: 
        radial-gradient(circle at 18% 38%, rgba(76, 7, 140, 0.82) 0%, rgba(14, 3, 26, 0.98) 65%),
        radial-gradient(circle at 75% 45%, rgba(46, 9, 129, 0.60) 0%, rgba(14, 3, 26, 0.95) 75%),
        #0E031A;
      z-index: 1;
    }}

    /* Glow de luz lila/violeta ambiental */
    .glow-violet {{
      position: absolute;
      right: 180px;
      top: 100px;
      width: 750px;
      height: 750px;
      background: radial-gradient(circle, rgba(166, 105, 218, 0.35) 0%, rgba(76, 7, 140, 0.20) 45%, transparent 70%);
      filter: blur(80px);
      z-index: 2;
    }}

    /* Foto de Marbelis en alta resolución */
    .photo-container {{
      position: absolute;
      right: 0;
      bottom: 0;
      width: 906px;
      height: 1080px;
      z-index: 3;
    }}

    .photo-container img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}

    /* Viñetas ambientales suaves para fundir el fondo con el estudio */
    .photo-vignette-top {{
      position: absolute;
      right: 0;
      top: 0;
      width: 906px;
      height: 380px;
      background: linear-gradient(to bottom, rgba(14, 3, 26, 0.88) 0%, rgba(14, 3, 26, 0.45) 45%, transparent 100%);
      pointer-events: none;
      z-index: 4;
    }}
    .photo-vignette-right {{
      position: absolute;
      right: 0;
      top: 0;
      width: 320px;
      height: 1080px;
      background: linear-gradient(to left, rgba(14, 3, 26, 0.85) 0%, rgba(14, 3, 26, 0.3) 50%, transparent 100%);
      pointer-events: none;
      z-index: 4;
    }}
    .photo-vignette-left {{
      position: absolute;
      right: 600px;
      top: 0;
      width: 320px;
      height: 1080px;
      background: linear-gradient(to right, rgba(14, 3, 26, 0.95) 0%, rgba(14, 3, 26, 0.4) 50%, transparent 100%);
      pointer-events: none;
      z-index: 4;
    }}
    .photo-vignette-bottom {{
      position: absolute;
      right: 0;
      bottom: 0;
      width: 906px;
      height: 200px;
      background: linear-gradient(to top, rgba(14, 3, 26, 0.95) 0%, transparent 100%);
      pointer-events: none;
      z-index: 4;
    }}

    .vignette {{
      position: absolute;
      inset: 0;
      box-shadow: inset 0 0 140px rgba(0,0,0,0.85);
      z-index: 5;
      pointer-events: none;
    }}

    /* Columna de Texto y Jerarquía Visual */
    .content-area {{
      position: relative;
      z-index: 6;
      width: 1080px;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-left: 120px;
      padding-right: 20px;
    }}

    /* Insignia / Badge de Episodio */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: rgba(76, 7, 140, 0.60);
      border: 1.5px solid rgba(42, 210, 197, 0.85);
      backdrop-filter: blur(14px);
      padding: 12px 28px;
      border-radius: 50px;
      width: fit-content;
      margin-bottom: 32px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4), 0 0 15px rgba(42, 210, 197, 0.25);
    }}

    .badge-icon {{
      font-size: 22px;
    }}

    .badge-text {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 3.5px;
      color: #FFFFFF;
      text-transform: uppercase;
    }}

    /* Gran Titular Gancho */
    .main-hook {{
      font-size: 108px;
      line-height: 0.96;
      font-weight: 900;
      color: #FFFFFF;
      letter-spacing: -2px;
      text-transform: uppercase;
      text-shadow: 0 10px 35px rgba(0, 0, 0, 0.95), 0 2px 8px rgba(0, 0, 0, 0.9);
      margin-bottom: 32px;
    }}

    .main-hook .accent {{
      color: {accent_color};
      text-shadow: 0 0 45px rgba(42, 210, 197, 0.5), 0 10px 30px rgba(0, 0, 0, 0.95);
      display: inline-block;
    }}

    /* Barra divisoria de estilo */
    .divider-line {{
      width: 140px;
      height: 6px;
      background: linear-gradient(to right, {accent_color}, #BA81C9);
      border-radius: 4px;
      margin-bottom: 26px;
      box-shadow: 0 0 16px rgba(42, 210, 197, 0.5);
    }}

    /* Subtítulo (Título Oficial del Episodio) */
    .subtitle-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-width: 780px;
    }}

    .subtitle-label {{
      font-size: 16px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: rgba(42, 210, 197, 0.9);
    }}

    .subtitle-text {{
      font-family: 'Mulish', sans-serif;
      font-size: 28px;
      font-weight: 700;
      color: #F0EBFA;
      letter-spacing: 0.2px;
      line-height: 1.35;
      text-shadow: 0 2px 10px rgba(0,0,0,0.85);
    }}

    /* Firma de Marca al pie */
    .footer-brand {{
      position: absolute;
      bottom: 50px;
      left: 120px;
      z-index: 6;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .footer-brand span {{
      font-size: 19px;
      font-weight: 800;
      letter-spacing: 4px;
      color: rgba(255, 255, 255, 0.45);
      text-transform: uppercase;
    }}

    .footer-brand .dot {{
      width: 6px;
      height: 6px;
      background: {accent_color};
      border-radius: 50%;
    }}
  </style>
</head>
<body>
  <div class="bg-canvas"></div>
  <div class="glow-violet"></div>

  <!-- Foto de Marbelis -->
  <div class="photo-container">
    <img src="{b64_marbelis}" alt="Marbelis Montero">
  </div>

  <div class="photo-vignette-top"></div>
  <div class="photo-vignette-right"></div>
  <div class="photo-vignette-left"></div>
  <div class="photo-vignette-bottom"></div>

  <div class="vignette"></div>

  <!-- Contenido de Texto -->
  <div class="content-area">
    <div class="badge">
      <span class="badge-icon">🎙️</span>
      <span class="badge-text">{badge_text}</span>
    </div>

    <h1 class="main-hook">
      {hook_html}
    </h1>

    <div class="divider-line"></div>

    <div class="subtitle-wrapper">
      <div class="subtitle-label">TEMA DEL EPISODIO</div>
      <div class="subtitle-text">{subtitle_text}</div>
    </div>
  </div>

  <div class="footer-brand">
    <span>REALMENTE</span>
    <div class="dot"></div>
    <span>MARBELIS MONTERO</span>
  </div>
</body>
</html>"""

variants = [
    {
        "file_name": "miniatura_ep64_opcion_1_recomendada.png",
        "html_name": "miniatura_ep64_opcion_1_recomendada.html",
        "badge": "EPISODIO #64",
        "hook": '¿POR QUÉ<br><span class="accent">TE FALLAS?</span>',
        "subtitle": "RealMente estar de tu lado: el arte de no volverte a fallar",
        "accent": "#2AD2C5"
    },
    {
        "file_name": "miniatura_ep64_opcion_2_accion.png",
        "html_name": "miniatura_ep64_opcion_2_accion.html",
        "badge": "EPISODIO #64",
        "hook": 'DEJA DE<br><span class="accent" style="color:#FFD166;text-shadow:0 0 45px rgba(255,209,102,0.5),0 10px 30px rgba(0,0,0,0.95);">FALLARTE</span>',
        "subtitle": "El arte de estar de tu lado y sostener tu palabra",
        "accent": "#FFD166"
    },
    {
        "file_name": "miniatura_ep64_opcion_3_dilema.png",
        "html_name": "miniatura_ep64_opcion_3_dilema.html",
        "badge": "EPISODIO #64",
        "hook": '¿DE TU LADO<br>O EN TU <span class="accent">CONTRA?</span>',
        "subtitle": "El arte de no volverte a fallar jamás",
        "accent": "#2AD2C5"
    }
]

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for v in variants:
            html = build_html(v["hook"], v["subtitle"], v["badge"], v["accent"])
            html_path = os.path.join(BASE_DIR, v["html_name"])
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            await page.set_content(html)
            await page.wait_for_timeout(600)
            
            out_img = os.path.join(BASE_DIR, v["file_name"])
            await page.screenshot(path=out_img, type="png")
            print(f"Rendered: {out_img}")
            await page.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
