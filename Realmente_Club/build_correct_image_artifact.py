import os
import shutil
from PIL import Image, ImageDraw, ImageFont

ARTIFACT_DIR = r"C:\Users\soyma\.gemini\antigravity\brain\d7d58a4c-2e8e-4b53-9cc8-4d992040c3ac"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

# Generate high resolution PNGs (1280x720) with name diapositiva_1.png to diapositiva_13.png
W, H = 1280, 720
C_BG = (25, 6, 51)           # #190633 Dark Purple
C_CARD = (46, 12, 89)        # #2E0C59 Plum Purple Card
C_TEAL = (42, 210, 197)      # #2AD2C5 Cyan Accent
C_PINK = (255, 90, 141)      # #FF5A8D Pink Accent
C_LAVENDER = (212, 178, 230) # #D4B2E6 Lavender Accent
C_WHITE = (255, 255, 255)
C_MUTED = (220, 205, 235)

def get_font(size, bold=False):
    font_names = ["arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf", "calibrib.ttf" if bold else "calibri.ttf"]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except IOError:
            continue
    return ImageFont.load_default()

font_badge = get_font(16, bold=True)
font_title = get_font(36, bold=True)
font_subtitle = get_font(20, bold=False)
font_card_title = get_font(22, bold=True)
font_card_body = get_font(17, bold=False)
font_quote = get_font(26, bold=True)
font_footer = get_font(15, bold=False)

def draw_header(draw, tag_text, title_text, subtitle_text=None):
    draw.rounded_rectangle([70, 45, 420, 80], radius=15, fill=(42, 210, 197, 35), outline=C_TEAL, width=2)
    draw.text((85, 52), tag_text.upper(), font=font_badge, fill=C_TEAL)
    draw.text((70, 95), title_text, font=font_title, fill=C_WHITE)
    if subtitle_text:
        draw.text((70, 145), subtitle_text, font=font_subtitle, fill=C_LAVENDER)

def draw_footer(draw, current, total=13):
    draw.line([70, 665, 1210, 665], fill=(255, 255, 255, 40), width=1)
    draw.text((70, 678), "RealMente Club · Marbelis Montero", font=font_footer, fill=C_MUTED)
    draw.text((1120, 678), f"Slide {current} de {total}", font=font_footer, fill=C_MUTED)

