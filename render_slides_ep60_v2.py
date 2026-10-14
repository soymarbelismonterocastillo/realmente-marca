import asyncio
from playwright.async_api import async_playwright
import os, shutil

HTML_TEMPLATE = """
<!DOCTYPE html>
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

    /* FONDOS EXACTOS DE LA MARCA (SEGUN CAPTURAS OFICIALES) */
    #slide-1 { background: #12091C; color: #FFFFFF; } /* Portada Berenjena Profundo */
    #slide-2 { background: #0D3B38; color: #FFFFFF; } /* Turquesa Oscuro / Petróleo */
    #slide-3 { background: #2E0C59; color: #FFFFFF; } /* Violeta Loto */
    #slide-4 { background: #12101F; color: #FFFFFF; } /* Negro Carbón / Índigo */
    #slide-5 { background: #4A0E4E; color: #FFFFFF; } /* Morado Uva */
    #slide-6 { background: linear-gradient(145deg, #2E0C59 0%, #4A0E4E 60%, #1A0536 100%); color: #FFFFFF; }

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

    /* CONTENEDOR DE TEXTO (POSICIONADO EN LA MITAD SUPERIOR) */
    .text-top-container {
      margin-top: 55px;
      display: flex;
      flex-direction: column;
      gap: 26px;
      max-width: 940px;
    }

    .prompt-headline {
      font-size: 42px;
      font-weight: 700;
      line-height: 1.35;
      color: #FFFFFF;
      letter-spacing: -0.5px;
    }

    /* TARJETA GLASSMORPHISM CON BORDE RESALTADO */
    .glass-card {
      background: rgba(0, 0, 0, 0.38);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-left: 5px solid #2AD2C5;
      border-radius: 20px;
      padding: 36px 42px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.3);
    }

    .card-text-highlight {
      font-size: 38px;
      font-weight: 700;
      line-height: 1.38;
      color: #FFFFFF;
    }

    .card-subtext {
      font-size: 32px;
      font-weight: 600;
      line-height: 1.4;
      color: #2AD2C5;
      margin-top: 14px;
    }

    .italic-note {
      font-size: 32px;
      font-style: italic;
      color: rgba(255, 255, 255, 0.82);
      font-weight: 500;
      line-height: 1.4;
      margin-top: 4px;
    }

    /* ZONA INFERIOR TOTALMENTE LIMPIA Y DESPEJADA PARA STICKERS / MEMES */
    .sticker-free-zone {
      flex: 1;
      width: 100%;
      min-height: 480px;
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

  <!-- SLIDE 1: PORTADA -->
  <div class="slide" id="slide-1">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    </div>
    <div class="text-top-container" style="margin-top: 75px;">
      <h1 class="prompt-headline" style="font-size: 50px; line-height: 1.28; margin-bottom: 8px;">
        El universo no te va a mandar <br>
        <span style="color: #2AD2C5; font-weight: 800;">un WhatsApp. 📱</span>
      </h1>
      <div class="glass-card" style="border-left-color: #A78BFA; background: rgba(0,0,0,0.42);">
        <p class="card-text-highlight" style="font-size: 36px; line-height: 1.4; color: #FFFFFF;">
          Y Mercurio retrógrado <span style="color: #F87171; font-weight: 800;">NO</span> tiene la culpa de que te dé pavor tomar una decisión. ⚡🚪
        </p>
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 2: EL IMPACTO (TURQUESA OSCURO #0D3B38) -->
  <div class="slide" id="slide-2">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline">
        Porque no decidir...
      </div>
      <div class="glass-card" style="border-left-color: #2AD2C5;">
        <div class="card-text-highlight">
          ya es una decisión:
        </div>
        <div class="card-subtext" style="color: #2AD2C5; font-size: 36px; margin-top: 14px;">
          TE ESTÁS QUEDANDO EN EL LIMBO PARA QUE ALGUIEN MÁS ELIJA POR TI.
        </div>
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 3: LA MÁSCARA (VIOLETA LOTO #2E0C59) -->
  <div class="slide" id="slide-3">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline" style="font-size: 38px;">
        Lees el horóscopo, buscas señales, pides opiniones a medio mundo con tal de evitar esa decisión incómoda...
      </div>
      <div class="glass-card" style="border-left-color: #C084FC;">
        <div class="card-text-highlight" style="font-size: 40px; color: #FFFFFF;">
          “Eso no es paciencia: <br>
          <span style="color: #2AD2C5;">es cobardía con aroma a incienso.” 🕯️</span>
        </div>
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 4: EL CUCHILLO AL ESTÓMAGO (NEGRO CARBÓN #12101F) -->
  <div class="slide" id="slide-4">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline">
        Hasta que te miras al espejo y te haces la pregunta prohibida:
      </div>
      <div class="glass-card" style="border-left-color: #A78BFA; background: rgba(0,0,0,0.5);">
        <div class="card-text-highlight" style="color: #A78BFA; font-size: 42px;">
          “¿Cuántos años más de tu vida vas a tirar a la basura esperando una señal divina?”
        </div>
      </div>
      <div class="italic-note" style="color: #FB7185; font-weight: 700;">
        Te estás haciendo vieja en la indecisión... 👀
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 5: EL GOLPE DE REALIDAD (MORADO UVA #4A0E4E) -->
  <div class="slide" id="slide-5">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    </div>
    <div class="text-top-container">
      <div class="prompt-headline">
        Porque el día que por fin te atrevas a dar el paso, no le vas a agradecer a los astros...
      </div>
      <div class="glass-card" style="border-left-color: #F472B6; background: rgba(0,0,0,0.45);">
        <div class="card-text-highlight" style="font-size: 38px; line-height: 1.36;">
          TE VAS A DECIR CON RABIA:<br>
          <span style="color: #2AD2C5;">«¿POR QUÉ CARAJOS REGALÉ TANTOS AÑOS DE MI VIDA ESPERANDO SEÑALES EN LUGAR DE DECIDIR?»</span>
        </div>
      </div>
    </div>
    <div class="sticker-free-zone"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 6: CIERRE & CTA -->
  <div class="slide" id="slide-6">
    <div class="slide-header">
      <div class="brand-logo"><span class="sparkle">✨</span> REALMENTE</div>
      <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    </div>
    <div class="text-top-container" style="align-items: center; text-align: center; margin-top: 60px;">
      <p style="font-size: 32px; color: #E2E8F0; line-height: 1.4; max-width: 860px;">
        La vida no se destraba pidiendo permiso afuera.<br>Se destraba cuando te paras firme adentro:
      </p>
      <div style="font-size: 52px; font-weight: 800; color: #2AD2C5; margin: 30px 0 35px; text-shadow: 0 4px 20px rgba(0,0,0,0.4);">
        «Ya está. Ya lo vi. Ya lo decidí.»
      </div>
      <div class="glass-card" style="border-left: 5px solid #2AD2C5; border-right: 5px solid #2AD2C5; width: 100%; max-width: 880px; padding: 28px 36px;">
        <div style="font-size: 22px; font-weight: 800; letter-spacing: 2px; color: #2AD2C5; text-transform: uppercase;">🎙️ EPISODIO 60 • REALMENTE PODCAST</div>
        <div style="font-size: 30px; font-weight: 700; color: #FFFFFF; margin-top: 10px;">La decisión que estás evadiendo es la puerta a tu siguiente nivel.</div>
      </div>
      <div style="background: linear-gradient(135deg, #2AD2C5 0%, #14B8A6 100%); color: #072B28; padding: 28px 56px; border-radius: 50px; font-size: 36px; font-weight: 800; letter-spacing: 0.5px; box-shadow: 0 20px 45px rgba(0,0,0,0.5); width: 100%; max-width: 840px; margin-top: 35px;">
        💬 Comenta la palabra <span style="text-decoration: underline;">DECISIÓN</span>
      </div>
      <p style="font-size: 26px; color: #D4B2E6; margin-top: 22px;">
        y te envío el episodio directo a tu DM 📩
      </p>
    </div>
    <div class="sticker-free-zone" style="min-height: 120px;"></div>
    <div class="slide-footer">
      <span>@marbelismontero</span>
      <span>RealMente Podcast</span>
    </div>
  </div>

</body>
</html>
"""

async def render():
    out_dir_brain = r"C:\Users\soyma\.gemini\antigravity\brain\41421e80-4487-4a8c-8b54-40c61767c134"
    out_dir_folder = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP60_Decision_y_Evasion\05_Redes_Reels_y_Carruseles"
    os.makedirs(out_dir_brain, exist_ok=True)
    os.makedirs(out_dir_folder, exist_ok=True)

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
            await page.wait_for_timeout(350)

            fn = f"slide_{i}_ep60_v2.png"
            file_brain = os.path.join(out_dir_brain, fn)
            await page.screenshot(path=file_brain, type="png")
            print(f"Rendered Slide {i} -> {file_brain}")

            file_folder = os.path.join(out_dir_folder, fn)
            shutil.copy(file_brain, file_folder)
            print(f"Copied Slide {i} -> {file_folder}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(render())
