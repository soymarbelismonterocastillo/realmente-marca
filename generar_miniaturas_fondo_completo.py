import asyncio
import os
import base64
from playwright.async_api import async_playwright

BASE_DIR = r"C:/Users/soyma/OneDrive/Documents/ANTIGRAVITY/MARCA/Episodios/EP64_Estar_de_Tu_Lado/02_Podcast_Guion_y_Grabacion"

def to_base64_src(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

b64_full_opt2 = to_base64_src(os.path.join(BASE_DIR, "full_frame_opt2.png"))
b64_full_opt1 = to_base64_src(os.path.join(BASE_DIR, "full_frame_opt1.png"))

# =========================================================================
# DISEÑO 1: INSPIRADO EN REF 1 (Matthew McConaughey / Modern Wisdom Podcast)
# Foto completa de fondo + Sombra lateral cinematográfica + Titular Gigante + Línea divisoria
# =========================================================================
html_opcion_1 = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;600;700;800;900&family=Mulish:wght@600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #0A0314;
      font-family: 'Jost', sans-serif;
      position: relative;
    }}

    /* Foto de fondo 100% COMPLETA sin recortes */
    .bg-full-photo {{
      position: absolute;
      inset: 0;
      width: 1920px;
      height: 1080px;
      object-fit: cover;
      z-index: 1;
    }}

    /* Degradado de sombra en el lateral izquierdo para que el texto resalte al 100% */
    .shadow-overlay-left {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        to right,
        rgba(10, 3, 22, 0.96) 0%,
        rgba(12, 4, 25, 0.90) 30%,
        rgba(14, 5, 30, 0.65) 48%,
        rgba(14, 5, 30, 0.20) 65%,
        transparent 80%
      );
      z-index: 2;
    }}

    /* Viñeta perimetral cinematográfica */
    .cinema-vignette {{
      position: absolute;
      inset: 0;
      box-shadow: inset 0 0 160px rgba(0, 0, 0, 0.75);
      z-index: 3;
      pointer-events: none;
    }}

    /* Resplandor violeta ambiental sutil */
    .ambient-glow {{
      position: absolute;
      left: 100px;
      top: 150px;
      width: 700px;
      height: 700px;
      background: radial-gradient(circle, rgba(76, 7, 140, 0.45) 0%, transparent 70%);
      filter: blur(80px);
      z-index: 2;
    }}

    /* Contenido de texto en la zona izquierda */
    .content-box {{
      position: relative;
      z-index: 4;
      width: 1050px;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-left: 110px;
      padding-right: 40px;
    }}

    /* Badge Episodio */
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: rgba(46, 9, 129, 0.75);
      border: 1.5px solid #2AD2C5;
      backdrop-filter: blur(12px);
      padding: 10px 26px;
      border-radius: 50px;
      width: fit-content;
      margin-bottom: 26px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5), 0 0 15px rgba(42, 210, 197, 0.3);
    }}

    .badge-dot {{
      width: 10px;
      height: 10px;
      background: #2AD2C5;
      border-radius: 50%;
      box-shadow: 0 0 10px #2AD2C5;
    }}

    .badge-text {{
      font-size: 23px;
      font-weight: 800;
      letter-spacing: 3px;
      color: #FFFFFF;
      text-transform: uppercase;
    }}

    /* Gran Titular Gancho estilo McConaughey / Modern Wisdom */
    .hook-title {{
      font-size: 112px;
      line-height: 0.94;
      font-weight: 900;
      color: #FFFFFF;
      letter-spacing: -2px;
      text-transform: uppercase;
      text-shadow: 0 10px 30px rgba(0, 0, 0, 0.95), 0 2px 10px rgba(0, 0, 0, 0.9);
      margin-bottom: 26px;
    }}

    .hook-title .highlight {{
      color: #2AD2C5;
      text-shadow: 0 0 40px rgba(42, 210, 197, 0.6), 0 10px 25px rgba(0, 0, 0, 0.95);
      display: block;
    }}

    /* Línea gráfica de acento horizontal */
    .accent-bar {{
      width: 140px;
      height: 6px;
      background: linear-gradient(to right, #2AD2C5, #BA81C9);
      border-radius: 3px;
      margin-bottom: 24px;
      box-shadow: 0 0 16px rgba(42, 210, 197, 0.5);
    }}

    /* Subtítulo oficial del episodio */
    .subtitle-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-width: 760px;
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
      letter-spacing: 0.3px;
      line-height: 1.35;
      text-shadow: 0 2px 10px rgba(0,0,0,0.85);
    }}

    /* Firma de Marca */
    .footer-brand {{
      position: absolute;
      bottom: 50px;
      left: 110px;
      z-index: 4;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .footer-brand span {{
      font-size: 19px;
      font-weight: 800;
      letter-spacing: 4px;
      color: rgba(255, 255, 255, 0.5);
      text-transform: uppercase;
    }}

    .footer-brand .dot {{
      width: 6px;
      height: 6px;
      background: #2AD2C5;
      border-radius: 50%;
    }}
  </style>
</head>
<body>
  <img src="{b64_full_opt2}" class="bg-full-photo" alt="Marbelis Montero">
  <div class="ambient-glow"></div>
  <div class="shadow-overlay-left"></div>
  <div class="cinema-vignette"></div>

  <div class="content-box">
    <div class="badge-pill">
      <div class="badge-dot"></div>
      <div class="badge-text">🎙️ EPISODIO #64</div>
    </div>

    <h1 class="hook-title">
      ¿POR QUÉ
      <span class="highlight">TE FALLAS?</span>
    </h1>

    <div class="accent-bar"></div>

    <div class="subtitle-wrapper">
      <div class="subtitle-label">TEMA DEL EPISODIO</div>
      <div class="subtitle-text">RealMente estar de tu lado: el arte de no volverte a fallar</div>
    </div>
  </div>

  <div class="footer-brand">
    <span>REALMENTE</span>
    <div class="dot"></div>
    <span>MARBELIS MONTERO</span>
  </div>
</body>
</html>"""

# =========================================================================
# DISEÑO 2: INSPIRADO EN REF 1B (Cajas de Alto Contraste tipo The Honest Bunch)
# Bloques sólidos de color que saltan al instante en YouTube
# =========================================================================
html_opcion_2 = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@700;800;900&family=Mulish:wght@700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #0A0314;
      font-family: 'Jost', sans-serif;
      position: relative;
    }}

    .bg-full-photo {{
      position: absolute;
      inset: 0;
      width: 1920px;
      height: 1080px;
      object-fit: cover;
      z-index: 1;
    }}

    .shadow-overlay-left {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        to right,
        rgba(10, 3, 22, 0.95) 0%,
        rgba(12, 4, 25, 0.88) 32%,
        rgba(14, 5, 30, 0.55) 50%,
        transparent 75%
      );
      z-index: 2;
    }}

    .cinema-vignette {{
      position: absolute;
      inset: 0;
      box-shadow: inset 0 0 160px rgba(0, 0, 0, 0.75);
      z-index: 3;
      pointer-events: none;
    }}

    .content-box {{
      position: relative;
      z-index: 4;
      width: 1100px;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-left: 110px;
      gap: 16px;
    }}

    .badge-box {{
      display: inline-block;
      background: #4C078C;
      color: #FFFFFF;
      font-size: 22px;
      font-weight: 800;
      letter-spacing: 3px;
      padding: 8px 22px;
      border-radius: 6px;
      width: fit-content;
      text-transform: uppercase;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
      border-left: 5px solid #2AD2C5;
    }}

    /* Cajas apiladas de alto impacto */
    .box-block {{
      display: inline-block;
      width: fit-content;
      padding: 12px 28px;
      font-size: 96px;
      line-height: 1;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -1px;
      border-radius: 8px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.7);
    }}

    .box-dark {{
      background: #0E031A;
      color: #FFFFFF;
      border-left: 8px solid #FFD166;
    }}

    .box-yellow {{
      background: #FFD166;
      color: #0E031A;
    }}

    .subtitle-card {{
      margin-top: 10px;
      background: rgba(14, 3, 26, 0.85);
      border: 1px solid rgba(255, 209, 102, 0.5);
      backdrop-filter: blur(10px);
      padding: 14px 26px;
      border-radius: 8px;
      max-width: 720px;
    }}

    .subtitle-card p {{
      font-family: 'Mulish', sans-serif;
      font-size: 26px;
      font-weight: 700;
      color: #F8F5FF;
      line-height: 1.3;
    }}

    .footer-brand {{
      position: absolute;
      bottom: 50px;
      left: 110px;
      z-index: 4;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .footer-brand span {{
      font-size: 19px;
      font-weight: 800;
      letter-spacing: 4px;
      color: rgba(255, 255, 255, 0.5);
      text-transform: uppercase;
    }}
  </style>
</head>
<body>
  <img src="{b64_full_opt2}" class="bg-full-photo" alt="Marbelis Montero">
  <div class="shadow-overlay-left"></div>
  <div class="cinema-vignette"></div>

  <div class="content-box">
    <div class="badge-box">🎙️ EPISODIO #64</div>
    <div class="box-block box-dark">DEJA DE</div>
    <div class="box-block box-yellow">FALLARTE</div>

    <div class="subtitle-card">
      <p>RealMente estar de tu lado: el arte de no volverte a fallar</p>
    </div>
  </div>

  <div class="footer-brand">
    <span>REALMENTE · MARBELIS MONTERO</span>
  </div>
</body>
</html>"""

# =========================================================================
# DISEÑO 3: INSPIRADO EN REF 2 (Creator Doodles, Outline y Conceptos Clave)
# Líneas orgánicas, contorno trazado, frases satélites con flechas y comillas
# =========================================================================
html_opcion_3 = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Jost:ital,wght@0,700;0,800;0,900;1,700;1,800&family=Mulish:ital,wght@0,600;0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: #000000;
      font-family: 'Jost', sans-serif;
      position: relative;
    }}

    /* Foto de fondo 100% COMPLETA */
    .bg-full-photo {{
      position: absolute;
      inset: 0;
      width: 1920px;
      height: 1080px;
      object-fit: cover;
      filter: contrast(1.08) brightness(0.92);
      z-index: 1;
    }}

    /* Viñeta perimetral oscura para contrastar los textos y doodles */
    .cinema-vignette {{
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 45%, transparent 35%, rgba(10, 3, 20, 0.75) 85%);
      z-index: 2;
      pointer-events: none;
    }}

    .shadow-bottom {{
      position: absolute;
      left: 0; right: 0; bottom: 0;
      height: 280px;
      background: linear-gradient(to top, rgba(10, 3, 20, 0.95) 0%, rgba(10, 3, 20, 0.6) 60%, transparent 100%);
      z-index: 2;
    }}

    /* Capa SVG para líneas, flechas y trazos orgánicos tipo doodle */
    .doodle-layer {{
      position: absolute;
      inset: 0;
      width: 1920px;
      height: 1080px;
      z-index: 3;
      pointer-events: none;
    }}

    /* Frases satélite estilo Referencia 2 */
    .satellite-tag {{
      position: absolute;
      z-index: 4;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .tag-title {{
      font-family: 'Mulish', sans-serif;
      font-style: italic;
      font-weight: 800;
      font-size: 38px;
      color: #FFFFFF;
      text-shadow: 0 4px 15px rgba(0,0,0,0.9), 0 2px 5px rgba(0,0,0,0.9);
      line-height: 1.15;
    }}

    .tag-highlight {{
      color: #2AD2C5;
      text-transform: uppercase;
      font-weight: 900;
      letter-spacing: 1px;
    }}

    /* Posiciones de etiquetas */
    .pos-top-right {{
      top: 80px;
      right: 120px;
      text-align: right;
    }}

    .pos-top-left {{
      top: 90px;
      left: 90px;
    }}

    .pos-mid-left {{
      top: 360px;
      left: 80px;
      max-width: 380px;
    }}

    /* Badge Episodio estilo sticker */
    .badge-sticker {{
      display: inline-block;
      background: #4C078C;
      border: 2px solid #2AD2C5;
      color: #FFFFFF;
      font-size: 24px;
      font-weight: 900;
      letter-spacing: 3px;
      padding: 8px 24px;
      border-radius: 40px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.8);
      margin-bottom: 12px;
      width: fit-content;
    }}

    /* Gran Titular Inferior Entre Comillas (Como en Ref 2: "NO LE DEBES NADA A NADIE") */
    .bottom-quote-bar {{
      position: absolute;
      bottom: 60px;
      left: 0;
      right: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 4;
      text-align: center;
    }}

    .quote-text {{
      font-size: 88px;
      font-weight: 900;
      color: #FFFFFF;
      text-transform: uppercase;
      letter-spacing: 0px;
      text-shadow: 0 10px 30px rgba(0,0,0,0.95), 0 2px 8px rgba(0,0,0,0.9);
      background: rgba(14, 3, 26, 0.75);
      border: 2px solid rgba(42, 210, 197, 0.6);
      backdrop-filter: blur(12px);
      padding: 12px 50px;
      border-radius: 20px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.8), 0 0 20px rgba(42, 210, 197, 0.25);
    }}

    .quote-text .accent {{
      color: #2AD2C5;
    }}

    .quote-sub {{
      margin-top: 10px;
      font-family: 'Mulish', sans-serif;
      font-size: 26px;
      font-weight: 700;
      color: #EBDFFC;
      letter-spacing: 2px;
      text-transform: uppercase;
      text-shadow: 0 2px 10px rgba(0,0,0,0.9);
    }}
  </style>
