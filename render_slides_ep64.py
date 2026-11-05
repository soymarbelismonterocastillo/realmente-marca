import asyncio
import os
import shutil
from playwright.async_api import async_playwright

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      width: 1080px;
      height: 1350px;
      overflow: hidden;
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      -webkit-font-smoothing: antialiased;
    }

    .slide {
      width: 1080px;
      height: 1350px;
      position: absolute;
      top: 0;
      left: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 75px 70px 65px;
    }

    /* FONDOS OFICIALES DE LA MARCA SEGÚN SKILL */
    #slide-1 { background: #12091C; color: #FFFFFF; } /* Portada Berenjena Profundo */
    #slide-2 { background: #0D3B38; color: #FFFFFF; } /* Turquesa Oscuro / Petróleo */
    #slide-3 { background: #2E0C59; color: #FFFFFF; } /* Violeta Loto */
    #slide-4 { background: #12101F; color: #FFFFFF; } /* Negro Carbón / Índigo */
    #slide-5 { background: linear-gradient(145deg, #2E0C59 0%, #4A0E4E 60%, #1A0536 100%); color: #FFFFFF; }

    /* HEADER SUPERIOR */
    .slide-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
    }

    .brand-logo {
      font-size: 23px;
      font-weight: 800;
      letter-spacing: 3px;
      color: #2AD2C5;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-logo .sparkle {
      color: #F59E0B;
      font-size: 24px;
    }

    .corner-badge {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.16);
      padding: 9px 22px;
      border-radius: 30px;
      font-size: 19px;
      font-weight: 600;
      color: #E2E8F0;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* CONTENEDOR DE TEXTO (CONCENTRADO ESTRICTAMENTE EN LOS PRIMEROS 600-650 PX) */
    .text-top-container {
      margin-top: 55px;
      display: flex;
      flex-direction: column;
      gap: 22px;
      max-width: 940px;
    }

    .prompt-headline {
      font-size: 44px;
      font-weight: 700;
      line-height: 1.28;
      color: #FFFFFF;
      letter-spacing: -0.5px;
    }

    /* TARJETA GLASSMORPHISM CON BORDE RESALTADO */
    .glass-card {
      background: rgba(0, 0, 0, 0.40);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-left: 5px solid #2AD2C5;
      border-radius: 20px;
      padding: 30px 38px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.35);
    }

    .card-text-highlight {
      font-size: 33px;
      font-weight: 600;
      line-height: 1.38;
      color: #FFFFFF;
    }

    .card-subtext {
      font-size: 29px;
      font-weight: 500;
      line-height: 1.4;
      color: #FFFFFF;
      margin-top: 10px;
    }

    .italic-note {
      font-size: 28px;
      font-style: italic;
      color: rgba(255, 255, 255, 0.88);
      font-weight: 500;
      line-height: 1.4;
      margin-top: 4px;
    }

    /* ZONA INFERIOR TOTALMENTE LIMPIA Y DESPEJADA PARA STICKERS / MEMES / FOTO */
    .sticker-free-zone {
      flex: 1;
      width: 100%;
      min-height: 520px;
    }

    /* FOOTER INFERIOR */
    .slide-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      padding-top: 20px;
      font-size: 19px;
      color: rgba(255, 255, 255, 0.45);
      font-weight: 500;
      letter-spacing: 0.5px;
    }
  </style>
