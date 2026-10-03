import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle

pdf_path = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\test_evaluacion_maslow.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Custom Palette
COLOR_PURPLE = colors.HexColor("#1e0d32")
COLOR_TURQUOISE = colors.HexColor("#008494")
COLOR_LILAC = colors.HexColor("#7e22ce")
COLOR_TEXT = colors.HexColor("#222222")
COLOR_BG_BOX = colors.HexColor("#f8f5ff")
COLOR_GOLD = colors.HexColor("#b45309")

style_title = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=COLOR_PURPLE,
    alignment=1,
    spaceAfter=6
)

style_subtitle = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=11,
    leading=14,
    textColor=COLOR_TURQUOISE,
    alignment=1,
    spaceAfter=15
)

style_quote = ParagraphStyle(
    'DocQuote',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=10,
    leading=14,
    textColor=COLOR_PURPLE,
    alignment=0,
    spaceAfter=10
)

style_instructions = ParagraphStyle(
    'DocInst',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13.5,
    textColor=COLOR_TEXT,
    spaceAfter=6
)

style_q_title = ParagraphStyle(
    'QTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=COLOR_PURPLE,
    spaceBefore=10,
    spaceAfter=6
)

style_opt = ParagraphStyle(
    'OptText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12.5,
    textColor=COLOR_TEXT,
    leftIndent=12,
    spaceAfter=4
)

style_sec_header = ParagraphStyle(
    'SecHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=17,
    textColor=COLOR_TURQUOISE,
    spaceBefore=16,
    spaceAfter=10
)

style_level_head = ParagraphStyle(
    'LevelHead',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=COLOR_GOLD,
    spaceBefore=8,
    spaceAfter=4
)

style_level_body = ParagraphStyle(
    'LevelBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=12.5,
    textColor=COLOR_TEXT,
    spaceAfter=6
)

story = []

# Title & Subtitle
story.append(Paragraph("<b>📋 TEST DE DIAGNÓSTICO: ¿DÓNDE ESTÁ TU ENERGÍA HOY?</b>", style_title))
story.append(Paragraph("<b>RealMente Club — Herramienta Exclusiva de Neuroalineación (Episodio 59)</b><br/>Por: Marbelis Montero (Master Trainer en PNL / RealMente Podcast)", style_subtitle))
story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_TURQUOISE, spaceAfter=12))

# Quote & Intro Box
quote_text = "<i>«Actuar desde la necesidad o la urgencia no es un fallo personal, es una respuesta biológica de tu cerebro priorizando un escalón no resuelto.»</i><br/><font color='#008494'><b>— Marbelis Montero (Episodio 59)</b></font>"
story.append(Paragraph(quote_text, style_quote))

inst_text = "<b>⏱️ INSTRUCCIONES (Responde en 2 minutos — Cero matemáticas):</b><br/>" \
            "1. <b>Responde en menos de 2 minutos:</b> Confía en lo primero que resuene en ti al leer cada opción.<br/>" \
            "2. <b>Respuesta espontánea:</b> Selecciona la opción que mejor describa tu realidad actual, sin juzgarte.<br/>" \
            "3. <b>Conteo simple:</b> Anota las letras (A, B, C, D o E). La letra que más repitas te revelará tu eslabón dominante al final."
story.append(Paragraph(inst_text, style_instructions))
story.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_LILAC, spaceAfter=10))