</head>
<body>
  <img src="{b64_full_opt2}" class="bg-full-photo" alt="Marbelis Montero">
  <div class="cinema-vignette"></div>
  <div class="shadow-bottom"></div>

  <!-- SVG con flechas doodle y líneas de resalte -->
  <svg class="doodle-layer" viewBox="0 0 1920 1080">
    <!-- Flecha hacia la derecha arriba -->
    <path d="M 1480 210 Q 1400 240 1340 300" fill="none" stroke="#2AD2C5" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="8 6"/>
    <polygon points="1340,300 1358,285 1350,306" fill="#2AD2C5"/>

    <!-- Flecha hacia la izquierda (microacuerdos) -->
    <path d="M 380 430 Q 520 420 620 450" fill="none" stroke="#FFD166" stroke-width="4.5" stroke-linecap="round" stroke-dasharray="8 6"/>
    <polygon points="620,450 600,438 605,458" fill="#FFD166"/>

    <!-- Contorno doodle blanco alrededor de Marbelis estilo Ref 2 -->
    <path d="M 520 850 Q 500 680 580 520 Q 640 400 710 320 Q 820 180 980 160 Q 1140 180 1220 300 Q 1300 420 1350 560 Q 1420 700 1440 850" 
          fill="none" stroke="rgba(255, 255, 255, 0.75)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="12 8"
          filter="drop-shadow(0 0 8px rgba(255,255,255,0.6))"/>
  </svg>

  <!-- Etiquetas satélite estilo Ref 2 -->
  <div class="satellite-tag pos-top-left">
    <div class="badge-sticker">🎙️ EPISODIO #64</div>
    <div class="tag-title">¿te castigas o<br><span class="tag-highlight">te sostienes?</span></div>
  </div>

  <div class="satellite-tag pos-top-right">
    <div class="tag-title">dejar de fallarte &<br><span class="tag-highlight">ESTAR DE TU LADO</span></div>
  </div>

  <div class="satellite-tag pos-mid-left">
    <div class="tag-title" style="font-size:32px;color:#FFD166;">
      microacuerdos de PNL<br><span style="font-size:24px;color:#FFFFFF;font-weight:600;font-style:normal;">para recuperar tu palabra</span>
    </div>
  </div>

  <!-- Gran Frase Inferior en comillas estilo Ref 2 -->
  <div class="bottom-quote-bar">
    <div class="quote-text">
      "NO TE VUELVAS A <span class="accent">FALLAR</span>"
    </div>
    <div class="quote-sub">
      RealMente · El arte de estar de tu lado
    </div>
  </div>
</body>
</html>"""

render_tasks = [
    {
        "name": "miniatura_fondo_completo_estilo_mcconaughey.png",
        "html_file": "miniatura_fondo_completo_estilo_mcconaughey.html",
        "html_content": html_opcion_1
    },
    {
        "name": "miniatura_fondo_completo_estilo_boxes.png",
        "html_file": "miniatura_fondo_completo_estilo_boxes.html",
        "html_content": html_opcion_2
    },
    {
        "name": "miniatura_fondo_completo_estilo_doodles_ref2.png",
        "html_file": "miniatura_fondo_completo_estilo_doodles_ref2.html",
        "html_content": html_opcion_3
    }
]

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for t in render_tasks:
            h_path = os.path.join(BASE_DIR, t["html_file"])
            with open(h_path, "w", encoding="utf-8") as f:
                f.write(t["html_content"])
            
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            await page.set_content(t["html_content"])
            await page.wait_for_timeout(700)
            
            out_img = os.path.join(BASE_DIR, t["name"])
            await page.screenshot(path=out_img, type="png")
            print(f"Rendered: {out_img}")
            await page.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
