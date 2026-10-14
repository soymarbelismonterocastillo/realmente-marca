import os
import sys
from PIL import Image, ImageDraw, ImageFont

ARTIFACT_DIR = r"C:\Users\soyma\.gemini\antigravity\brain\d7d58a4c-2e8e-4b53-9cc8-4d992040c3ac"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

# Canvas Dimensions (16:9 1280x720)
W, H = 1280, 720

# Color Palette: Clean high-contrast dark mode
C_BG = (25, 6, 51)           # #190633 Dark Purple Background
C_CARD = (44, 12, 85)        # #2C0C55 Card Container
C_TEAL = (42, 210, 197)      # #2AD2C5 Bright Cyan Accent
C_PINK = (255, 90, 141)      # #FF5A8D Bright Pink Accent
C_LAVENDER = (180, 140, 220) # Soft Lavender Accent for headers only
C_WHITE = (255, 255, 255)    # PURE WHITE for ALL body text & subtitles

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "calibrib.ttf" if bold else "calibri.ttf"]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except IOError:
            continue
    return ImageFont.load_default()

font_badge = get_font(15, bold=True)
font_title = get_font(38, bold=True)
font_subtitle = get_font(22, bold=False)
font_card_title = get_font(24, bold=True)
font_card_body = get_font(21, bold=False)  # Increased font size for readability
font_quote = get_font(28, bold=True)
font_footer = get_font(15, bold=False)

def draw_header(draw, tag_text, title_text, subtitle_text=None):
    # Subtle thin top line + tag text (no thick ugly box)
    draw.line([70, 45, 150, 45], fill=C_TEAL, width=3)
    draw.text((165, 38), tag_text.upper(), font=font_badge, fill=C_TEAL)

    # Main Title (White, Large)
    draw.text((70, 85), title_text, font=font_title, fill=C_WHITE)

    # Subtitle (White/Cyan, Large)
    if subtitle_text:
        draw.text((70, 142), subtitle_text, font=font_subtitle, fill=C_WHITE)

def draw_footer(draw, current, total=13):
    draw.line([70, 665, 1210, 665], fill=(255, 255, 255, 40), width=1)
    draw.text((70, 678), "RealMente Club · Marbelis Montero", font=font_footer, fill=C_WHITE)
    draw.text((1120, 678), f"Slide {current} de {total}", font=font_footer, fill=C_WHITE)