# 10 Questions
questions_data = [
    ("1. Si observas la mayor parte de tus pensamientos en un día normal, ¿hacia dónde se fuga tu atención de manera involuntaria?", [
        "<b>A)</b> Hacia mi cansancio físico: la falta de sueño reparador, el agotamiento acumulado o sentir que termino el día sin energía.",
        "<b>B)</b> Hacia mis recursos: la estabilidad económica, mi vivienda, el trabajo o cómo reducir la incertidumbre del futuro.",
        "<b>C)</b> Hacia mis lazos: mi pareja, la familia, mis amistades o la necesidad de sentirme acompañada e integrada en mi entorno.",
        "<b>D)</b> Hacia mi desempeño: si lo que hago es suficiente, cómo me perciben los demás o si estoy a la altura de lo que se espera de mí.",
        "<b>E)</b> Hacia mi propósito: si estoy viviendo la vida que realmente quiero, expresando mis talentos o creando algo con sentido."
    ]),
    ("2. Imagina que surge una situación de mucha presión o un imprevisto. ¿Cómo se manifiesta tu primera señal de alerta física o emocional?", [
        "<b>A)</b> Mi cuerpo somatiza de inmediato: contracturas musculares, dolor de cabeza, gastritis o un malestar físico puntual.",
        "<b>B)</b> Entro en modo control: reviso cuentas, presupuesto o busco proteger mi vivienda y mi estabilidad laboral.",
        "<b>C)</b> Busco a alguien cercano para desahogarme o me aíslo por miedo a distanciarme o molestar a mi entorno.",
        "<b>D)</b> Me juzgo duro: empiezo a dudar de mi capacidad, me comparo con otros o siento que cometí un error.",
        "<b>E)</b> Hago una pausa reflexiva: busco el aprendizaje de la situación y reoriento mis metas sin perder mi centro."
    ]),
    ("3. Si analizas tu bienestar biológico cotidiano, ¿en cuál de estos aspectos sientes que tu cuerpo te pide más atención?", [
        "<b>A)</b> En mi salud digestiva y visceral: regularizar mi tránsito intestinal, evitar la inflamación abdominal y sentirme liviana al comer.",
        "<b>B)</b> En mi entorno de vida: habitar un espacio seguro, sin caos doméstico, con certidumbre económica y paz en la pareja.",
        "<b>C)</b> En mis afectos: compartir momentos de calidad, risas y conversaciones francas con gente querida.",
        "<b>D)</b> En mi autoconfianza: reconocer lo que he logrado, dejar de buscar aprobación fuera y validar mi propio criterio.",
        "<b>E)</b> En mi crecimiento: dedicar tiempo a mis pasiones, aprender cosas fascinantes y expandir mi potencial."
    ]),
    ("4. Al momento de tomar una decisión importante en tu vida, ¿cuál es el filtro principal que pesa en tu balanza?", [
        "<b>A)</b> ¿Tengo la vitalidad física, la nutrición y la resistencia para asumir este compromiso sin descuidar mi salud?",
        "<b>B)</b> ¿Es una opción segura? ¿Protege mi vivienda, mis ingresos y la estabilidad de los míos?",
        "<b>C)</b> ¿Cómo afectará esto a mis relaciones cercanas? ¿Me mantendrá conectada con la gente que amo?",
        "<b>D)</b> ¿Esta decisión demuestra mi capacidad y me ayuda a consolidar mi autonomía y valor propio?",
        "<b>E)</b> ¿Esta decisión me permite ser fiel a quien realmente soy y desarrollar mis talentos únicos?"
    ]),
    ("5. Si pudieras regalarte un «estado de tranquilidad absoluta» para este momento de tu vida, ¿cuál elegirías?", [
        "<b>A)</b> Un cuerpo que funciona en armonía: sueño profundo, buena digestión, sin dolores ni diagnósticos médicos pendientes.",
        "<b>B)</b> Un entorno estable, con resguardo económico, vivienda segura y libertad de amenazas o incertidumbre.",
        "<b>C)</b> Relaciones nutricias en pareja, familia y amigos, donde me sienta aceptada, amada y parte de algo hermoso.",
        "<b>D)</b> Una autoestima inquebrantable, donde reconozca mis logros y deje de depender de cómo me perciben fuera.",
        "<b>E)</b> Sentido de vida pleno, donde cree libremente, aprenda y viva en coherencia con mis verdaderos valores."
    ]),
    ("6. Si observas la causa principal del «freno de mano» que a veces estanca tus proyectos o tu avance, ¿dónde se ubica?", [
        "<b>A)</b> En que postergo mi autocuidado: vivo ignorando señales de cansancio, malestares recurrentes o temas de salud por seguir cumpliendo.",
        "<b>B)</b> En la constante amenaza o incertidumbre sobre el futuro laboral, económico o habitacional.",
        "<b>C)</b> En la frialdad de la desconexión, la soledad o conflictos no resueltos con personas importantes para mí.",
        "<b>D)</b> En que me exijo demasiado para demostrar mi valor, cayendo en la comparación o la búsqueda de validación.",
        "<b>E)</b> En que estoy cumpliendo expectativas ajenas o viviendo en automático en lugar de desarrollar mi potencial."
    ]),
    ("7. Cuando decides hacer una pausa en tu rutina o dedicar tiempo para ti, ¿qué busca tu mente por necesidad?", [
        "<b>A)</b> Descanso y desconexión: soltar el esfuerzo físico, dormir sin alarmas y dejar que el cuerpo se recargue.",
        "<b>B)</b> Orden y previsibilidad: dejar la casa organizada, planificar presupuestos y asegurar que el entorno esté protegido.",
        "<b>C)</b> Nutrición afectiva: compartir una charla profunda, una comida compartida o un abrazo con gente que quiero.",
        "<b>D)</b> Crecimiento personal: estudiar un tema nuevo, leer o realizar actividades que refuercen mi autoconfianza.",
        "<b>E)</b> Expresión y creatividad: hacer arte, escribir, conectar con la naturaleza o planear proyectos con propósito."
    ]),
    ("8. Si le preguntas a tu círculo más cercano qué es lo que más te observan en esta etapa, ¿qué te dirían?", [
        "<b>A)</b> «Necesitas parar un poco: te ves agotada o con achaques físicos que necesitas atender de una vez.»",
        "<b>B)</b> «Estás muy enfocada en resolver la estabilidad, el dinero, el contrato o el orden de la vivienda.»",
        "<b>C)</b> «Estás buscando momentos de calidad para compartir, conectar y estar cerca de tu familia o pareja.»",
        "<b>D)</b> «Te cuesta festejar tus propios logros y a veces dudas demasiado de tu enorme capacidad.»",
        "<b>E)</b> «Te ves buscando un sentido más profundo, con ganas de crear y transformar tu vida.»"
    ]),
    ("9. Al mirar el uso que le das a tus inversiones personales (tiempo, dinero o energía), ¿cuál es la prioridad que predomina?", [
        "<b>A)</b> Tratamientos de salud, masajes, buena alimentación, suplementos o terapias para recuperar el cuerpo.",
        "<b>B)</b> Reforzar la seguridad del hogar, crear un ahorro de reserva o asegurar la estabilidad de la familia.",
        "<b>C)</b> Vivir experiencias compartidas: viajes con mi pareja o familia, festejos o actividades sociales.",
        "<b>D)</b> Cursos de crecimiento personal, certificaciones, mentorías o herramientas para fortalecer mi autoestima profesional.",
        "<b>E)</b> Financiar mi propio proyecto de vida, emprendimiento con propósito o iniciativas que trasciendan."
    ]),
    ("10. De las siguientes 5 preguntas de diagnóstico, ¿cuál es la que toca la fibra más sensible de tu momento presente?", [
        "<b>A)</b> «¿Mi cuerpo está recibiendo la salud, el descanso y la vitalidad que necesita, o estoy simplemente sobreviviendo?»",
        "<b>B)</b> «¿Siento que tengo una base estable, segura y protegida en mi vivienda y mis recursos para poder vivir en paz?»",
        "<b>C)</b> «¿Me siento conectada y parte de una familia/entorno afín, o estoy viviendo aislada o desconectada de los demás?»",
        "<b>D)</b> «¿Mi valor depende de mis logros y de la aprobación ajena, o reconozco mi propio valor con seguridad?»",
        "<b>E)</b> «¿Estoy viviendo desde quien realmente soy y desarrollando el máximo de mi potencial de vida?»"
    ])
]

