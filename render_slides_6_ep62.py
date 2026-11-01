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

    /* PALETA OFICIAL DE 6 SLIDES SEGÚN SKILL CARRETES */
    #slide-1 { background: #12091C; color: #FFFFFF; } /* Slide 1: Berenjena Profundo */
    #slide-2 { background: #0D3B38; color: #FFFFFF; } /* Slide 2: Petróleo / Turquesa Oscuro */
    #slide-3 { background: #2E0C59; color: #FFFFFF; } /* Slide 3: Violeta Loto */
    #slide-4 { background: #12101F; color: #FFFFFF; } /* Slide 4: Negro Carbón / Índigo */
    #slide-5 { background: #4A0E4E; color: #FFFFFF; } /* Slide 5: Ciruela / Uva Profundo */
    #slide-6 { background: linear-gradient(145deg, #2E0C59 0%, #4A0E4E 60%, #1A0536 100%); color: #FFFFFF; } /* Slide 6: Cierre */

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

    /* CONTENEDOR DE TEXTO (50% SUPERIOR LIBRE) */
    .text-top-container {
      margin-top: 50px;
      display: flex;
      flex-direction: column;
      gap: 22px;
      max-width: 940px;
    }

    .prompt-headline {
      font-size: 43px;
      font-weight: 700;
      line-height: 1.28;
      color: #FFFFFF;
      letter-spacing: -0.5px;
    }

    /* TARJETA GLASSMORPHISM */
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
      font-weight: 700;
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

    /* REGLA DEL 50% INFERIOR LIBRE */
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

  <!-- SLIDE 1: PORTADA / GANCHO DISRUPTIVO (#12091C) -->
  <div class="slide" id="slide-1">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 62 • Podcast</div>
    </div>
    <div class="text-top-container" style="margin-top: 55px;">
      <h1 class="prompt-headline" style="font-size: 47px; line-height: 1.25;">
        No estás siendo «prudente»... <br>
        <span style="color: #2AD2C5; font-weight: 800;">le tienes terror a que te llamen egoísta. 🚪⚡</span>
      </h1>
      <div class="glass-card" style="border-left-color: #2AD2C5; background: rgba(0,0,0,0.45);">
        <p class="card-text-highlight" style="font-size: 34px; line-height: 1.38; color: #FFFFFF;">
          En el segundo exacto en que vas a poner un límite o cobrar lo que vales, tu mente suelta a la culpa como perro guardián.
        </p>
      </div>
      <div class="italic-note" style="color: #C084FC; font-weight: 600; font-size: 29px;">
        La culpa no te avisa que estás haciendo daño: te avisa que estás a punto de salir de la jaula. ✨
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 2: EL DIAGNÓSTICO (#0D3B38) -->
  <div class="slide" id="slide-2">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 62 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 43px;">
        Tú no naciste con culpa: <br>
        <span style="color: #2AD2C5; font-weight: 800;">te la programaron para hacerte predecible. 🏛️</span>
      </div>
      <div class="glass-card" style="border-left-color: #2AD2C5;">
        <div class="card-text-highlight" style="font-size: 32px; font-weight: 500; line-height: 1.4;">
          Durante siglos se implantó el «deber ser» como alarma interna para mantenerte dócil sin necesidad de ponerte un policía las 24 horas.
        </div>
        <div class="card-subtext" style="color: #FFFFFF; font-size: 30px; font-weight: 700; line-height: 1.35; margin-top: 12px;">
          Romper el molde no es cometer un delito: es desafiar las normas que otros crearon para controlarte.
        </div>
      </div>
      <div class="italic-note" style="color: #2AD2C5; font-weight: 600; font-size: 28px;">
        ⚠️ Cada vez que te achicas para encajar, compras paz ajena con tu propia frustración.
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 3: DESMONTAR LA MÁSCARA (#2E0C59) -->
  <div class="slide" id="slide-3">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 62 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 43px;">
        El juego perverso de la culpa: <br>
        <span style="color: #C084FC;">la mesa en la que vives atrapada. 🪑</span>
      </div>
      <div class="glass-card" style="border-left-color: #C084FC; background: rgba(0,0,0,0.42);">
        <div class="card-text-highlight" style="font-size: 31px; font-weight: 500; line-height: 1.4; color: #FFFFFF;">
          Toda tu vida te la pasas rotando entre 4 esquinas:
          <div style="margin-top: 10px; font-size: 29px; line-height: 1.42;">
            • <strong style="color: #2AD2C5;">Lo Bueno vs. Lo Malo:</strong> juicios morales rígidos.<br>
            • <strong style="color: #C084FC;">Víctima vs. Victimaria:</strong> si dices no, te crees mala; si toleras todo, te refugias como la mártir abnegada.
          </div>
        </div>
      </div>
      <div class="italic-note" style="color: #D8B4FE; font-size: 28px;">
        💡 La culpa solo existe si previamente etiquetaste tu bienestar como algo «inaceptable».
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 4: EL QUIEBRE EN PNL (#12101F) -->
  <div class="slide" id="slide-4">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 62 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 42px;">
        Axioma liberador de PNL: <br>
        <span style="color: #FB7185;">Los hechos son neutros. El drama lo inventa tu cabeza. 🧠</span>
      </div>
      <div class="glass-card" style="border-left-color: #FB7185; background: rgba(0,0,0,0.5);">
        <div class="card-text-highlight" style="font-size: 32px; font-weight: 500; line-height: 1.4; color: #FFFFFF;">
          Decir «no puedo hoy» es un hecho neutro. El reproche moral es el invento de tu diálogo interno.
        </div>
        <div style="font-size: 30px; font-weight: 700; color: #2AD2C5; margin-top: 12px; line-height: 1.35;">
          Si alguien se molesta por tu límite, solo demuestra que su expectativa sobre ti se rompió.
        </div>
      </div>
      <div class="italic-note" style="color: #FB7185; font-weight: 700; font-size: 28px;">
        👀 Su enojo es su proceso: jamás tu condena.
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 5: EL GOLPE DE REALIDAD (#4A0E4E) -->
  <div class="slide" id="slide-5">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 62 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 42px;">
        ¿Por qué carajos compras paz ajena <br>
        <span style="color: #FB7185;">con tu propia frustración? ⏱️</span>
      </div>
      <div class="glass-card" style="border-left-color: #FB7185; background: rgba(0,0,0,0.48);">
        <div class="card-text-highlight" style="font-size: 32px; font-weight: 500; line-height: 1.4; color: #FFFFFF;">
          El precio de tu nueva identidad no es el dinero ni reventarte trabajando.
        </div>
        <div style="font-size: 30px; font-weight: 700; color: #2AD2C5; margin-top: 12px; line-height: 1.35;">
          El verdadero peaje es aprender a sostener la incomodidad transitoria de que tu entorno se desacomode cuando creces.
        </div>
      </div>
      <div class="italic-note" style="color: #C084FC; font-weight: 700; font-size: 28px;">
        🔥 Preferir ser «la niña buena que se sacrifica» es la trampa más cara de tu vida.
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 6: ROMPER EL TECHO, CIERRE & CTA (GRADIENTE VIOLETA CIERRE) -->
  <div class="slide" id="slide-6">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 62 • Podcast</div>
    </div>
    <div class="text-top-container" style="align-items: center; text-align: center; margin-top: 40px;">
      <p style="font-size: 26px; color: #C084FC; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
        Revelación de Identidad
      </p>
      <h2 style="font-size: 41px; font-weight: 800; color: #FFFFFF; line-height: 1.22; max-width: 900px; margin-top: -6px;">
        La culpa es el indicador de que <br>
        <span style="color: #2AD2C5;">estás rompiendo tu techo. 🚀</span>
      </h2>

      <div class="glass-card" style="border-left: 5px solid #2AD2C5; border-right: 5px solid #2AD2C5; width: 100%; max-width: 900px; padding: 22px 30px; text-align: center; background: rgba(0,0,0,0.5);">
        <p style="font-size: 26px; font-weight: 500; color: #E2E8F0; line-height: 1.35;">
          Si nunca sientes culpa, estás en piloto automático. La punzada no te frena: te avisa que pasaste de nivel.
        </p>
        <div style="font-size: 30px; font-weight: 800; color: #C084FC; margin-top: 10px; line-height: 1.3;">
          «No compro paz ajena con mi frustración. Sostengo la incomodidad de serle fiel a mí misma.»
        </div>
      </div>

      <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.18); border-radius: 18px; width: 100%; max-width: 900px; padding: 18px 24px; margin-top: 8px;">
        <div style="font-size: 19px; font-weight: 800; letter-spacing: 2px; color: #2AD2C5; text-transform: uppercase;">🎙️ REALMENTE PODCAST • REALMENTE CLUB</div>
        <div style="font-size: 24px; font-weight: 700; color: #FFFFFF; margin-top: 4px;">Episodio 62: La trampa de la culpa y el precio de tu nueva identidad</div>
      </div>

      <div style="background: linear-gradient(135deg, #2AD2C5 0%, #14B8A6 100%); color: #072B28; padding: 20px 40px; border-radius: 50px; font-size: 30px; font-weight: 800; letter-spacing: 0.5px; box-shadow: 0 16px 36px rgba(0,0,0,0.5); width: 100%; max-width: 820px; margin-top: 12px;">
        💬 Comenta la palabra <span style="text-decoration: underline;">PODCAST</span>
      </div>
      <p style="font-size: 24px; color: #D4B2E6; margin-top: 10px; font-weight: 600;">
        y te envío el episodio directo a tu DM 📩
      </p>
    </div>
    <div class="sticker-free-zone" style="min-height: 30px;"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>RealMente Podcast</span>
    </div>
  </div>

</body>
</html>
"""

async def render():
    out_dir_brain = r"C:\Users\soyma\.gemini\antigravity\brain\adf591c1-934b-4f97-bbfb-e3eebc5fe0a5"
    out_dir_folder = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\05_Redes_Reels_y_Carruseles"
    out_dir_gdrive = r"G:\Mi unidad\MARCA\03_Contenido_Redes\Carruseles\C018_La_Trampa_de_la_Culpa_Ep62"
    out_dir_root = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA"

    os.makedirs(out_dir_brain, exist_ok=True)
    os.makedirs(out_dir_folder, exist_ok=True)
    os.makedirs(out_dir_gdrive, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})

        for i in range(1, 7):
            css_override = f"""
            <style>
              .slide {{ display: none !important; }}
              #slide-{i} {{ display: flex !important; }}
            </style>
            """
            full_html = HTML_TEMPLATE.replace('</head>', f'{css_override}</head>')

            await page.set_content(full_html)
            await page.wait_for_timeout(400)

            fn = f"slide_{i}_ep62.png"
            file_brain = os.path.join(out_dir_brain, fn)
            await page.screenshot(path=file_brain, type="png")
            print(f"Rendered Slide {i} -> {file_brain}")

            file_folder = os.path.join(out_dir_folder, fn)
            shutil.copy(file_brain, file_folder)
            print(f"Copied Slide {i} -> {file_folder}")

            file_root = os.path.join(out_dir_root, fn)
            shutil.copy(file_brain, file_root)

            try:
                file_gdrive = os.path.join(out_dir_gdrive, fn)
                shutil.copy(file_brain, file_gdrive)
                print(f"Copied Slide {i} -> {file_gdrive}")
            except Exception as e:
                print(f"Notice: Google Drive copy failed: {e}")

        await browser.close()
    print("Render completed successfully for all 6 slides of Episode 62!")

if __name__ == "__main__":
    asyncio.run(render())