# Slide 1
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([440, 70, 840, 110], radius=20, fill=(42, 210, 197, 30), outline=C_TEAL, width=2)
draw.text((465, 78), "REALMENTE CLUB · SESIÓN EN VIVO", font=font_badge, fill=C_TEAL)
draw.text((W//2, 190), "Tu vida no cambia cuando lo entiendes,", font=font_title, fill=C_WHITE, anchor="mm")
draw.text((W//2, 245), "cambia cuando lo ejecutas", font=font_title, fill=C_WHITE, anchor="mm")
draw.text((W//2, 310), "De la teoría a la acción: Desmantelando los 4 patrones de saboteo", font=font_subtitle, fill=C_TEAL, anchor="mm")
draw.rounded_rectangle([180, 390, 1100, 560], radius=20, fill=C_CARD, outline=C_LAVENDER, width=2)
draw.text((W//2, 435), "📅 Sábado 19 de Septiembre, 2026", font=font_card_title, fill=C_WHITE, anchor="mm")
draw.text((W//2, 480), "🎙️ Facilitadora: Marbelis Montero (Coach & Trainer en PNL)", font=font_card_body, fill=C_MUTED, anchor="mm")
draw.text((W//2, 515), "💜 Enfoque de Hoy: Romper la parálisis por análisis y pasar a la ejecución", font=font_card_body, fill=C_TEAL, anchor="mm")
draw_footer(draw, 1)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_1.png"))

# Slide 2
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "REFLEXIÓN DE APERTURA", "Tu Verdadero Punto de Partida Hoy")
draw.rounded_rectangle([100, 220, 1180, 580], radius=24, fill=C_CARD, outline=C_TEAL, width=3)
draw.rectangle([100, 220, 116, 580], fill=C_TEAL)
lines = [
    "“Saber lo que tienes que hacer y no hacerlo es exactamente",
    "lo mismo que no saber nada. Tu vida no cambia con la teoría",
    "que entiendes en la cabeza, cambia con la imperfección",
    "que te atreves a ejecutar en el mundo real.”"
]
y = 300
for l in lines:
    col = C_TEAL if "imperfección" in l else C_WHITE
    draw.text((150, y), l, font=font_quote, fill=col)
    y += 55
draw_footer(draw, 2)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_2.png"))

# Slide 3
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "CONCEPTO CLAVE", "La Brecha Entre Entender y Ejecutar", "Por qué saberlo todo no está cambiando tu vida")
cards = [
    ("📚 Zona de Confort del Saber", "Creer que acumular información, libros, podcasts y diagnósticos equivale a transformar tu vida.", C_TEAL),
    ("🧠 La Ilusión del Ego", "El ego te hace sentir que 'estás trabajando en ti' al analizar, para evitar el riesgo de actuar.", C_PINK),
    ("⚡ La Verdad Incómoda", "Entender calma la culpa, pero solo la ejecución concreta reprograma tu mente real.", C_LAVENDER)
]
for i, (ctitle, cdesc, color) in enumerate(cards):
    x = 70 + i * 395
    draw.rounded_rectangle([x, 220, x + 350, 600], radius=20, fill=C_CARD, outline=color, width=2)
    draw.text((x + 25, 260), ctitle, font=font_card_title, fill=C_WHITE)
    words = cdesc.split()
    cur, l_list = "", []
    for w in words:
        if len(cur + " " + w) > 26:
            l_list.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: l_list.append(cur)
    cy = 340
    for l in l_list:
        draw.text((x + 25, cy), l, font=font_card_body, fill=C_MUTED)
        cy += 32
draw_footer(draw, 3)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_3.png"))

# Slide 4
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "MAPA MENTAL DE LA PARÁLISIS", "Las 2 Grandes Trampas Invisibles del Ego", "De dónde nace tu procrastinación sofisticada")
draw.rounded_rectangle([70, 220, 610, 600], radius=20, fill=C_CARD, outline=C_PINK, width=3)
draw.text((100, 260), "🔴 La Trampa del Pasado", font=font_card_title, fill=C_PINK)
draw.text((100, 305), "Adicción al 'Por Qué'", font=font_card_title, fill=C_WHITE)
for idx, l in enumerate(["Creer que necesitas resolver o entender", "hasta el último origen histórico de tu pasado", "antes de dar un solo paso firme en el presente."]):
    draw.text((100, 380 + idx * 34), l, font=font_card_body, fill=C_MUTED)
draw.rounded_rectangle([670, 220, 1210, 600], radius=20, fill=C_CARD, outline=C_LAVENDER, width=3)
draw.text((700, 260), "🟣 La Trampa del Futuro", font=font_card_title, fill=C_LAVENDER)
draw.text((700, 305), "Ilusión del 'Momento Perfecto'", font=font_card_title, fill=C_WHITE)
for idx, l in enumerate(["Creer que debes esperar a que tus emociones,", "tu seguridad, tu motivación y las circunstancias", "estén totalmente impecables antes de actuar."]):
    draw.text((700, 380 + idx * 34), l, font=font_card_body, fill=C_MUTED)
draw_footer(draw, 4)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_4.png"))

# Pattern helper
def make_pattern(s_num, tag, title, p1, p2, p3):
    img = Image.new("RGB", (W, H), C_BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw, tag, title)
    for i, (t, d, col) in enumerate([p1, p2, p3]):
        y = 200 + i * 145
        draw.rounded_rectangle([70, y, 1210, y + 125], radius=18, fill=C_CARD, outline=col, width=2)
        draw.text((100, y + 22), t, font=font_card_title, fill=col)
        draw.text((100, y + 65), d, font=font_card_body, fill=C_WHITE)
    draw_footer(draw, s_num)
    img.save(os.path.join(ARTIFACT_DIR, f"diapositiva_{s_num}.png"))

make_pattern(5, "TRAMPA DEL PASADO · PATRÓN 1", "La Analista del Pasado ('La Adicción al Por Qué')",
    ("🔍 El Mecanismo del Ego", "Creer que comprender la causa original o el trauma del pasado equivale automáticamente a haber resuelto el problema.", C_PINK),
    ("🔄 El Bucle de las Explicaciones", "Buscar infinitos justificativos en tu historia para darte la razón y quedarte en la zona conocida de comodidad.", C_TEAL),
    ("💥 La Verdad Incómoda", "Entender a medias consuela la culpa del ego, pero no cambia tu comportamiento presente si no ejecutas.", C_LAVENDER))

make_pattern(6, "TRAMPA DEL PASADO · PATRÓN 2", "La Sanadora Eterna ('La Excusa del Trabajo Previo')",
    ("🛡️ El Escudo de la Sanación", "Usar la sanación como una coraza sofisticada para evitar la exposición, el rechazo y el riesgo de actuar.", C_PINK),
    ("🚫 La Premisa Limítrofe", "Creer firmemente: 'Hasta que no sane esto del todo o termine este taller, no me puedo exigir avanzar'.", C_LAVENDER),
    ("✨ La Verdad Incómoda", "La acción concreta en el presente es la mejor herramienta de reprogramación y sanación, no el requisito previo.", C_TEAL))

make_pattern(7, "TRAMPA DEL FUTURO · PATRÓN 3", "La Esperadora del Momento Perfecto ('La Ilusión del Futuro')",
    ("⏳ El Mecanismo de Postergación", "Postergar decisiones esperando que las circunstancias o tu estado emocional estén mágicamente alineados.", C_LAVENDER),
    ("🔮 El Mito de Sentirse Lista", "Fantasear con que un día te despertarás sintiéndote 100% segura, confiada, sin dudas y sin ningún tipo de miedo.", C_PINK),
    ("🎯 La Verdad Incómoda", "El momento perfecto no existe. Esperarlo es una defensa contra la incomodidad de aprender sobre la marcha.", C_TEAL))

make_pattern(8, "TRAMPA DEL FUTURO · PATRÓN 4", "La Protectora del Potencial ('La Fantasía del Control')",
    ("💎 La Fantasía Idealizada", "Enamorarse de las ideas en la cabeza, donde todo es impecable porque nadie las juzga ni las pone a prueba.", C_TEAL),
    ("🫣 El Miedo al Choque de Realidad", "Aterra chocar con la realidad concreta porque la realidad siempre es imperfecta, caótica e incontrolable.", C_PINK),
    ("🔨 La Verdad Incómoda", "Es mil veces preferible un primer intento imperfecto en el mundo real que conservar el estatus de 'alguien con gran potencial no realizado'.", C_LAVENDER))

# Slide 9
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "APRENDIZAJE EN ACCIÓN", "La Metáfora de Lanzarse al Agua", "Aprender a nadar exige estar en el medio")
for i, (ctitle, cdesc, color) in enumerate([
    ("🏖️ Fuera del Agua (Teoría)", "En la orilla todo es planificación limpia y perfecta. Pero afuera NO estás aprendiendo a nadar.", C_TEAL),
    ("🌊 Dentro del Agua (Acción)", "Para aprender a nadar hay que lanzarse, sentir la densidad del agua, patalear y tragar agua.", C_PINK),
    ("🏊‍♀️ La Lección de Vida", "No se aprende a nadar mirando la piscina; la maestría se construye ejecutando adentro.", C_LAVENDER)
]):
    x = 70 + i * 395
    draw.rounded_rectangle([x, 220, x + 350, 600], radius=20, fill=C_CARD, outline=color, width=2)
    draw.text((x + 25, 260), ctitle, font=font_card_title, fill=C_WHITE)
    words = cdesc.split()
    cur, l_list = "", []
    for w in words:
        if len(cur + " " + w) > 26:
            l_list.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: l_list.append(cur)
    cy = 340
    for l in l_list:
        draw.text((x + 25, cy), l, font=font_card_body, fill=C_MUTED)
        cy += 32
draw_footer(draw, 9)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_9.png"))

# Slide 10
make_pattern(10, "DISCIPLINA vs. EMOCIÓN", "La Acción es Fría: Desmitificando la Motivación",
    ("📉 La Falacia de la Motivación", "Esperar 'sentir ganas' te paraliza porque la emoción previa es voluble e inestable.", C_PINK),
    ("🧊 La Acción es Neutra y Fría", "Accionar no requiere emoción previa; requiere decisión en automático sin pedir permiso a tu estado de ánimo.", C_TEAL),
    ("🏆 El Orden Real", "El orgullo, la satisfacción y la motivación vienen DESPUÉS de accionar, nunca antes.", C_LAVENDER))

# Slide 11
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "PNL & PRÁCTICA EN VIVO", "Ejercicio Práctico: De la Teoría a la Acción")
draw.rounded_rectangle([150, 230, 1130, 580], radius=24, fill=C_CARD, outline=C_TEAL, width=3)
draw.text((W//2, 340), "🧘‍♀️ Ejercicio Práctico del Club", font=font_title, fill=C_WHITE, anchor="mm")
draw.text((W//2, 420), "Guiado en vivo por Marbelis Montero", font=font_subtitle, fill=C_TEAL, anchor="mm")
draw_footer(draw, 11)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_11.png"))

# Slide 12
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "TRANSFORMACIÓN DE IDENTIDAD", "El Salto de Identidad y Compromiso")
draw.rounded_rectangle([70, 180, 610, 360], radius=18, fill=C_CARD, outline=C_LAVENDER, width=2)
draw.text((95, 210), "👤 Cambio de Postura", font=font_card_title, fill=C_LAVENDER)
draw.text((95, 255), "Dejar de identificarte como 'la que analiza/sana'", font=font_card_body, fill=C_WHITE)
draw.text((95, 290), "y encarnar a 'la persona que ejecuta hoy'.", font=font_card_body, fill=C_WHITE)
draw.rounded_rectangle([670, 180, 1210, 360], radius=18, fill=C_CARD, outline=C_PINK, width=2)
draw.text((695, 210), "🤝 Compromiso de 24 Horas", font=font_card_title, fill=C_PINK)
draw.text((695, 255), "Ejecutar tu acción mínima hoy antes de dormir", font=font_card_body, fill=C_WHITE)
draw.text((695, 290), "sin excusas y compartirla en la comunidad.", font=font_card_body, fill=C_WHITE)
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
    cy += 42
draw_footer(draw, 12)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_12.png"))

# Slide 13
img = Image.new("RGB", (W, H), C_BG)
draw = ImageDraw.Draw(img)
draw_header(draw, "COMUNIDAD EN VIVO", "Espacio de Preguntas, Reprogramación & Sesión 1 a 1 en Vivo")
draw.rounded_rectangle([250, 290, 1030, 430], radius=40, fill=(42, 210, 197, 40), outline=C_TEAL, width=3)
draw.text((W//2, 360), "⏸️ Pausamos la grabación para conversar", font=font_card_title, fill=C_TEAL, anchor="mm")
draw.text((W//2, 490), "Un espacio seguro, íntimo y totalmente privado para nuestra comunidad", font=font_subtitle, fill=C_LAVENDER, anchor="mm")
draw_footer(draw, 13)
img.save(os.path.join(ARTIFACT_DIR, "diapositiva_13.png"))

print("Generated diapositiva_1.png to diapositiva_13.png successfully!")

# Write artifact file using correct markdown syntax: ![caption](/C:/Users/...)
art_path = os.path.join(ARTIFACT_DIR, "diapositivas_clase_ep57_diseno.md")
md_lines = [
    "# 🎨 Carrusel de 13 Slides HD — Clase Sábado Episodio 57",
    "### Marbelis Montero · RealMente Club",
    "**Tema:** Tu vida no cambia cuando lo entiendes, cambia cuando lo ejecutas",
    "",
    "---",
    "",
    "## 🎠 Carrusel Interactivo HD",
    "",
    "````carousel"
]

for i in range(1, 14):
    p = f"/C:/Users/soyma/.gemini/antigravity/brain/d7d58a4c-2e8e-4b53-9cc8-4d992040c3ac/diapositiva_{i}.png"
    md_lines.append(f"![Diapositiva {i}]({p})")
    if i < 13:
        md_lines.append("<!-- slide -->")

md_lines.append("````")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 🖼️ Vista Individual HD de las Diapositivas")
md_lines.append("")

slide_titles = [
    "Portada Principal",
    "Frase de Apertura (Cita Gigante)",
    "El Encuadre (Saber vs. Hacer)",
    "El Mapa del Saboteo (Las 2 Trampas)",
    "Patrón 1: La Analista del Pasado",
    "Patrón 2: La Sanadora Eterna",
    "Patrón 3: La Esperadora del Momento Perfecto",
    "Patrón 4: La Protectora del Potencial",
    "La Metáfora de Nadar",
    "La Acción es Fría (Desmitificando la Motivación)",
    "Ejercicio Práctico en Vivo",
    "El Salto de Identidad y Compromiso",
    "Pausa de Grabación & Espacio Privado 1 a 1"
]

for i in range(1, 14):
    t = slide_titles[i-1]
    p = f"/C:/Users/soyma/.gemini/antigravity/brain/d7d58a4c-2e8e-4b53-9cc8-4d992040c3ac/diapositiva_{i}.png"
    md_lines.append(f"### Slide {i}: {t}")
    md_lines.append(f"![Diapositiva {i}]({p})")
    md_lines.append("")

with open(art_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("Artifact written with correct /C:/ paths!")
