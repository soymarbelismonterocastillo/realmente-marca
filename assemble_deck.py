import base64

# Read base64 image
with open(r'c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\mesa_metafora_culpa.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')
data_uri = f'data:image/png;base64,{b64}'

html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Episodio 62 - La trampa de la culpa y el precio invisible de asumir esta nueva identidad | RealMente Club</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      /* PALETA DE MARCA REALMENTE OFICIAL: Morado Oscuro Berenjena + Turquesa + Lila Claro */
      --bg-gradient: linear-gradient(135deg, #12091c 0%, #1e0d32 50%, #140824 100%);
      --card-bg: rgba(30, 15, 48, 0.88);
      --card-border: rgba(192, 132, 252, 0.38);
      --text-main: #f5f3ff;
      --text-muted: #c084fc;
      --accent-turquoise: #00f2fe;
      --accent-turquoise-glow: rgba(0, 242, 254, 0.28);
      --accent-lilac: #d8b4fe;
      --accent-lilac-glow: rgba(216, 180, 254, 0.28);
      --badge-bg: rgba(0, 242, 254, 0.14);
      --badge-border: rgba(0, 242, 254, 0.45);
      --highlight-bg: linear-gradient(135deg, rgba(216, 180, 254, 0.14), rgba(0, 242, 254, 0.14));
      --shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.75);
    }}

    [data-theme="light"] {{
      --bg-gradient: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 50%, #e9d5ff 100%);
      --card-bg: rgba(255, 255, 255, 0.95);
      --card-border: rgba(168, 85, 247, 0.35);
      --text-main: #2e1065;
      --text-muted: #7e22ce;
      --accent-turquoise: #0891b2;
      --accent-turquoise-glow: rgba(8, 145, 178, 0.2);
      --accent-lilac: #9333ea;
      --accent-lilac-glow: rgba(147, 51, 234, 0.18);
      --badge-bg: rgba(8, 145, 178, 0.1);
      --badge-border: rgba(8, 145, 178, 0.35);
      --highlight-bg: linear-gradient(135deg, rgba(243, 232, 255, 0.95), rgba(233, 213, 255, 0.95));
      --shadow: 0 20px 45px -10px rgba(76, 29, 149, 0.18);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Outfit', 'Montserrat', sans-serif;
      background: #09030f;
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 20px;
      overflow-x: hidden;
      transition: background 0.3s ease;
    }}

    /* Top Controls Bar */
    .controls-bar {{
      display: flex;
      gap: 15px;
      margin-bottom: 18px;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(14px);
      padding: 10px 24px;
      border-radius: 50px;
      border: 1px solid rgba(255, 255, 255, 0.14);
      z-index: 100;
    }}

    .btn {{
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 9px 20px;
      border-radius: 20px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
    }}

    .btn:hover {{
      background: var(--accent-turquoise);
      color: #09030f;
      border-color: var(--accent-turquoise);
      transform: translateY(-2px);
      box-shadow: 0 4px 15px var(--accent-turquoise-glow);
    }}

    .slide-counter-badge {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-turquoise);
      padding: 5px 16px;
      background: rgba(0, 242, 254, 0.15);
      border-radius: 14px;
      border: 1px solid rgba(0, 242, 254, 0.35);
    }}

    /* Presentation Deck Viewport (16:9) */
    .deck-viewport {{
      width: 100%;
      max-width: 1040px;
      aspect-ratio: 16 / 9;
      background: var(--bg-gradient);
      border-radius: 24px;
      box-shadow: var(--shadow);
      border: 1.5px solid var(--card-border);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      transition: all 0.4s ease;
    }}

    /* Glowing decorative backgrounds */
    .glow-circle-1 {{
      position: absolute;
      top: -120px;
      right: -120px;
      width: 420px;
      height: 420px;
      background: radial-gradient(circle, var(--accent-turquoise-glow) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }}

    .glow-circle-2 {{
      position: absolute;
      bottom: -140px;
      left: -140px;
      width: 440px;
      height: 440px;
      background: radial-gradient(circle, var(--accent-lilac-glow) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }}

    /* Individual Slide Container */
    .slide {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 30px 45px 44px 45px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.96) translateY(10px);
      transition: all 0.45s cubic-bezier(0.4, 0, 0.2, 1);
      box-sizing: border-box;
      z-index: 1;
    }}

    .slide.active {{
      opacity: 1;
      visibility: visible;
      transform: scale(1) translateY(0);
      z-index: 10;
    }}

    /* Header Badges & Titles */
    .tag-header {{
      display: inline-block;
      background: var(--badge-bg);
      border: 1px solid var(--badge-border);
      color: var(--accent-turquoise);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 2.2px;
      text-transform: uppercase;
      padding: 5px 18px;
      border-radius: 50px;
      margin-bottom: 10px;
    }}

    .slide-title {{
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 2.25rem;
      font-weight: 700;
      line-height: 1.25;
      color: var(--accent-turquoise);
      margin-bottom: 12px;
      max-width: 900px;
    }}

    .slide-subtitle {{
      font-size: 1.25rem;
      color: var(--accent-lilac);
      font-weight: 500;
      max-width: 780px;
      margin-bottom: 18px;
      line-height: 1.5;
    }}

    /* Quote Box */
    .quote-box {{
      background: var(--card-bg);
      backdrop-filter: blur(14px);
      border-left: 6px solid var(--accent-turquoise);
      border-top: 1px solid var(--card-border);
      border-right: 1px solid var(--card-border);
      border-bottom: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 42px 50px;
      max-width: 860px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    }}

    .quote-text {{
      font-family: 'Playfair Display', serif;
      font-size: 1.95rem;
      font-style: italic;
      line-height: 1.45;
      color: var(--text-main);
      margin-bottom: 18px;
    }}

    .quote-author {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--accent-turquoise);
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}

    /* Minimalist Box (Slide 6 - Ejercicio Práctico) */
    .minimal-box {{
      background: var(--highlight-bg);
      border: 2.5px dashed var(--accent-turquoise);
      border-radius: 24px;
      padding: 70px 60px;
      max-width: 840px;
      width: 100%;
      box-shadow: 0 20px 50px rgba(0, 242, 254, 0.18);
      text-align: center;
    }}

    .minimal-title {{
      font-family: 'Playfair Display', serif;
      font-size: 3.8rem;
      color: var(--accent-turquoise);
      font-weight: 700;
      line-height: 1.2;
      letter-spacing: 0.5px;
    }}

    /* Table Graphic Container (Slide 3) */
    .table-graphic-box {{
      width: 100%;
      max-width: 780px;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.6);
      border: 1.5px solid var(--card-border);
      background: #12091c;
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .table-graphic-box img {{
      width: 100%;
      height: auto;
      max-height: 350px;
      display: block;
      object-fit: contain;
    }}

    /* Grid for the 4 Legs Explanation (Slide 4) */
    .table-structure {{
      width: 100%;
      max-width: 900px;
      margin-top: 6px;
    }}

    .table-top-bar {{
      background: linear-gradient(90deg, rgba(216, 180, 254, 0.25), rgba(0, 242, 254, 0.25));
      border: 1.5px solid var(--accent-turquoise);
      border-radius: 14px;
      padding: 10px 20px;
      text-align: center;
      font-family: 'Playfair Display', serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 12px;
      box-shadow: 0 4px 15px rgba(0, 242, 254, 0.15);
    }}

    .legs-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      width: 100%;
    }}

    .leg-card {{
      background: var(--card-bg);
      border-radius: 14px;
      padding: 14px 12px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
      box-shadow: 0 8px 20px rgba(0,0,0,0.3);
      position: relative;
    }}

    .leg-card.leg-1 {{
      border: 1.5px solid rgba(0, 242, 254, 0.45);
      border-top: 4px solid var(--accent-turquoise);
    }}
    .leg-card.leg-2 {{
      border: 1.5px solid rgba(244, 63, 94, 0.45);
      border-top: 4px solid #f43f5e;
    }}
    .leg-card.leg-3 {{
      border: 1.5px solid rgba(216, 180, 254, 0.45);
      border-top: 4px solid var(--accent-lilac);
    }}
    .leg-card.leg-4 {{
      border: 1.5px solid rgba(251, 146, 60, 0.45);
      border-top: 4px solid #fb923c;
    }}

    .leg-badge {{
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      padding: 3px 10px;
      border-radius: 20px;
      margin-bottom: 6px;
    }}
    .leg-1 .leg-badge {{ background: rgba(0, 242, 254, 0.18); color: var(--accent-turquoise); }}
    .leg-2 .leg-badge {{ background: rgba(244, 63, 94, 0.18); color: #fb7185; }}
    .leg-3 .leg-badge {{ background: rgba(216, 180, 254, 0.18); color: var(--accent-lilac); }}
    .leg-4 .leg-badge {{ background: rgba(251, 146, 60, 0.18); color: #fdba74; }}

    .leg-title {{
      font-family: 'Playfair Display', serif;
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 6px;
    }}

    .leg-desc {{
      font-size: 1.05rem;
      line-height: 1.42;
      color: #e2e8f0;
    }}

    .table-footer-anchor {{
      margin-top: 14px;
      font-size: 1.15rem;
      color: var(--accent-lilac);
      font-style: italic;
      text-align: center;
      font-weight: 500;
    }}

    /* Results Grid (Slide 5) */
    .levels-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      width: 100%;
      max-width: 900px;
      text-align: left;
    }}

    .level-card {{
      background: var(--card-bg);
      border-radius: 12px;
      padding: 12px 18px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    }}

    .level-card.lvl-red {{
      border: 1px solid rgba(244, 63, 94, 0.45);
      border-left: 5px solid #f43f5e;
    }}
    .level-card.lvl-orange {{
      border: 1px solid rgba(251, 146, 60, 0.45);
      border-left: 5px solid #fb923c;
    }}
    .level-card.lvl-yellow {{
      border: 1px solid rgba(250, 204, 21, 0.45);
      border-left: 5px solid #facc15;
    }}
    .level-card.lvl-green {{
      border: 1px solid rgba(0, 242, 254, 0.45);
      border-left: 5px solid var(--accent-turquoise);
    }}

    .level-header {{
      font-size: 1.18rem;
      font-weight: 700;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .lvl-red .level-header {{ color: #fb7185; }}
    .lvl-orange .level-header {{ color: #fdba74; }}
    .lvl-yellow .level-header {{ color: #fde047; }}
    .lvl-green .level-header {{ color: var(--accent-turquoise); }}

    .level-body {{
      font-size: 1.08rem;
      line-height: 1.45;
      color: var(--text-main);
    }}

    /* Q&A Presentation Box (Slide 8) */
    .qa-box {{
      background: var(--card-bg);
      backdrop-filter: blur(14px);
      border: 2px solid rgba(0, 242, 254, 0.45);
      border-radius: 24px;
      padding: 50px 60px;
      max-width: 820px;
      width: 100%;
      box-shadow: 0 20px 50px rgba(0, 242, 254, 0.18);
      text-align: center;
    }}

    /* Nav Arrows */
    .nav-arrow {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.22);
      color: #fff;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 50;
      transition: all 0.2s ease;
      font-size: 1.3rem;
    }}

    .nav-arrow:hover {{
      background: var(--accent-turquoise);
      color: #09030f;
      border-color: var(--accent-turquoise);
    }}

    .nav-prev {{ left: 18px; }}
    .nav-next {{ right: 18px; }}

    /* Footer bar inside deck */
    .slide-footer {{
      position: absolute;
      bottom: 14px;
      left: 35px;
      right: 35px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      padding-top: 8px;
      z-index: 20;
    }}

    .key-hint {{
      margin-top: 14px;
      font-size: 0.85rem;
      color: #94a3b8;
    }}

    .key-badge {{
      background: rgba(255, 255, 255, 0.12);
      padding: 3px 8px;
      border-radius: 6px;
      font-family: monospace;
      color: var(--accent-turquoise);
    }}
  </style>
</head>
<body>

  <!-- Controls Bar -->
  <div class="controls-bar">
    <button class="btn" onclick="prevSlide()">← Anterior</button>
    <div class="slide-counter-badge" id="slideNum">Slide 1 / 8</div>
    <button class="btn" onclick="nextSlide()">Siguiente →</button>
    <button class="btn" onclick="toggleTheme()">🌓 Tema (Oscuro / Claro)</button>
    <button class="btn" onclick="toggleFullscreen()">⛶ Pantalla Completa</button>
  </div>

  <!-- Deck Viewport -->
  <div class="deck-viewport" id="deck">
    <div class="glow-circle-1"></div>
    <div class="glow-circle-2"></div>

    <button class="nav-arrow nav-prev" onclick="prevSlide()">‹</button>
    <button class="nav-arrow nav-next" onclick="nextSlide()">›</button>

    <!-- SLIDE 1: PORTADA OFICIAL -->
    <div class="slide active">
      <span class="tag-header">RealMente Club • Clase en Vivo</span>
      <h1 class="slide-title">RealMente la trampa de la culpa y el precio invisible de asumir esta nueva identidad</h1>
      <p class="slide-subtitle">Episodio 62 • RealMente Club<br><strong style="color: var(--accent-turquoise);">Con Marbelis Montero</strong></p>
    </div>

    <!-- SLIDE 2: FRASE DE APERTURA -->
    <div class="slide">
      <span class="tag-header">Punto de Partida</span>
      <div class="quote-box">
        <p class="quote-text">"Es preferible sostener la incomodidad de no complacer al mundo que vivir con el peso de haberte traicionado a ti misma."</p>
        <p class="quote-author">— Marbelis Montero</p>
      </div>
    </div>

    <!-- SLIDE 3: LA MESA DE 4 PATAS (DIBUJO LITERAL) -->
    <div class="slide">
      <span class="tag-header">Metáfora Visual</span>
      <h2 class="slide-title" style="font-size: 2.1rem; margin-bottom: 8px;">La Mesa de 4 Patas de la Culpa</h2>
      
      <div class="table-graphic-box">
        <img src="{data_uri}" alt="La Mesa de 4 Patas de la Culpa">
      </div>
    </div>

    <!-- SLIDE 4: EXPLICACIÓN DE LAS 4 PATAS -->
    <div class="slide">
      <span class="tag-header">Metáfora Diagnóstica</span>
      <h2 class="slide-title" style="font-size: 2.1rem; margin-bottom: 10px;">Las 4 Posiciones de la Culpa</h2>
      
      <div class="table-structure">
        <div class="table-top-bar">
          ⚖️ La Superficie del Juicio Moral (Blanco y Negro)
        </div>
        
        <div class="legs-grid">
          <!-- PATA 1 -->
          <div class="leg-card leg-1">
            <span class="leg-badge">Pata 1</span>
            <div class="leg-title">Lo «Bueno»</div>
            <p class="leg-desc">El mandato del "deber ser", la complacencia y sacrificarte para ser aceptada.</p>
          </div>

          <!-- PATA 2 -->
          <div class="leg-card leg-2">
            <span class="leg-badge">Pata 2</span>
            <div class="leg-title">Lo «Malo»</div>
            <p class="leg-desc">El juicio moral y el terror inconsciente a que te llamen egoísta.</p>
          </div>

          <!-- PATA 3 -->
          <div class="leg-card leg-3">
            <span class="leg-badge">Pata 3</span>
            <div class="leg-title">La Víctima</div>
            <p class="leg-desc">Instalarte en el sufrimiento porque "los demás" te lastiman o te exigen.</p>
          </div>

          <!-- PATA 4 -->
          <div class="leg-card leg-4">
            <span class="leg-badge">Pata 4</span>
            <div class="leg-title">La Victimaria</div>
            <p class="leg-desc">La culpa de poner límites o cobrar, creyendo que perjudicas al otro.</p>
          </div>
        </div>

        <p class="table-footer-anchor">
          "Vives rotando entre estas 4 posiciones. Toda la culpa se sostiene aquí."
        </p>
      </div>
    </div>

    <!-- SLIDE 5: RESULTADO DEL INSTRUMENTO -->
    <div class="slide">
      <span class="tag-header">Autoevaluación de Identidad</span>
      <h2 class="slide-title" style="font-size: 2.1rem; margin-bottom: 12px;">Tu Nivel de Culpa Inconsciente</h2>
      
      <div class="levels-grid">
        <!-- NIVEL 1 -->
        <div class="level-card lvl-red">
          <div class="level-header">
            <span>🔴 17 a 21 pts</span>
            <span style="font-size: 0.95rem; opacity: 0.9;">(80% - 100%)</span>
          </div>
          <div style="font-weight: 700; font-size: 1.15rem; margin-bottom: 3px; color: var(--text-main);">La Guardiana del Deber Ser</div>
          <p class="level-body">Existir, descansar o cobrar se sienten como un delito. Compras paz ajena pagando con tu propia frustración.</p>
        </div>

        <!-- NIVEL 2 -->
        <div class="level-card lvl-orange">
          <div class="level-header">
            <span>🟠 12 a 16 pts</span>
            <span style="font-size: 0.95rem; opacity: 0.9;">(55% - 75%)</span>
          </div>
          <div style="font-weight: 700; font-size: 1.15rem; margin-bottom: 3px; color: var(--text-main);">La Compradora de Paz Ajena</div>
          <p class="level-body">Avanzas hacia tu meta, pero pagas un peaje constante de sobreesfuerzo y justificaciones interminables.</p>
        </div>

        <!-- NIVEL 3 -->
        <div class="level-card lvl-yellow">
          <div class="level-header">
            <span>🟡 6 a 11 pts</span>
            <span style="font-size: 0.95rem; opacity: 0.9;">(25% - 50%)</span>
          </div>
          <div style="font-weight: 700; font-size: 1.15rem; margin-bottom: 3px; color: var(--text-main);">El Techo de Expansión</div>
          <p class="level-body">Pones límites básicos, pero la culpa te frena cada vez que quieres dar un salto de mayor visibilidad o dinero.</p>
        </div>

        <!-- NIVEL 4 -->
        <div class="level-card lvl-green">
          <div class="level-header">
            <span>🟢 0 a 5 pts</span>
            <span style="font-size: 0.95rem; opacity: 0.9;">(0% - 20%)</span>
          </div>
          <div style="font-weight: 700; font-size: 1.15rem; margin-bottom: 3px; color: var(--text-main);">Soberanía y Neutralidad</div>
          <p class="level-body">Los hechos son neutros; toleras la molestia ajena sin cargártela y tus metas no son negociables.</p>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: EJERCICIO PRÁCTICO (SOLO EL TÍTULO EN GRANDE) -->
    <div class="slide">
      <div class="minimal-box">
        <h1 class="minimal-title">Ejercicio práctico</h1>
      </div>
    </div>

    <!-- SLIDE 7: FRASE DE CIERRE -->
    <div class="slide">
      <span class="tag-header">Anclaje y Soberanía</span>
      <div class="quote-box">
        <p class="quote-text">"La culpa no es una pared para retroceder, es la puerta que confirma que ya estás lista para tu siguiente nivel."</p>
        <p class="quote-author">— Marbelis Montero</p>
      </div>
    </div>

    <!-- SLIDE 8: ESPACIO ABIERTO A PREGUNTAS -->
    <div class="slide">
      <span class="tag-header" style="background: rgba(0, 242, 254, 0.15); border-color: rgba(0, 242, 254, 0.4); color: var(--accent-turquoise);">
        🎙️ Espacio Exclusivo RealMente Club
      </span>
      <div class="qa-box">
        <h2 class="slide-title" style="font-size: 2.5rem; margin-bottom: 14px; color: var(--accent-turquoise);">
          Mentoría en Vivo y Preguntas
        </h2>
        <p class="slide-subtitle" style="font-size: 1.35rem; color: var(--text-main); font-weight: 600; margin-bottom: 14px;">
          Revisemos tu caso y desarticulemos tu freno de culpa
        </p>
        <p style="font-size: 1.18rem; color: var(--accent-lilac); font-weight: 400; line-height: 1.5;">
          Micrófonos y chat abiertos para las socias del Club.
        </p>
      </div>
    </div>

    <!-- Footer Bar inside Deck -->
    <div class="slide-footer">
      <span>RealMente Club • Episodio 62</span>
      <span>Marbelis Montero — Master Trainer en PNL</span>
    </div>
  </div>

  <!-- Key hint -->
  <div class="key-hint">
    <span>Navega con teclado: <span class="key-badge">←</span> <span class="key-badge">→</span> o clic en las flechas</span>
  </div>

  <script>
    const slides = document.querySelectorAll('.slide');
    const slideNum = document.getElementById('slideNum');
    const deck = document.getElementById('deck');
    let currentSlide = 0;
    const totalSlides = slides.length;

    function showSlide(index) {{
      if (index < 0) index = 0;
      if (index >= totalSlides) index = totalSlides - 1;
      
      slides.forEach((slide, idx) => {{
        slide.classList.remove('active');
        if (idx === index) {{
          slide.classList.add('active');
        }}
      }});
      
      currentSlide = index;
      slideNum.textContent = `Slide ${{currentSlide + 1}} / ${{totalSlides}}`;
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides - 1) {{
        showSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 0) {{
        showSlide(currentSlide - 1);
      }}
    }}

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        prevSlide();
      }}
    }});

    // Theme Toggle (Light / Dark)
    function toggleTheme() {{
      const currentTheme = document.body.getAttribute('data-theme');
      if (currentTheme === 'light') {{
        document.body.removeAttribute('data-theme');
      }} else {{
        document.body.setAttribute('data-theme', 'light');
      }}
    }}

    // Fullscreen Toggle
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        deck.requestFullscreen().catch(err => {{
          alert(`Error al activar pantalla completa: ${{err.message}}`);
        }});
      }} else {{
        document.exitFullscreen();
      }}
    }}
  </script>
</body>
</html>'''

path1 = r'c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\presentacion_episodio_62.html'
path2 = r'c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas\presentacion_episodio_62.html'

for p in [path1, path2]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_template)

print('Updated both presentations with 8 slides, including table illustration and explanation cards!')
