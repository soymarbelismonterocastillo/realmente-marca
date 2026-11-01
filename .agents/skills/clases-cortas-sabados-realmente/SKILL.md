---
name: clases-cortas-sabados-realmente
description: >-
  Metodología pedagógica, diseño visual y directrices de facilitación para conceptualizar, estructurar y programar clases en vivo ágiles y resumidas de los sábados de RealMente Club (Marbelis Montero). Define una arquitectura compacta de 7 a 8 diapositivas en formato 16:9 con paleta morado berenjena y turquesa, protagonismo verbal total de la facilitadora, ilustración visual literal central (ej. metáfora de la mesa de 4 patas rotulada), desglose conceptual, resultado del instrumento/test, lámina ultra minimalista de ejercicio práctico (solo el título), frases de apertura y cierre de alto impacto, incrustación de imágenes en Base64 y protocolo de entrega directa en Google Drive y Escritorio de Windows.
---

# 🎓 Skill Oficial: Clases Cortas y Ágiles de los Sábados — RealMente Club
**Docente y Creadora:** Marbelis Montero (Master Trainer en PNL y Especialista en Neuroalineación)  
**Contexto:** Clases magistrales y mentoría en vivo de formato resumido y dinámico para *RealMente Club*, diseñadas para que Marbelis tenga el protagonismo verbal completo («hablar más ella y fluir con el momento»), usando las diapositivas como apoyo visual limpio sin sobrecarga de texto.

---

## 🧭 1. PRINCIPIOS PEDAGÓGICOS Y DIRECTRICES INNEGOCIABLES

### 1. Formato Ágil y Conducción Verbal Libre (Cero Sobrecarga)
* A diferencia del formato de clase larga (11 láminas con comparativas y filtros extensos), el formato **Clase Corta** se enfoca en **7 u 8 láminas esenciales**.
* ⛔ **PROHIBIDO:** 
  * Diapositivas cargadas de párrafos, listas de pasos o instrucciones para la facilitadora.
  * Duplicar conceptos o explicaciones teóricas complejas.
* ✅ **OBLIGATORIO:**
  * La pantalla es un anclaje visual limpio; Marbelis desarrolla, explica y profundiza verbalmente.
  * La lámina de ejercicio debe ser **ultra minimalista**: lleva **únicamente el título** (ej. `# Ejercicio práctico`), sin instrucciones escritas para que ella conduzca el trabajo en libreta en vivo.

### 2. Ilustración Visual Literal Central
* Cuando el episodio o tema se apoya en una metáfora diagnóstica (como *La Mesa de 4 Patas de la Culpa*):
  * Se debe incluir un **dibujo o render literal realista y estilizado** del objeto (ej. mesa de madera real con su tablero y sus 4 patas bien definidas sobre el fondo de la marca).
  * El concepto macro se rotula en grande en el objeto (ej. `CULPA - La Superficie del Juicio Moral`).
  * Cada elemento o pata lleva su indicador nítido apuntando directamente al punto físico (ej. `Pata 1: Lo «Bueno»`, `Pata 2: Lo «Malo»`, `Pata 3: La Víctima`, `Pata 4: La Victimaria`).
  * Inmediatamente después va la lámina de desglose o profundización con tarjetas limpias.

### 3. Conexión Inmediata con el Instrumento Semanal
* Una de las diapositivas centrales debe mostrar los **resultados del instrumento de autoevaluación / termómetro** completado por las socias en su libreta.
* Presenta los 4 niveles con sus rangos de puntaje exactos y nombres de identidad (ej. 17-21 pts, 12-16 pts, 6-11 pts, 0-5 pts) para que la socia ubique su nivel en pantalla al instante.

### 4. Frases Protagonistas de Apertura y Cierre
* **Frase de Apertura (Slide 2):** Cita contundente de quiebre y movimiento que rompe la inercia mental de entrada.
* **Frase de Cierre (Penúltima Slide):** Cita de anclaje, soberanía y permiso para el siguiente nivel.
* Ambas van en láminas exclusivas con formato tipográfico editorial (*Playfair Display* cursiva).

---

## 📐 2. ARQUITECTURA NARRATIVA DE CLASE CORTA (7 U 8 SLIDES)