story.append(Paragraph("<b>❓ LAS 10 PREGUNTAS DE DIAGNÓSTICO</b>", style_sec_header))

for q_title, opts in questions_data:
    story.append(Paragraph(f"<b>{q_title}</b>", style_q_title))
    for opt in opts:
        story.append(Paragraph(opt, style_opt))
    story.append(Spacer(1, 4))

story.append(HRFlowable(width="100%", thickness=1, color=COLOR_TURQUOISE, spaceBefore=10, spaceAfter=10))

# Results Section
story.append(Paragraph("<b>📊 RESULTADOS Y GUÍA COMPLETA DE LOS 5 ESLABONES</b>", style_sec_header))
story.append(Paragraph("Suma la cantidad de respuestas <b>A, B, C, D o E</b> que elegiste. La letra dominante determina tu eslabón de enfoque actual:", style_instructions))

levels_guide = [
    ("🔴 Mayoría de A — Nivel 1: Fisiología y Salud (Sobrevivir / Reconstrucción Biológica)",
     "<b>🧠 Diagnóstico Neurológico:</b> Tu sistema nervioso autónomo está operando con elevada carga de estrés o fatiga acumulada. Tu biología te está pidiendo atención real (sueño reparador, salud digestiva, aliviar somatizaciones).<br/>"
     "<b>🚨 El Freno de Mano Inconsciente:</b> Exigirte claridad mental o metas altas cuando no tienes energía física disponible es un acto de autoexigencia tóxica."),
    
    ("🟠 Mayoría de B — Nivel 2: Seguridad y Certeza (Piso Firme / Estabilidad)",
     "<b>🧠 Diagnóstico Neurológico:</b> Tu mente percibe inestabilidad económica, laboral o falta de previsibilidad en tu entorno de vida. Estás operando en hipervigilancia buscando certezas.<br/>"
     "<b>🚨 El Freno de Mano Inconsciente:</b> Confundir la prisa con la efectividad. Accionar desde la angustia material transmite necesidad y traba los resultados."),
    
    ("🟡 Mayoría de C — Nivel 3: Pertenencia y Afecto (Conexión Social / Vínculos)",
     "<b>🧠 Diagnóstico Neurológico:</b> Tu energía pide nutrir vínculos afectivos reales (pareja, familia, amistades). Tu cerebro busca calidez humana y cercanía.<br/>"
     "<b>🚨 El Freno de Mano Inconsciente:</b> Aislarte por miedo a molestar o sobredimensionar la desconexión afectiva."),
    
    ("🟢 Mayoría de D — Nivel 4: Estima y Valor Propio (Autonomía y Valía Personal)",
     "<b>🧠 Diagnóstico Neurológico:</b> Tienes la base resuelta, pero tu diálogo interno busca afianzar tu autoconfianza y validar tu propio criterio sin depender de la mirada ajena.<br/>"
     "<b>🚨 El Freno de Mano Inconsciente:</b> Dudar de tu capacidad antes de dar un paso o buscar aprobación externa para validar lo que ya sabes hacer."),
    
    ("🟣 Mayoría de E — Nivel 5: Autorrealización y Propósito (Completitud y Potencial)",
     "<b>🧠 Diagnóstico Neurológico:</b> Tu base está estable y resuelta. Tu energía busca libertad creativa, aprendizaje continuo, trascendencia e impacto genuino.<br/>"
     "<b>🚨 El Freno de Mano Inconsciente:</b> Postergar tu visión de vida por distraerte en la operatividad del día a día.")
]

for l_head, l_body in levels_guide:
    story.append(Paragraph(f"<b>{l_head}</b>", style_level_head))
    story.append(Paragraph(l_body, style_level_body))

story.append(HRFlowable(width="100%", thickness=1, color=COLOR_LILAC, spaceBefore=12, spaceAfter=10))

footer_text = "<i>«Recuerda: No necesitas tener resuelta toda la Pirámide de Maslow para activar tu Estado de Poder. Tu Estado de Poder se activa en el instante en que eliges quitar el freno del miedo y actuar con presencia soberana.»</i><br/><font color='#008494'><b>— Marbelis Montero (Master Trainer en PNL / RealMente Podcast)</b></font>"
story.append(Paragraph(footer_text, style_quote))

doc.build(story)
print("PDF GENERATED SUCCESSFULLY:", pdf_path)
