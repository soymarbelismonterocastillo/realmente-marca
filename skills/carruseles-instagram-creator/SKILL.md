---
name: ai-carousel-generation
description: >
  Instrucciones para generar carruseles de Instagram cohesivos usando generación de imágenes por IA, integrando elementos fotográficos con formas gráficas y tipografía específicas de la marca.
---

# AI Carousel Generation Skill

Esta skill define el flujo de trabajo para crear carruseles de Instagram altamente visuales y fotográficos utilizando herramientas de generación de imágenes por IA (como la herramienta `generate_image` de Antigravity).

## Filosofía Principal

1. **Enfoque "Imagen Primero"**: El diseño debe priorizar la fotografía realista de alta calidad (ej. del servicio, cliente ideal, resultados) integrada orgánicamente con los elementos gráficos de la marca.
2. **Consistencia de Marca Estricta**: Cada slide *debe* adherirse rigurosamente a las pautas de marca del cliente (paleta de colores, formas, estilo tipográfico).
3. **Flujo Continuo (Seamless)**: La transición entre slides debe sentirse cohesiva, compartiendo marcos de fondo similares o elementos continuos.
4. **Control de Versiones**: Siempre guardar nuevos experimentos de estilo como archivos de preview nuevos (ej. `[nombre]_preview_v2.md`) para permitir al usuario comparar opciones ("A/B testing visual").

## Flujo de Trabajo (Workflow)

### 1. Recopilación de Contexto
Antes de generar cualquier imagen, el agente DEBE:
- **Buscar de forma proactiva** si existe algún archivo de "Brand Guidelines", "Brandbook" o lineamientos de marca en el proyecto actual. Si se encuentra, utilizar esa información de inmediato. De lo contrario, **preguntar al usuario** por el nombre de su marca y sus lineamientos visuales (colores, estilo, tipografía) o solicitarle que indique la ruta a su documento. **NUNCA asumir el nombre de la marca ni utilizar colores o estilos predeterminados sin antes confirmarlos o leerlos de un documento oficial.**
- Leer el contenido fuente (el archivo markdown con el copy slide por slide).
- Extraer los colores exactos, el estilo visual (ej. "boho chic", "minimalista corporativo") y las preferencias tipográficas basándose **exclusivamente** en la información o el documento proporcionado por el usuario. *Nunca adivinar estos datos.*

### 2. Estructura del Prompt (Prompt Engineering)
Construir el prompt de generación de imagen utilizando esta estructura exacta:

> A professional vertical Instagram carousel slide (aspect ratio 4:5). 
> **Visual Style**: [Describir el elemento fotográfico para este slide, ej. 'A high-quality close-up photograph of a woman smiling with braids']. The photo is beautifully integrated with [Describir el estilo gráfico de la marca, ej. 'minimalist boho chic graphic elements']. 
> **Colors**: The background and graphic overlays feature a brand color palette of [Insertar colores exactos del Brand Guideline, ej. 'light pastel pink, soft beige, and hot pink abstract organic blob shapes']. 
> **Typography**: Extremely clear, modern, bold text overlaid perfectly spelling exactly '[Título Principal]'. Below it, smaller elegant text spelling perfectly exactly '[Subtítulo/Texto Secundario]'. High-end, cohesive carousel aesthetic.

*REGLA CRÍTICA DE TEXTO*: Nunca incluir palabras literales como "Title:" o "Subtitle:" en el texto a generar. Instruir a la IA a escribir *estrictamente* las palabras deseadas.

### 3. Reglas de Contenido
- **Llamados a la Acción (CTAs)**: Los CTAs deben ser directos y neutrales respecto a la plataforma (para que sirvan en Instagram, Facebook, etc.). Ej: *Escribime la palabra [PALABRA] por mensaje privado y te lo mando*. Nunca incluir nombres de plataformas como WhatsApp o "al link de mi bio" dentro del diseño gráfico de la imagen.
- **Redes Sociales**: No incluir el `@usuario` dentro del diseño gráfico del carrusel, ya que resulta redundante al publicarse en la misma cuenta.

### 4. Ejecución y Control de Versiones (Preview)
- Generar todos los slides de un **solo carrusel** como lote de prueba inicial.
- Embeber las imágenes generadas en un archivo markdown de previsualización (ej. `[nombre_carrusel]_preview_v1.md`) usando el componente de markdown `carousel` para que el usuario pueda deslizar y revisar.
- Si se solicitan cambios de estilo, generar un archivo `_v2.md`.
- Solicitar validación explícita del usuario antes de proceder a generar el resto de los carruseles (bulk generation).
