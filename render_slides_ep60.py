import asyncio
from playwright.async_api import async_playwright
import os, shutil

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    html, body {
      margin: 0;
      padding: 0;
      width: 1080px;
      height: 1350px;
      overflow: hidden;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .slide-container {
      width: 1080px;
      height: 1350px;
      position: absolute;
      top: 0;
      left: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 85px 70px;
      box-sizing: border-box;
    }

    /* SLIDE 1: Fondo blanco limpio */
    #slide-1 {
      background-color: #FFFFFF;
      color: #190633;
      justify-content: center;
      align-items: center;
    }

    /* SLIDES 2 A 6: Fondos en colores simples y elegantes de la marca */
    #slide-2 { background: #0D3B38; color: #FFFFFF; } /* Turquesa oscuro marca */
    #slide-3 { background: #2E0C59; color: #FFFFFF; } /* Violeta Loto marca */
    #slide-4 { background: #12101F; color: #FFFFFF; } /* Negro Carbón */
    #slide-5 { background: #4A0E4E; color: #FFFFFF; } /* Morado Uva */
    #slide-6 { background: linear-gradient(135deg, #2E0C59 0%, #5416A0 100%); color: #FFFFFF; }

    /* Top Corner Header Badge */
    .corner-badge {
      position: absolute;
      top: 65px;
      right: 70px;
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(212, 178, 230, 0.3);
      padding: 12px 24px;
      border-radius: 30px;
      font-family: 'Jost', sans-serif;
      font-size: 20px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #D4B2E6;
    }

    .brand-logo {
      position: absolute;
      top: 65px;
      left: 70px;
      font-family: 'Jost', sans-serif;
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 2.5px;
      color: #2AD2C5;
      text-transform: uppercase;
    }

    .content-box {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      margin-top: 110px;
    }

    .title-large {
      font-family: 'Jost', sans-serif;
      font-size: 46px;
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 35px;
      color: #FFFFFF;
    }

    .highlight-card {
      background: rgba(0, 0, 0, 0.35);
      backdrop-filter: blur(10px);
      border-left: 6px solid #2AD2C5;
      border-radius: 20px;
      padding: 38px 42px;
      font-size: 38px;
      line-height: 1.4;
      font-weight: 600;
      color: #FFFFFF;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }

    /* Espacio reservado para sticker de humorista */
    .sticker-placeholder-area {
      height: 380px;
      margin-top: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px dashed rgba(255, 255, 255, 0.15);
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.03);
      color: rgba(255, 255, 255, 0.35);
      font-size: 22px;
      font-weight: 600;
      letter-spacing: 1px;
    }

    .footer-bar {
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 20px;
      color: rgba(255, 255, 255, 0.6);
      font-weight: 500;
    }
  </style>
