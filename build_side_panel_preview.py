import base64
import os

brain_dir = r"C:\Users\soyma\.gemini\antigravity\brain\adf591c1-934b-4f97-bbfb-e3eebc5fe0a5"
target_html = os.path.join(brain_dir, "carrete_preview.html")

b64_imgs = []
for i in range(1, 7):
    img_path = os.path.join(brain_dir, f"slide_{i}_ep62.png")
    with open(img_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        b64_imgs.append(f"data:image/png;base64,{b64}")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Revisión Carrete 6 Slides — Ep 62 | RealMente</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    body {{
      background: #08030e;
      color: #f5f3ff;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 16px;
    }}
    .slide-thumb {{
      cursor: pointer;
      border: 2px solid rgba(192, 132, 252, 0.25);
      border-radius: 12px;
      overflow: hidden;
      transition: all 0.2s ease;
      aspect-ratio: 4 / 5;
      background: #140924;
    }}
    .slide-thumb:hover, .slide-thumb.active {{
      border-color: #2ad2c5;
      box-shadow: 0 0 15px rgba(42, 210, 197, 0.4);
      transform: translateY(-2px);
    }}
    .preview-card {{
      max-width: 460px;
      width: 100%;
      aspect-ratio: 4 / 5;
      border-radius: 20px;
      overflow: hidden;
      border: 1.5px solid rgba(192, 132, 252, 0.3);
      box-shadow: 0 20px 45px rgba(0,0,0,0.8), 0 0 35px rgba(42, 210, 197, 0.25);
      background: #12091c;
    }}
    .preview-card img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
  </style>
</head>
<body class="p-4 flex flex-col items-center">
  <div class="max-w-4xl w-full">
    <!-- Header -->
    <div class="flex items-center justify-between bg-white/5 border border-white/10 rounded-2xl p-4 mb-6 backdrop-blur">
      <div class="flex items-center gap-3">
        <span class="bg-teal-500/20 text-teal-300 border border-teal-500/40 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">
          Episodio 62 • Podcast
        </span>
        <h1 class="text-base font-bold text-white">Carrete 6 Slides — Revisión de Diseño</h1>
      </div>
      <div class="text-xs text-purple-300/80 font-medium bg-purple-950/50 border border-purple-500/30 px-3 py-1 rounded-full">
        👑 50% Inferior Libre
      </div>
    </div>

    <!-- Main Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
      <!-- Columna Izquierda: Vista Previa Grande -->
      <div class="flex flex-col items-center">
        <div class="preview-card" id="cardViewport">
          <img id="mainImg" src="{b64_imgs[0]}" alt="Slide Actual">
        </div>
        <div class="flex items-center justify-between w-full max-w-[460px] mt-4 px-2">
          <button onclick="prevSlide()" class="px-4 py-2 rounded-xl bg-white/10 hover:bg-teal-500/20 border border-white/20 hover:border-teal-400 text-sm font-semibold text-white transition">
            ◀ Anterior
          </button>
          <span id="slideCounter" class="text-sm font-bold text-teal-300">Slide 1 de 6</span>
          <button onclick="nextSlide()" class="px-4 py-2 rounded-xl bg-white/10 hover:bg-teal-500/20 border border-white/20 hover:border-teal-400 text-sm font-semibold text-white transition">
            Siguiente ▶
          </button>
        </div>
      </div>

      <!-- Columna Derecha: Selector de Slides y Detalles -->
      <div class="flex flex-col gap-4">
        <div class="bg-white/5 border border-white/10 rounded-2xl p-4">
          <h2 class="text-sm font-bold text-teal-300 mb-3 uppercase tracking-wider">Seleccionar Lámina</h2>
          <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
            <div class="slide-thumb active" onclick="setSlide(0)" id="thumb-0">
              <img src="{b64_imgs[0]}" class="w-full h-full object-cover">
            </div>
            <div class="slide-thumb" onclick="setSlide(1)" id="thumb-1">
              <img src="{b64_imgs[1]}" class="w-full h-full object-cover">
            </div>
            <div class="slide-thumb" onclick="setSlide(2)" id="thumb-2">
              <img src="{b64_imgs[2]}" class="w-full h-full object-cover">
            </div>
            <div class="slide-thumb" onclick="setSlide(3)" id="thumb-3">
              <img src="{b64_imgs[3]}" class="w-full h-full object-cover">
            </div>
            <div class="slide-thumb" onclick="setSlide(4)" id="thumb-4">
              <img src="{b64_imgs[4]}" class="w-full h-full object-cover">
            </div>
            <div class="slide-thumb" onclick="setSlide(5)" id="thumb-5">
              <img src="{b64_imgs[5]}" class="w-full h-full object-cover">
            </div>
          </div>
        </div>

        <div class="bg-white/5 border border-white/10 rounded-2xl p-4">
          <h2 class="text-sm font-bold text-purple-300 mb-2 uppercase tracking-wider" id="slideName">Slide 1 — Portada / Gancho Disruptivo</h2>
          <p class="text-xs text-slate-300 leading-relaxed" id="slideDesc">
            Titular: «No estás siendo prudente... le tienes terror a que te llamen egoísta». Concentrado en los primeros 600px con la mitad inferior 100% limpia para foto de Marbelis.
          </p>
        </div>

        <div class="bg-white/5 border border-white/10 rounded-2xl p-4">
          <h2 class="text-sm font-bold text-teal-300 mb-2 uppercase tracking-wider">📁 Ubicaciones de Almacenamiento</h2>
          <div class="text-xs text-slate-300 space-y-2">
            <p><strong class="text-white">Google Drive:</strong><br><code class="text-teal-300 bg-black/40 px-2 py-1 rounded block mt-1 select-all">G:\\Mi unidad\\MARCA\\03_Contenido_Redes\\Carruseles\\C018_La_Trampa_de_la_Culpa_Ep62\\</code></p>
            <p><strong class="text-white">Local:</strong><br><code class="text-purple-300 bg-black/40 px-2 py-1 rounded block mt-1 select-all">c:\\Users\\soyma\\OneDrive\\Documents\\ANTIGRAVITY\\MARCA\\Episodios\\EP62_La_Trampa_de_la_Culpa\\05_Redes_Reels_y_Carruseles\\</code></p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    const images = {b64_imgs};
    const info = [
      {{ title: "Slide 1 — Gancho Disruptivo", desc: "No estás siendo «prudente»... le tienes terror a que te llamen egoísta. Fondo Berenjena Profundo (#12091C). 50% inferior despejado para foto de Marbelis." }},
      {{ title: "Slide 2 — Diagnóstico Social", desc: "Tú no naciste con culpa: te la programaron para hacerte predecible. Fondo Petróleo / Turquesa (#0D3B38). Desmonta el 'deber ser'." }},
      {{ title: "Slide 3 — Desmontar la Máscara", desc: "La mesa de 4 patas: Bueno vs Malo / Víctima vs Victimaria. Fondo Violeta Loto (#2E0C59)." }},
      {{ title: "Slide 4 — Axioma de PNL", desc: "Los hechos son neutros. El drama lo inventa tu cabeza. Fondo Negro Carbón (#12101F). Su enojo es su expectativa rota, no tu condena." }},
      {{ title: "Slide 5 — Golpe de Realidad", desc: "¿Por qué carajos compras paz ajena con tu propia frustración? Fondo Ciruela Profundo (#4A0E4E)." }},
      {{ title: "Slide 6 — Romper el Techo y CTA", desc: "La culpa es el indicador de que estás rompiendo tu techo. Fondo Gradiente Violeta Cierre. Mantra + Invitación al Episodio 62 + Palabra clave CULPA." }}
    ];

    let current = 0;

    function update() {{
      document.getElementById('mainImg').src = images[current];
      document.getElementById('slideCounter').innerText = `Slide ${{current + 1}} de ${{images.length}}`;
      document.getElementById('slideName').innerText = info[current].title;
      document.getElementById('slideDesc').innerText = info[current].desc;

      for (let i = 0; i < images.length; i++) {{
        const el = document.getElementById(`thumb-${{i}}`);
        if (el) {{
          if (i === current) {{
            el.classList.add('active');
          }} else {{
            el.classList.remove('active');
          }}
        }}
      }}
    }}

    function setSlide(i) {{
      current = i;
      update();
    }}

    function prevSlide() {{
      current = (current - 1 + images.length) % images.length;
      update();
    }}

    function nextSlide() {{
      current = (current + 1) % images.length;
      update();
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowLeft') prevSlide();
      if (e.key === 'ArrowRight') nextSlide();
    }});
  </script>
</body>
</html>
"""

with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated self-contained base64 HTML artifact: {target_html}")