</head>
<body>

  <!-- SLIDE 1: PORTADA (FONDO BERENJENA #12091C) -->
  <div class="slide" id="slide-1">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 64 • Podcast</div>
    </div>
    <div class="text-top-container" style="margin-top: 55px;">
      <h1 class="prompt-headline" style="font-size: 46px; line-height: 1.25;">
        Llegas puntual a cada cita ajena... <br>
        <span style="color: #2AD2C5; font-weight: 800;">pero a ti te dejas siempre para después. ⏳🪞</span>
      </h1>
      <div class="glass-card" style="border-left-color: #2AD2C5; background: rgba(0,0,0,0.45);">
        <div style="font-size: 20px; font-weight: 800; letter-spacing: 2px; color: #2AD2C5; text-transform: uppercase; margin-bottom: 8px;">LA GRAN INCOHERENCIA</div>
        <p class="card-text-highlight" style="font-size: 32px; line-height: 1.38; color: #FFFFFF;">
          ¿Por qué con el mundo entero eres un bálsamo de paciencia y comprensión, pero contigo te conviertes en un tribunal de fusilamiento?
        </p>
      </div>
      <div class="italic-note" style="color: #C084FC; font-weight: 600; font-size: 28px;">
        No te falta fuerza de voluntad: tienes tu cuenta interna en números rojos. 📉
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 2: EL DIAGNÓSTICO (TURQUESA OSCURO #0D3B38) -->
  <div class="slide" id="slide-2">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 64 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 43px;">
        Tu mente inconsciente te está mirando: <br>
        <span style="color: #2AD2C5; font-weight: 800;">cada promesa rota es un voto contra ti. ⚡</span>
      </div>
      <div class="glass-card" style="border-left-color: #2AD2C5;">
        <div class="card-text-highlight" style="font-size: 30px; font-weight: 500; line-height: 1.4;">
          Te comprometiste a 5 minutos para ti, pero ante una llamada ajena te cancelaste sin dudar para no incomodar.
        </div>
        <div class="card-subtext" style="color: #FFFFFF; font-size: 29px; font-weight: 700; line-height: 1.35; margin-top: 12px;">
          El cerebro registra el abandono: cada microacuerdo roto consolida la creencia biológica de que tu palabra no vale nada.
        </div>
      </div>
      <div class="italic-note" style="color: #2AD2C5; font-weight: 600; font-size: 28px;">
        ⚠️ Decirle sí a todos para complacer es la forma más rápida de decirte no a ti.
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 3: LA MÁSCARA AL DESCUBIERTO (VIOLETA LOTO #2E0C59) -->
  <div class="slide" id="slide-3">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 64 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 43px;">
        Querer pasar de 0 a 100 en un día... <br>
        <span style="color: #C084FC; font-weight: 800;">es la excusa perfecta para desertar. 🛑🚪</span>
      </div>
      <div class="glass-card" style="border-left-color: #C084FC; background: rgba(0,0,0,0.42);">
        <div class="card-text-highlight" style="font-size: 30px; font-weight: 500; line-height: 1.4; color: #FFFFFF;">
          Exigirte perfección inmediata o amenazarte con el látigo interno ante el primer tropiezo no es disciplina: es autosabotaje disfrazado de rigor.
          <div style="margin-top: 12px; font-size: 29px; line-height: 1.4; color: #2AD2C5; font-weight: 700;">
            La autoconfianza no se decreta con euforia: se construye con acuerdos de lo mínimo necesario, tan simples que sea imposible fallar.
          </div>
        </div>
      </div>
      <div class="italic-note" style="color: #D8B4FE; font-size: 28px; font-weight: 600;">
        💡 Primero es poco a poco, luego es poco a poco y después es poco a poco.
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 4: EL QUIEBRE SOMÁTICO Y PREGUNTA DE PODER (NEGRO CARBÓN #12101F) -->
  <div class="slide" id="slide-4">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 64 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 42px;">
        Si tu vida dependiera de contratarte... <br>
        <span style="color: #FB7185; font-weight: 800;">¿confiarías hoy en tu propia palabra? ⚖️👁️</span>
      </div>
      <div class="glass-card" style="border-left-color: #FB7185; background: rgba(0,0,0,0.5);">
        <div class="card-text-highlight" style="font-size: 30px; font-weight: 500; line-height: 1.4; color: #FFFFFF;">
          Si ves a una niña caer y rasparse las rodillas, jamás le darías golpes en el suelo. La abrazas y la levantas.
        </div>
        <div style="font-size: 29px; font-weight: 700; color: #2AD2C5; margin-top: 12px; line-height: 1.35;">
          Estar de tu lado no es ser un robot perfecto: es no declararte la guerra ni buscar un árbitro cuando te equivocas.
        </div>
      </div>
      <div class="italic-note" style="color: #FB7185; font-weight: 700; font-size: 28px;">
        👀 Ante el tropiezo: cero látigo. Aprender, reajustar y seguir.
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 5: RESOLUCIÓN DE PODER & CTA (GRADIENTE VIOLETA CIERRE) -->
  <div class="slide" id="slide-5">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 64 • Podcast</div>
    </div>
    <div class="text-top-container" style="align-items: center; text-align: center; margin-top: 48px;">
      <p style="font-size: 32px; color: #E2E8F0; line-height: 1.35; max-width: 860px;">
        Pasa tu cuenta interna a números verdes:<br>
        <span style="color: #FB7185; font-weight: 700;">tu palabra contigo es un contrato sagrado.</span>
      </p>
      <div style="font-size: 42px; font-weight: 800; color: #2AD2C5; margin: 24px 0 28px; text-shadow: 0 4px 20px rgba(0,0,0,0.5); line-height: 1.25; max-width: 900px;">
        «No te pidas una perfección inalcanzable: pídete presencia, respeto y contención diaria.»
      </div>
      <div class="glass-card" style="border-left: 5px solid #2AD2C5; border-right: 5px solid #2AD2C5; width: 100%; max-width: 880px; padding: 22px 34px; text-align: center;">
        <div style="font-size: 20px; font-weight: 800; letter-spacing: 2px; color: #2AD2C5; text-transform: uppercase;">🎙️ EPISODIO 64 • ESTRENO VIDEO PODCAST</div>
        <div style="font-size: 25px; font-weight: 700; color: #FFFFFF; margin-top: 8px;">RealMente estar de tu lado: el arte de no volverte a fallar.</div>
      </div>
      <div style="background: linear-gradient(135deg, #2AD2C5 0%, #14B8A6 100%); color: #072B28; padding: 22px 46px; border-radius: 50px; font-size: 32px; font-weight: 800; letter-spacing: 0.5px; box-shadow: 0 20px 45px rgba(0,0,0,0.5); width: 100%; max-width: 840px; margin-top: 26px;">
        💬 Comenta la palabra <span style="text-decoration: underline;">CONFIANZA</span>
      </div>
      <p style="font-size: 24px; color: #D4B2E6; margin-top: 14px; font-weight: 500;">
        y te envío la Hoja Guía del Acuerdo Mínimo Viable a tu DM 📩
      </p>
    </div>
    <div class="sticker-free-zone" style="min-height: 90px;"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>RealMente Podcast</span>
    </div>
  </div>

</body>
</html>
"""

async def render():
    out_dir_brain = r"C:\Users\soyma\.gemini\antigravity\brain\5ceb0b92-fe28-4051-bbf4-e627707149ac"
    out_dir_folder = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP64_Estar_de_Tu_Lado\05_Redes_Reels_y_Carruseles"
    out_dir_gdrive = r"G:\Mi unidad\MARCA\03_Contenido_Redes\Carruseles\C020_Estar_de_Tu_Lado_Ep64"

    os.makedirs(out_dir_brain, exist_ok=True)
    os.makedirs(out_dir_folder, exist_ok=True)
    os.makedirs(out_dir_gdrive, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})

        for i in range(1, 6):
            css_override = f"""
            <style>
              .slide {{ display: none !important; }}
              #slide-{i} {{ display: flex !important; }}
            </style>
            """
            full_html = HTML_TEMPLATE.replace('</head>', f'{css_override}</head>')

            await page.set_content(full_html)
            await page.wait_for_timeout(500)

            fn = f"slide_{i}_ep64.png"
            file_brain = os.path.join(out_dir_brain, fn)
            await page.screenshot(path=file_brain, type="png")
            print(f"Rendered Slide {i} -> {file_brain}")

            file_folder = os.path.join(out_dir_folder, fn)
            shutil.copy(file_brain, file_folder)
            print(f"Copied Slide {i} -> {file_folder}")

            try:
                file_gdrive = os.path.join(out_dir_gdrive, fn)
                shutil.copy(file_brain, file_gdrive)
                print(f"Copied Slide {i} -> {file_gdrive}")
            except Exception as e:
                print(f"Notice: Google Drive copy failed: {e}")

        await browser.close()
    print("Render completed successfully for all 5 slides of Episode 64!")

if __name__ == "__main__":
    asyncio.run(render())