</head>
<body>

  <!-- SLIDE 1 (Fondo Blanco Limpio Editorial) -->
  <div class="slide-container" id="slide-1">
    <div style="background: #F9F5FF; border: 3px solid #2E0C59; border-left: 10px solid #2AD2C5; border-radius: 24px; padding: 50px 45px; width: 100%; max-width: 940px; box-shadow: 0 20px 40px rgba(46, 12, 89, 0.15);">
      <p style="font-family: 'Jost', sans-serif; font-size: 48px; font-weight: 800; line-height: 1.35; color: #190633; margin-bottom: 25px;">
        El universo no te va a mandar <br>
        <span style="color: #0D9488; font-weight: 900;">un WhatsApp. 📱</span>
      </p>
      <p style="font-family: 'Jost', sans-serif; font-size: 38px; font-weight: 600; line-height: 1.4; color: #5416A0;">
        Y Mercurio retrógrado <strong>NO</strong> tiene la culpa de que te dé pavor tomar una decisión. ⚡🚪
      </p>
    </div>
    <div class="sticker-placeholder-area" style="width: 100%; max-width: 940px; border-color: rgba(46, 12, 89, 0.2); color: rgba(46, 12, 89, 0.4); background: rgba(46, 12, 89, 0.02);">
      [ 🎭 Espacio reservado para sticker de humorista / meme ]
    </div>
    <div class="footer-bar" style="width: 100%; max-width: 940px; border-top-color: rgba(46, 12, 89, 0.15); color: #5416A0;">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 2 (Fondo Turquesa Profundo Marca) -->
  <div class="slide-container" id="slide-2">
    <div class="brand-logo">✨ RealMente</div>
    <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    <div class="content-box">
      <div class="title-large" style="font-size: 54px; line-height: 1.25; margin-bottom: 30px;">
        No decidir <br>
        <span style="color: #2AD2C5;">ya es una decisión.</span>
      </div>
      <div class="highlight-card" style="border-left-color: #2AD2C5; background: rgba(0, 0, 0, 0.35);">
        Es la <strong>decisión cobarde</strong> de quedarte en el limbo esperando que la vida o alguien más elija por ti.
      </div>
      <div class="sticker-placeholder-area">
        [ 🎭 Espacio reservado para sticker de humorista / meme ]
      </div>
    </div>
    <div class="footer-bar">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 3 (Fondo Violeta Loto Marca) -->
  <div class="slide-container" id="slide-3">
    <div class="brand-logo">✨ RealMente</div>
    <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    <div class="content-box">
      <div class="title-large" style="font-size: 38px; line-height: 1.35; margin-bottom: 25px;">
        Lees el horóscopo, buscas señales, pides opiniones a medio mundo... con tal de no tener esa conversación incómoda.
      </div>
      <div class="highlight-card" style="border-left-color: #D4B2E6; background: rgba(0, 0, 0, 0.4);">
        <span style="color: #FFFFFF; font-weight: 800; font-size: 40px;">
          Eso no es paciencia: <br>
          <span style="color: #2AD2C5;">es cobardía con aroma a incienso. 🕯️</span>
        </span>
      </div>
      <div class="sticker-placeholder-area">
        [ 🎭 Espacio reservado para sticker de humorista / meme ]
      </div>
    </div>
    <div class="footer-bar">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 4 (Fondo Negro Carbón) -->
  <div class="slide-container" id="slide-4">
    <div class="brand-logo">✨ RealMente</div>
    <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    <div class="content-box">
      <div class="title-large" style="font-size: 36px; margin-bottom: 20px; color: #D4B2E6;">
        Mírate al espejo con total honestidad:
      </div>
      <div class="highlight-card" style="border-left-color: #2AD2C5; background: rgba(0, 0, 0, 0.5); padding: 35px;">
        <span style="color: #FFFFFF; font-size: 42px; font-weight: 800; line-height: 1.3;">
          ¿Cuántos años más de tu vida vas a tirar a la basura esperando una «señal divina»?
        </span>
      </div>
      <div style="font-size: 34px; font-weight: 700; color: #FB7185; margin-top: 25px; line-height: 1.35;">
        Mientras tú dudas, la vida se va. <br>
        Te estás haciendo vieja en la indecisión.
      </div>
      <div class="sticker-placeholder-area" style="height: 280px; margin-top: 25px;">
        [ 🎭 Espacio reservado para sticker de humorista / meme ]
      </div>
    </div>
    <div class="footer-bar">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 5 (Fondo Morado Uva) -->
  <div class="slide-container" id="slide-5">
    <div class="brand-logo">✨ RealMente</div>
    <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    <div class="content-box">
      <div class="title-large" style="font-size: 38px; margin-bottom: 25px;">
        ¿Sabes qué es lo que más te va a doler?
      </div>
      <div class="highlight-card" style="border-left-color: #2AD2C5; background: rgba(0, 0, 0, 0.45); padding: 40px;">
        <p style="font-size: 30px; color: #D4B2E6; margin: 0 0 15px 0;">El día que por fin te atrevas a dar el paso te vas a decir con rabia:</p>
        <span style="color: #FFFFFF; font-size: 40px; font-weight: 800; line-height: 1.35;">
          «¿Por qué carajos regalé tantos años de mi vida esperando señales en lugar de decidir?»
        </span>
      </div>
      <div class="sticker-placeholder-area">
        [ 🎭 Espacio reservado para sticker de humorista / meme ]
      </div>
    </div>
    <div class="footer-bar">
      <span>@marbelismontero</span>
      <span>Desliza ➡️</span>
    </div>
  </div>

  <!-- SLIDE 6 (Fondo Gradiente Violeta Cierre + CTA) -->
  <div class="slide-container" id="slide-6">
    <div class="brand-logo">✨ RealMente</div>
    <div class="corner-badge">📌 Ep. 60 • Podcast</div>
    <div class="content-box" style="justify-content: center; align-items: center; text-align: center;">
      <p style="font-size: 32px; color: #D4B2E6; line-height: 1.4; margin-bottom: 25px; max-width: 900px;">
        La vida no se destraba pidiendo permiso afuera. <br>Se destraba cuando te paras firme adentro:
      </p>
      <div style="font-family: 'Jost', sans-serif; font-size: 52px; font-weight: 800; color: #2AD2C5; margin-bottom: 40px; text-shadow: 0 5px 20px rgba(0,0,0,0.4);">
        «Ya está. Ya lo vi. Ya lo decidí.»
      </div>
      <div style="background: rgba(0, 0, 0, 0.35); border: 2px solid #2AD2C5; border-radius: 24px; padding: 30px 40px; margin-bottom: 35px; width: 100%; max-width: 880px;">
        <div style="font-size: 24px; font-weight: 800; letter-spacing: 2px; color: #2AD2C5; text-transform: uppercase;">🎙️ EPISODIO 60 • REALMENTE PODCAST</div>
        <div style="font-size: 32px; font-weight: 700; color: #FFFFFF; margin-top: 10px;">La decisión que estás evadiendo es la puerta a tu siguiente nivel.</div>
      </div>
      <div style="background: linear-gradient(135deg, #2AD2C5 0%, #14B8A6 100%); color: #072B28; padding: 30px 60px; border-radius: 50px; font-family: 'Jost', sans-serif; font-size: 38px; font-weight: 800; letter-spacing: 1px; box-shadow: 0 20px 45px rgba(0,0,0,0.5); width: 100%; max-width: 850px;">
        💬 Comenta la palabra <span style="text-decoration: underline;">DECISIÓN</span>
      </div>
      <p style="font-size: 28px; color: #E0E7FF; margin-top: 25px;">
        y te envío el episodio directo a tu DM 📩
      </p>
    </div>
    <div class="footer-bar">
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
              .slide-container {{ display: none !important; }}
              #slide-{i} {{ display: flex !important; }}
            </style>
            """
            full_html = HTML_CONTENT.replace('</head>', f'{css_override}</head>')
            
            await page.set_content(full_html)
            await page.wait_for_timeout(350)
            
            fn = f"slide_{i}_ep60.png"
            file_brain = os.path.join(out_dir_brain, fn)
            await page.screenshot(path=file_brain, type="png")
            print(f"Rendered Slide {i} -> {file_brain}")
            
            # Copy to official folder
            file_folder = os.path.join(out_dir_folder, fn)
            shutil.copy(file_brain, file_folder)
            print(f"Copied Slide {i} -> {file_folder}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(render())
