import base64
import os

brain_dir = r"C:\Users\soyma\.gemini\antigravity\brain\adf591c1-934b-4f97-bbfb-e3eebc5fe0a5"
target_html = os.path.join(brain_dir, "carrete_inline_widget.html")

b64_imgs = []
for i in range(1, 7):
    p = os.path.join(brain_dir, f"slide_{i}_ep62_small.png")
    with open(p, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
        b64_imgs.append(f"data:image/png;base64,{b64}")

html_code = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      background: transparent;
      margin: 0;
      padding: 6px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    .slide-frame {{
      aspect-ratio: 4 / 5;
      max-height: 400px;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
      border: 1px solid rgba(255,255,255,0.15);
      background: #0a0410;
      position: relative;
    }}
    .slide-frame img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #0a0410;
    }}
    .tab-btn {{
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
      border: 1px solid rgba(255,255,255,0.1);
      background: rgba(255,255,255,0.05);
      color: #cbd5e1;
    }}
    .tab-btn:hover {{
      background: rgba(42, 210, 197, 0.2);
      border-color: #2ad2c5;
      color: #2ad2c5;
    }}
    .tab-btn.active {{
      background: #2ad2c5;
      color: #072b28;
      border-color: #2ad2c5;
      box-shadow: 0 0 10px rgba(42,210,197,0.4);
    }}
  </style>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased">
  <div class="bg-[var(--card,#150a21)] text-[var(--foreground,#f5f3ff)] border border-[var(--border,rgba(192,132,252,0.3))] rounded-2xl p-3 shadow-xl max-w-2xl mx-auto">
    
    <!-- Header Controls -->
    <div class="flex items-center justify-between pb-2 mb-2 border-b border-white/10 flex-wrap gap-2">
      <div class="flex items-center gap-2">
        <span class="bg-[#2ad2c5]/20 text-[#2ad2c5] border border-[#2ad2c5]/40 text-[10px] font-black px-2 py-0.5 rounded-full uppercase tracking-wider">
          Ep. 62
        </span>
        <span class="text-xs font-bold text-white" id="slideLabel">Slide 1 de 6: Portada / Gancho</span>
      </div>
      <div class="flex items-center gap-1">
        <button onclick="copyCurrentText()" class="text-[11px] bg-white/10 hover:bg-white/20 text-white font-medium px-2 py-1 rounded border border-white/20 transition">
          📋 Copiar Slide
        </button>
        <button onclick="copyCaption()" class="text-[11px] bg-[#2ad2c5] hover:bg-[#14b8a6] text-[#072b28] font-bold px-2 py-1 rounded transition">
          🚀 Copiar Caption
        </button>
      </div>
    </div>

    <!-- Tabs for 6 Slides -->
    <div class="grid grid-cols-6 gap-1 mb-2">
      <button class="tab-btn active" onclick="setSlide(0)" id="tab-0">#1 Gancho</button>
      <button class="tab-btn" onclick="setSlide(1)" id="tab-1">#2 Origen</button>
      <button class="tab-btn" onclick="setSlide(2)" id="tab-2">#3 4 Patas</button>
      <button class="tab-btn" onclick="setSlide(3)" id="tab-3">#4 Neutro</button>
      <button class="tab-btn" onclick="setSlide(4)" id="tab-4">#5 Realidad</button>
      <button class="tab-btn" onclick="setSlide(5)" id="tab-5">#6 Techo</button>
    </div>

    <!-- Slide Visual Display -->
    <div class="flex flex-col sm:flex-row items-center gap-3">
      <!-- Image Preview -->
      <div class="slide-frame shrink-0 w-[240px] mx-auto">
        <img id="activeImg" src="{b64_imgs[0]}" alt="Slide Actual">
      </div>

      <!-- Slide Details -->
      <div class="flex-1 w-full flex flex-col justify-between self-stretch bg-black/30 border border-white/10 rounded-xl p-3 text-xs">
        <div>
          <div class="text-[10px] font-bold uppercase tracking-wider text-[#c084fc] mb-1" id="slideBadge">Berenjena Profundo (#12091C)</div>
          <h3 class="text-sm font-bold text-white mb-2 leading-tight" id="slideTitle">
            No estás siendo «prudente»... le tienes terror a que te llamen egoísta. 🚪⚡
          </h3>
          <div class="bg-white/5 border-l-2 border-[#2ad2c5] p-2 rounded text-[11px] text-slate-200 mb-2 leading-relaxed" id="slideCard">
            En el segundo exacto en que vas a poner un límite o cobrar lo que vales, tu mente suelta a la culpa como perro guardián.
          </div>
          <div class="text-[11px] italic text-[#c084fc] font-medium" id="slideNote">
            La culpa no te avisa que estás haciendo daño: te avisa que estás a punto de salir de la jaula. ✨
          </div>
        </div>

        <div class="mt-3 pt-2 border-t border-white/10 flex items-center justify-between">
          <button onclick="prevSlide()" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded font-bold text-[11px]">◀ Anterior</button>
          <span class="text-[10px] text-teal-300 font-bold">50% Inferior Libre ✅</span>
          <button onclick="nextSlide()" class="px-3 py-1 bg-white/10 hover:bg-white/20 text-white rounded font-bold text-[11px]">Siguiente ▶</button>
        </div>
      </div>
    </div>

  </div>

  <script>
    const images = {b64_imgs};
    const slides = [
      {{
        num: 1,
        label: "Slide 1 de 6: Portada / Gancho",
        badge: "Berenjena Profundo (#12091C) • 50% Inferior Libre",
        title: "No estás siendo «prudente»... le tienes terror a que te llamen egoísta. 🚪⚡",
        card: "En el segundo exacto en que vas a poner un límite o cobrar lo que vales, tu mente suelta a la culpa como perro guardián.",
        note: "La culpa no te avisa que estás haciendo daño: te avisa que estás a punto de salir de la jaula. ✨",
        text: "✨ REALMENTE | 📌 Ep. 62 • Podcast\\n\\nNo estás siendo «prudente»... le tienes terror a que te llamen egoísta. 🚪⚡\\n\\nEn el segundo exacto en que vas a poner un límite o cobrar lo que vales, tu mente suelta a la culpa como perro guardián.\\n\\nLa culpa no te avisa que estás haciendo daño: te avisa que estás a punto de salir de la jaula. ✨\\n\\n@marbelismontero | Desliza ➡️"
      }},
      {{
        num: 2,
        label: "Slide 2 de 6: El Diagnóstico Social",
        badge: "Petróleo / Turquesa Oscuro (#0D3B38) • 50% Inferior Libre",
        title: "Tú no naciste con culpa: te la programaron para hacerte predecible. 🏛️",
        card: "Durante siglos se implantó el «deber ser» como alarma interna para mantenerte dócil sin necesidad de ponerte un policía las 24 horas. Romper el molde no es cometer un delito: es desafiar las normas que otros crearon para controlarte.",
        note: "⚠️ Cada vez que te achicas para encajar, compras paz ajena con tu propia frustración.",
        text: "✨ REALMENTE | 📌 Ep. 62 • Podcast\\n\\nTú no naciste con culpa: te la programaron para hacerte predecible. 🏛️\\n\\nDurante siglos se implantó el «deber ser» como alarma interna para mantenerte dócil sin necesidad de ponerte un policía las 24 horas. Romper el molde no es cometer un delito: es desafiar las normas que otros crearon para controlarte.\\n\\n⚠️ Cada vez que te achicas para encajar, compras paz ajena con tu propia frustración.\\n\\n@marbelismontero | Desliza ➡️"
      }},
      {{
        num: 3,
        label: "Slide 3 de 6: Desmontar la Máscara",
        badge: "Violeta Loto (#2E0C59) • 50% Inferior Libre",
        title: "El juego perverso de la culpa: la mesa en la que vives atrapada. 🪑",
        card: "Toda tu vida te la pasas rotando entre 4 esquinas:\\n• Lo Bueno vs. Lo Malo: juicios morales rígidos.\\n• Víctima vs. Victimaria: si dices no, te crees mala; si toleras todo, te refugias como la mártir abnegada.",
        note: "💡 La culpa solo existe si previamente etiquetaste tu bienestar como algo «inaceptable».",
        text: "✨ REALMENTE | 📌 Ep. 62 • Podcast\\n\\nEl juego perverso de la culpa: la mesa en la que vives atrapada. 🪑\\n\\nToda tu vida te la pasas rotando entre 4 esquinas:\\n• Lo Bueno vs. Lo Malo: juicios morales rígidos.\\n• Víctima vs. Victimaria: si dices no, te crees mala; si toleras todo, te refugias como la mártir abnegada.\\n\\n💡 La culpa solo existe si previamente etiquetaste tu bienestar como algo «inaceptable».\\n\\n@marbelismontero | Desliza ➡️"
      }},
      {{
        num: 4,
        label: "Slide 4 de 6: Quiebre en PNL (Hechos Neutros)",
        badge: "Negro Carbón / Índigo (#12101F) • 50% Inferior Libre",
        title: "Axioma liberador de PNL: Los hechos son neutros. El drama lo inventa tu cabeza. 🧠",
        card: "Decir «no puedo hoy» es un hecho neutro. El reproche moral es el invento de tu diálogo interno. Si alguien se molesta por tu límite, solo demuestra que su expectativa sobre ti se rompió.",
        note: "👀 Su enojo es su proceso: jamás tu condena.",
        text: "✨ REALMENTE | 📌 Ep. 62 • Podcast\\n\\nAxioma liberador de PNL: Los hechos son neutros. El drama lo inventa tu cabeza. 🧠\\n\\nDecir «no puedo hoy» es un hecho neutro. El reproche moral es el invento de tu diálogo interno. Si alguien se molesta por tu límite, solo demuestra que su expectativa sobre ti se rompió.\\n\\n👀 Su enojo es su proceso: jamás tu condena.\\n\\n@marbelismontero | Desliza ➡️"
      }},
      {{
        num: 5,
        label: "Slide 5 de 6: Golpe de Realidad",
        badge: "Ciruela / Uva Profundo (#4A0E4E) • 50% Inferior Libre",
        title: "¿Por qué carajos compras paz ajena con tu propia frustración? ⏱️",
        card: "El precio de tu nueva identidad no es el dinero ni reventarte trabajando. El verdadero peaje es aprender a sostener la incomodidad transitoria de que tu entorno se desacomode cuando creces.",
        note: "🔥 Preferir ser «la niña buena que se sacrifica» es la trampa más cara de tu vida.",
        text: "✨ REALMENTE | 📌 Ep. 62 • Podcast\\n\\n¿Por qué carajos compras paz ajena con tu propia frustración? ⏱️\\n\\nEl precio de tu nueva identidad no es el dinero ni reventarte trabajando. El verdadero peaje es aprender a sostener la incomodidad transitoria de que tu entorno se desacomode cuando creces.\\n\\n🔥 Preferir ser «la niña buena que se sacrifica» es la trampa más cara de tu vida.\\n\\n@marbelismontero | Desliza ➡️"
      }},
      {{
        num: 6,
        label: "Slide 6 de 6: Romper el Techo y CTA",
        badge: "Gradiente Violeta Cierre • Revelación de Identidad",
        title: "La culpa es el indicador de que estás rompiendo tu techo. 🚀",
        card: "Si nunca sientes culpa, estás en piloto automático repitiendo lo conocido. La punzada no te frena: te avisa que tu identidad pasó de nivel.\\n\\n«No compro paz ajena con mi frustración. Sostengo la incomodidad de serle fiel a mí misma.»",
        note: "🎙️ REALMENTE PODCAST • REALMENTE CLUB — Comenta PODCAST y te envío el episodio al DM 📩",
        text: "✨ REALMENTE | 📌 Ep. 62 • Podcast\\nREVELACIÓN DE IDENTIDAD\\n\\nLa culpa es el indicador de que estás rompiendo tu techo. 🚀\\n\\nSi nunca sientes culpa, estás en piloto automático repitiendo lo conocido. La punzada no te frena: te avisa que tu identidad pasó de nivel.\\n\\n«No compro paz ajena con mi frustración. Sostengo la incomodidad de serle fiel a mí misma.»\\n\\n🎙️ REALMENTE PODCAST • REALMENTE CLUB\\nEpisodio 62: La trampa de la culpa y el precio de tu nueva identidad\\n\\n💬 Comenta la palabra PODCAST y te envío el episodio directo a tu DM 📩\\n\\n@marbelismontero | RealMente Club"
      }}
    ];

    let current = 0;

    function update() {{
      const s = slides[current];
      document.getElementById('activeImg').src = images[current];
      document.getElementById('slideLabel').innerText = s.label;
      document.getElementById('slideBadge').innerText = s.badge;
      document.getElementById('slideTitle').innerText = s.title;
      document.getElementById('slideCard').innerText = s.card;
      document.getElementById('slideNote').innerText = s.note;

      for (let i = 0; i < 6; i++) {{
        const btn = document.getElementById(`tab-${{i}}`);
        if (i === current) {{
          btn.className = "tab-btn active";
        }} else {{
          btn.className = "tab-btn";
        }}
      }}
    }}

    function setSlide(i) {{
      current = i;
      update();
    }}

    function prevSlide() {{
      current = (current - 1 + 6) % 6;
      update();
    }}

    function nextSlide() {{
      current = (current + 1) % 6;
      update();
    }}

    function copyCurrentText() {{
      navigator.clipboard.writeText(slides[current].text).then(() => {{
        alert("¡Texto del Slide " + (current+1) + " copiado!");
      }});
    }}

      const caption = `¿Cuántas veces has dicho «sí, tranquila, cuenta conmigo» teniendo ganas de gritar que NO, solo para que nadie piense que cambiaste o que te volviste egoísta? 🚪⚡\\n\\nTe pasa cuando vas a cobrar lo que vale tu trabajo, cuando cancelas un compromiso para descansar o cuando pones un límite firme: en ese segundo exacto se te cierra el estómago y aparece una voz pesada que te hace retroceder.\\n\\nPero detente: esa punzada no te está avisando que estás haciendo daño. Te avisa que estás rompiendo las expectativas ajenas para por fin empezar a respetarte a ti misma.\\n\\nSentir culpa no es un fallo tuyo: es el peaje transitorio de convertirte en la mujer que de verdad quieres ser.\\n\\nEn el nuevo Episodio 62 de RealMente Podcast nos metemos de lleno en lo que nadie te cuenta sobre crecer: por qué para asumir tu nueva identidad primero tienes que aprender a sostener la incomodidad de no complacer al mundo.\\n\\nDesliza el carrusel completo para integrar las claves de esta semana. 🎠\\n\\n🎙️ Episodio 62 ya disponible en Spotify y YouTube.\\n\\n💬 Comenta la palabra PODCAST aquí abajo y te envío el episodio completo directo a tu DM 📩\\n\\n¡Cero excusas!\\n\\n#RealMentePodcast #MarbelisMontero #CulpaInconsciente #RealMenteClub #PNL`;
      navigator.clipboard.writeText(caption).then(() => {{
        alert("¡Caption copiado!");
      }});
    }}
  </script>
</body>
</html>
"""

with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated updated carrete_inline_widget.html successfully!")