# SLIDE 1: PORTADA
def create_slide_1():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)

    # Subtle Badge
    draw.line([440, 65, 480, 65], fill=C_TEAL, width=3)
    draw.text((500, 56), "REALMENTE CLUB · CLASE EN VIVO", font=font_badge, fill=C_TEAL)

    # Title lines
    draw.text((W//2, 175), "Tu vida no cambia cuando lo entiendes,", font=font_title, fill=C_WHITE, anchor="mm")
    draw.text((W//2, 230), "cambia cuando lo ejecutas", font=font_title, fill=C_WHITE, anchor="mm")

    # Subtitle
    draw.text((W//2, 295), "De la teoría a la acción: Desmantelando los 4 patrones de saboteo", font=font_subtitle, fill=C_TEAL, anchor="mm")

    # Info Card Box
    draw.rounded_rectangle([180, 370, 1100, 570], radius=20, fill=C_CARD, outline=C_TEAL, width=2)
    draw.text((W//2, 415), "📅 Sábado 19 de Septiembre, 2026", font=font_card_title, fill=C_WHITE, anchor="mm")
    draw.text((W//2, 465), "🎙️ Facilitadora: Marbelis Montero (Coach & Trainer en PNL)", font=font_card_body, fill=C_WHITE, anchor="mm")
    draw.text((W//2, 515), "💜 Enfoque de Hoy: Romper la parálisis por análisis y pasar a la ejecución", font=font_card_body, fill=C_TEAL, anchor="mm")

    draw_footer(draw, 1)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_1.png"))

# SLIDE 2: FRASE DE APERTURA
def create_slide_2():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "REFLEXIÓN DE APERTURA", "Tu Verdadero Punto de Partida Hoy")

    # Quote Box
    draw.rounded_rectangle([100, 210, 1180, 590], radius=24, fill=C_CARD, outline=C_TEAL, width=3)
    draw.rectangle([100, 210, 116, 590], fill=C_TEAL)

    text_lines = [
        "“Saber lo que tienes que hacer y no hacerlo es exactamente",
        "lo mismo que no saber nada. Tu vida no cambia con la teoría",
        "que entiendes en la cabeza, cambia con la imperfección",
        "que te atreves a ejecutar en el mundo real.”"
    ]
    y = 280
    for line in text_lines:
        color = C_TEAL if "imperfección" in line else C_WHITE
        draw.text((150, y), line, font=font_quote, fill=color)
        y += 60

    draw_footer(draw, 2)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_2.png"))

# SLIDE 3: ENCUADRE
def create_slide_3():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "CONCEPTO CLAVE", "La Brecha Entre Entender y Ejecutar", "Por qué saberlo todo no está cambiando tu vida")

    cards = [
        ("📚 Zona de Confort del Saber", "Creer que acumular información, libros y podcasts equivale a transformar tu vida real.", C_TEAL),
        ("🧠 La Ilusión del Ego", "El ego te hace sentir que 'estás trabajando en ti' al analizar, para evitar el riesgo de actuar.", C_PINK),
        ("⚡ La Verdad Incómoda", "Entender calma la culpa, pero solo la ejecución concreta reprograma tu mente real.", C_TEAL)
    ]
    for i, (ctitle, cdesc, color) in enumerate(cards):
        x = 70 + i * 395
        draw.rounded_rectangle([x, 210, x + 350, 610], radius=20, fill=C_CARD, outline=color, width=2)
        draw.text((x + 25, 245), ctitle, font=font_card_title, fill=C_WHITE)
        
        words = cdesc.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 22:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        
        cy = 320
        for line in lines:
            draw.text((x + 25, cy), line, font=font_card_body, fill=C_WHITE)
            cy += 38

    draw_footer(draw, 3)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_3.png"))

# SLIDE 4: MAPA DEL SABOTEO
def create_slide_4():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "MAPA MENTAL DE LA PARÁLISIS", "Las 2 Grandes Trampas Invisibles del Ego", "De dónde nace tu procrastinación sofisticada")

    # Left Card
    draw.rounded_rectangle([70, 210, 610, 610], radius=20, fill=C_CARD, outline=C_PINK, width=3)
    draw.text((100, 250), "🔴 La Trampa del Pasado", font=font_card_title, fill=C_PINK)
    draw.text((100, 295), "Adicción al 'Por Qué'", font=font_card_title, fill=C_WHITE)
    lines1 = ["Creer que necesitas resolver o entender", "hasta el último origen de tu pasado", "antes de dar un solo paso en el presente."]
    cy = 370
    for l in lines1:
        draw.text((100, cy), l, font=font_card_body, fill=C_WHITE)
        cy += 40

    # Right Card
    draw.rounded_rectangle([670, 210, 1210, 610], radius=20, fill=C_CARD, outline=C_TEAL, width=3)
    draw.text((700, 250), "🟣 La Trampa del Futuro", font=font_card_title, fill=C_TEAL)
    draw.text((700, 295), "Ilusión del 'Momento Perfecto'", font=font_card_title, fill=C_WHITE)
    lines2 = ["Creer que debes esperar a que tus emociones,", "tu seguridad, tu motivación y el entorno", "estén totalmente impecables antes de actuar."]
    cy = 370
    for l in lines2:
        draw.text((700, cy), l, font=font_card_body, fill=C_WHITE)
        cy += 40

    draw_footer(draw, 4)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_4.png"))

# PATTERN SLIDES BUILDER (5 to 8)
def create_pattern_slide(slide_num, tag, title, p1, p2, p3):
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, tag, title)

    pts = [p1, p2, p3]
    for i, (t, d, col) in enumerate(pts):
        y = 195 + i * 148
        draw.rounded_rectangle([70, y, 1210, y + 130], radius=18, fill=C_CARD, outline=col, width=2)
        draw.text((100, y + 20), t, font=font_card_title, fill=col)
        draw.text((100, y + 68), d, font=font_card_body, fill=C_WHITE)

    draw_footer(draw, slide_num)
    img.save(os.path.join(ARTIFACT_DIR, f"diapositiva_{slide_num}.png"))

# SLIDE 5: PATRÓN 1
def create_slide_5():
    create_pattern_slide(5, "TRAMPA DEL PASADO · PATRÓN 1", "La Analista del Pasado ('La Adicción al Por Qué')",
        ("🔍 El Mecanismo del Ego", "Creer que comprender la causa original o el trauma del pasado equivale automáticamente a haber resuelto el problema.", C_PINK),
        ("🔄 El Bucle de las Explicaciones", "Buscar infinitos justificativos en tu historia para darte la razón y quedarte en la zona conocida de comodidad.", C_TEAL),
        ("💥 La Verdad Incómoda", "Entender a medias consuela la culpa del ego, pero no cambia tu comportamiento presente si no ejecutas.", C_WHITE)
    )

# SLIDE 6: PATRÓN 2
def create_slide_6():
    create_pattern_slide(6, "TRAMPA DEL PASADO · PATRÓN 2", "La Sanadora Eterna ('La Excusa del Trabajo Previo')",
        ("🛡️ El Escudo de la Sanación", "Usar la sanación como una coraza sofisticada para evitar la exposición, el rechazo y el riesgo de actuar.", C_PINK),
        ("🚫 La Premisa Limítrofe", "Creer firmemente: 'Hasta que no sane esto del todo o termine este taller, no me puedo exigir avanzar'.", C_WHITE),
        ("✨ La Verdad Incómoda", "La acción concreta en el presente es la mejor herramienta de reprogramación y sanación, no el requisito previo.", C_TEAL)
    )

# SLIDE 7: PATRÓN 3
def create_slide_7():
    create_pattern_slide(7, "TRAMPA DEL FUTURO · PATRÓN 3", "La Esperadora del Momento Perfecto ('La Ilusión del Futuro')",
        ("⏳ El Mecanismo de Postergación", "Postergar decisiones esperando que las circunstancias o tu estado emocional estén mágicamente alineados.", C_TEAL),
        ("🔮 El Mito de Sentirse Lista", "Fantasear con que un día te despertarás sintiéndote 100% segura, confiada, sin dudas y sin ningún tipo de miedo.", C_PINK),
        ("🎯 La Verdad Incómoda", "El momento perfecto no existe. Esperarlo es una defensa contra la incomodidad de aprender sobre la marcha.", C_WHITE)
    )

# SLIDE 8: PATRÓN 4
def create_slide_8():
    create_pattern_slide(8, "TRAMPA DEL FUTURO · PATRÓN 4", "La Protectora del Potencial ('La Fantasía del Control')",
        ("💎 La Fantasía Idealizada", "Enamorarse de las ideas en la cabeza, donde todo es impecable porque nadie las juzga ni las pone a prueba.", C_TEAL),
        ("🫣 El Miedo al Choque de Realidad", "Aterra chocar con la realidad concreta porque la realidad siempre es imperfecta, caótica e incontrolable.", C_PINK),
        ("🔨 La Verdad Incómoda", "Es mil veces preferible un primer intento imperfecto en el mundo real que conservar el estatus de 'gran potencial no realizado'.", C_WHITE)
    )

# SLIDE 9: NADAR
def create_slide_9():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "APRENDIZAJE EN ACCIÓN", "La Metáfora de Lanzarse al Agua", "Aprender a nadar exige estar en el medio")

    cards = [
        ("🏖️ Fuera del Agua (Teoría)", "En la orilla todo es planificación limpia y perfecta. Pero afuera NO estás aprendiendo a nadar.", C_TEAL),
        ("🌊 Dentro del Agua (Acción)", "Para aprender a nadar hay que lanzarse, sentir la densidad del agua, patalear y tragar agua.", C_PINK),
        ("🏊‍♀️ La Lección de Vida", "No se aprende a nadar mirando la piscina; la maestría se construye ejecutando adentro.", C_TEAL)
    ]
    for i, (ctitle, cdesc, color) in enumerate(cards):
        x = 70 + i * 395
        draw.rounded_rectangle([x, 210, x + 350, 610], radius=20, fill=C_CARD, outline=color, width=2)
        draw.text((x + 25, 245), ctitle, font=font_card_title, fill=C_WHITE)
        
        words = cdesc.split()
        lines = []
        cur = ""
        for w in words:
            if len(cur + " " + w) > 22:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        
        cy = 320
        for line in lines:
            draw.text((x + 25, cy), line, font=font_card_body, fill=C_WHITE)
            cy += 38

    draw_footer(draw, 9)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_9.png"))

# SLIDE 10: ACCIÓN ES FRÍA
def create_slide_10():
    create_pattern_slide(10, "DISCIPLINA vs. EMOCIÓN", "La Acción es Fría: Desmitificando la Motivación",
        ("📉 La Falacia de la Motivación", "Esperar 'sentir ganas' te paraliza porque la emoción previa es voluble e inestable.", C_PINK),
        ("🧊 La Acción es Neutra y Fría", "Accionar no requiere emoción previa; requiere decisión en automático sin pedir permiso a tu estado de ánimo.", C_TEAL),
        ("🏆 El Orden Real", "El orgullo, la satisfacción y la motivación vienen DESPUÉS de accionar, nunca antes.", C_WHITE)
    )

# SLIDE 11: EJERCICIO
def create_slide_11():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "PNL & PRÁCTICA EN VIVO", "Ejercicio Práctico: De la Teoría a la Acción")

    draw.rounded_rectangle([150, 230, 1130, 580], radius=24, fill=C_CARD, outline=C_TEAL, width=3)
    draw.text((W//2, 340), "🧘‍♀️ Ejercicio Práctico del Club", font=font_title, fill=C_WHITE, anchor="mm")
    draw.text((W//2, 420), "Guiado en vivo por Marbelis Montero", font=font_subtitle, fill=C_TEAL, anchor="mm")

    draw_footer(draw, 11)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_11.png"))

# SLIDE 12: SALTO IDENTIDAD
def create_slide_12():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "TRANSFORMACIÓN DE IDENTIDAD", "El Salto de Identidad y Compromiso")

    draw.rounded_rectangle([70, 180, 610, 360], radius=18, fill=C_CARD, outline=C_TEAL, width=2)
    draw.text((95, 210), "👤 Cambio de Postura", font=font_card_title, fill=C_TEAL)
    draw.text((95, 255), "Dejar de identificarte como 'la que analiza/sana'", font=font_card_body, fill=C_WHITE)
    draw.text((95, 295), "y encarnar a 'la persona que ejecuta hoy'.", font=font_card_body, fill=C_WHITE)

    draw.rounded_rectangle([670, 180, 1210, 360], radius=18, fill=C_CARD, outline=C_PINK, width=2)
    draw.text((695, 210), "🤝 Compromiso de 24 Horas", font=font_card_title, fill=C_PINK)
    draw.text((695, 255), "Ejecutar tu acción mínima hoy antes de dormir", font=font_card_body, fill=C_WHITE)
    draw.text((695, 295), "sin excusas y compartirla en la comunidad.", font=font_card_body, fill=C_WHITE)

    # Final Quote
    draw.rounded_rectangle([70, 400, 1210, 600], radius=20, fill=C_CARD, outline=C_TEAL, width=2)
    q_lines = [
        "“No esperes a estar lista para lanzarte al agua; lánzate al agua para aprender a estar lista.",
        "Al final del día, tu potencial no se mide por lo impecable que es tu idea en la mente,",
        "sino por la valentía con la que encarnas tu nueva identidad en la realidad.”"
    ]
    cy = 445
    for ql in q_lines:
        col = C_TEAL if "valentía" in ql else C_WHITE
        draw.text((W//2, cy), ql, font=font_card_body, fill=col, anchor="mm")
        cy += 45

    draw_footer(draw, 12)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_12.png"))

# SLIDE 13: PAUSA GRABACIÓN (EXACT LAYOUT FROM LAST WEEK SLIDE 10)
def create_slide_13():
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)

    # Header Badge (Centered, subtle)
    draw.line([540, 65, 570, 65], fill=C_TEAL, width=3)
    draw.text((580, 56), "COMUNIDAD EN VIVO", font=font_badge, fill=C_TEAL)

    # Main Title (Centered, White, Large)
    draw.text((W//2, 175), "Espacio de Preguntas & Reprogramación", font=font_title, fill=C_WHITE, anchor="mm")

    # Center Pill Badge (Centered capsule box)
    draw.rounded_rectangle([340, 290, 940, 390], radius=45, fill=(42, 210, 197, 30), outline=C_TEAL, width=3)
    draw.text((W//2, 340), "⏸️ Pausamos la grabación para conversar", font=font_card_title, fill=C_TEAL, anchor="mm")

    # Subtitle (Centered, White)
    draw.text((W//2, 480), "Un espacio seguro y privado para nuestra comunidad", font=font_subtitle, fill=C_WHITE, anchor="mm")

    draw_footer(draw, 13)
    img.save(os.path.join(ARTIFACT_DIR, "diapositiva_13.png"))

if __name__ == "__main__":
    create_slide_1()
    create_slide_2()
    create_slide_3()
    create_slide_4()
    create_slide_5()
    create_slide_6()
    create_slide_7()
    create_slide_8()
    create_slide_9()
    create_slide_10()
    create_slide_11()
    create_slide_12()
    create_slide_13()
    print("Re-generated slide PNGs with crisp white text, large fonts, subtle headers, and clean Slide 13!")