```
[SLIDE 1] ➔ Portada Oficial (Título exacto del Episodio + RealMente Club + Con Marbelis Montero)
[SLIDE 2] ➔ Frase de Apertura (Cita contundente de quiebre y movimiento)
[SLIDE 3] ➔ Ilustración Literal de la Metáfora Central (Render/Dibujo con rótulos directos)
[SLIDE 4] ➔ Explicación / Desglose de los Elementos (Tarjetas limpias de profundización)
[SLIDE 5] ➔ Resultado del Instrumento Semanal (Niveles y puntajes de la autoevaluación)
[SLIDE 6] ➔ Ejercicio Práctico (ULTRA MINIMALISTA: Solo el título «# Ejercicio práctico»)
[SLIDE 7] ➔ Frase de Cierre (Cita de anclaje, soberanía y evolución)
[SLIDE 8] ➔ Mentoría en Vivo y Preguntas (Cierre con micrófonos y chat abiertos)
```
*(Nota: Si no hay lámina de desglose separada, el mazo se compacta en 7 láminas exactas).*

---

## 🎨 3. IDENTIDAD VISUAL Y ESPECIFICACIONES TÉCNICAS

* **Fondo Principal (Modo Oscuro):** Degradado Violeta Berenjena Profundo (`#12091c` a `#1e0d32` a 135°).
* **Fondo Modo Claro (Lavender Soft):** `#faf5ff` a `#e9d5ff`.
* **Acento Primario:** Turquesa brillante (`#00f2fe`).
* **Acento Secundario:** Lila Claro (`#d8b4fe`).
* **Texto Principal:** Blanco Lavanda (`#f5f3ff`).
* **Alertas / Inacción:** Rosa Carmesí (`#fb7185`).
* **Legibilidad Zoom (+2 Puntos Obligatorio):**
  * Títulos: `2.25rem` a `2.5rem` (*Playfair Display*).
  * Subtítulos: `1.25rem` a `1.35rem`.
  * Citas: `1.95rem` (*Playfair Display* cursiva).
  * Texto en tarjetas y párrafos: `1.08rem` a `1.18rem` con `line-height: 1.45 - 1.50`.
  * Título minimalista de ejercicio: `3.6rem` a `3.8rem`.
* **Aspect Ratio Fijo:** Formato panorámico 16:9 (`aspect-ratio: 16 / 9; max-width: 1040px`).
* **Incrustación de Imágenes en Base64:**
  * Para evitar errores de carga en el protocolo `file:///`, caché de navegadores o rutas relativas, toda imagen protagónica debe incrustarse como `data:image/png;base64,...` directamente en el código HTML.
* **Controles Integrados:** Botones Anterior/Siguiente, flechas laterales (`‹` / `›`), contador dinámico (`Slide X / 8`), atajos de teclado (`←`, `→`, espacio), pantalla completa y modo oscuro/claro.

---

## 🔄 4. PROTOCOLO DE SINCRONIZACIÓN Y DESPLIEGUE FINAL

Al finalizar cualquier clase de este formato, ejecutar automáticamente el protocolo completo:

1. **Guardar en 2 ubicaciones del Workspace:**
   * Raíz: `presentacion_episodio_XX.html`
   * Carpeta del episodio: `Episodios/EPXX_.../04_Club_Ejercicio_y_Diapositivas/presentacion_episodio_XX.html`
2. **Generar Capturas de Alta Resolución con Playwright:**
   * Renderizar capturas PNG de cada una de las diapositivas (`slide_01.png` a `slide_08.png`).
   * Guardar en la carpeta `previews/` del episodio y copiar a la carpeta de artefactos de Antigravity.
3. **Crear y Actualizar el Artefacto Visual:**
   * Crear/actualizar `visual_presentacion_epXX.md` con un `carousel` para que Marbelis revise la presentación diapositiva por diapositiva en el panel lateral sin ver código.
4. **Sincronización Automática con Google Drive:**
   * Copiar a `G:\Mi unidad\MARCA\Realmente_Club\` con nombre oficial:  
     `Presentacion_Clase_Sabado_EPXX_Marbelis_Montero.html`.
   * Copiar a `G:\Mi unidad\MARCA\Episodios\EPXX_...\04_Club_Ejercicio_y_Diapositivas\`.
   * Copiar a `G:\Mi unidad\MARCA\Podcast_Club\EPXX_...\04_Club_Ejercicio_y_Diapositivas\`.
5. **Accesos Directos en el Escritorio de Windows:**
   * Crear en `C:\Users\soyma\Desktop\` y `C:\Users\soyma\OneDrive\Desktop\`:
     * `CLASE_SABADO_EPXX.html` (archivo directo).
     * `CLASE_SABADO_EPXX.url` (acceso directo al navegador).
     * `ABRIR_CLASE_SABADO_EPXX.bat` (lanzador en 1 clic).
6. **Apertura Inmediata en Navegador:**
   * Lanzar el archivo en el navegador predeterminado para que quede listo en pantalla para la socia.
