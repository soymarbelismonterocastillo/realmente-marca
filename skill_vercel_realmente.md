# SKILL Y GUÍA MAESTRA DE DESPLIEGUE Y GESTIÓN EN VERCEL & AI GATEWAY - REALMENTE
**Creadora y Titular:** Marbelis Montero (@soymarbelismonterocastillo)

> **ESTE DOCUMENTO ES LA REFERENCIA OBLIGATORIA Y SKILL DE BUENAS PRÁCTICAS PARA LA ADMINISTRACIÓN DE PROYECTOS WEB INDEPENDIENTES, SERVICIOS SERVERLESS, REPOSITORIOS DEDICADOS EN GITHUB Y VERCEL AI GATEWAY EN EL ECOSISTEMA REALMENTE.**

---

## 🎯 1. REGLA MANDATORIA: 1 PROYECTO VERCEL = 1 REPOSITORIO GITHUB INDEPENDIENTE

Para garantizar escalabilidad, mantenibilidad, dominios independientes y un control de versiones limpio:

* **Arquitectura Modular e Independiente:** Cada aplicación web, test interactivo, presentación HTML, flyer promocional, herramienta o dashboard de RealMente **DEBE TENER SU PROPIO REPOSITORIO EN GITHUB** y su proyecto correspondiente en Vercel.
* **Prohibición de Repositorios Monolíticos Desordenados:** No se deben mezclar múltiples aplicaciones web ejecutables en un solo proyecto Vercel. Cada proyecto evoluciona y se actualiza de forma autónoma.
* **Vinculación CI/CD:** Al publicar commits en la rama `main` del repositorio específico en GitHub, Vercel desplegará automáticamente la nueva versión en tiempo real.

### Estándar de Nombres para Repositorios y Proyectos Vercel (`kebab-case`):
* `realmente-test-maslow` (App web del test interactivo de Maslow).
* `realmente-presentacion-ep59` (Diapositivas interactivas para la clase del Ep. 59).
* `realmente-flyer-expansion` (Landing page / flyer promocional de la charla).
* `realmente-saga-complacencia` (Dashboard de la estrategia de contenido).
* `realmente-carrusel-ep59` (Visualizador interactivo de carruseles).
* `realmente-marca` (Repositorio central de documentación y skills).

---

## 💡 2. PROTOCOLO OBLIGATORIO DE PROACTIVIDAD E INCENTIVO DE DESPLIEGUES

Dado que el titular de la marca se enfoca en la creación estratégica de contenidos, el asistente **DEBE SER PROACTIVO** en cada interacción:

1. **Sugerencia Automática al Crear Contenido:** Cada vez que se genere un archivo interactivo (`.html`, `.tsx`, `.js`, calculadora, test, mapa mental, presentación o flyer), el asistente **propondrá inmediatamente su despliegue en Vercel** creando un nuevo repositorio en GitHub.
2. **Incentivo de Ideas Innovadoras (Potencial Ilimitado):** El asistente sugerirá proactivamente conceptos de despliegue avanzados que aprovechen Vercel, como:
   * **Micro-SaaS & Herramientas del Club:** Generadores de afirmaciones con IA (usando Vercel AI Gateway), calculadoras de metas, diarios de introspección.
   * **Landing Pages Dinámicas:** Páginas de captura de leads con Analytics de Vercel y métricas en tiempo real.
   * **Web Apps de Episodios:** Reproductores interactivos de audio con transcripción sincronizada.
   * **Tarjetas Digitales e Invitaciones:** Páginas interactivas con animaciones glassmorphic y enlaces directos a WhatsApp/Club.
3. **Recordatorios de Actualización:** Si se modifica un test o presentación localmente, el asistente recordará sincronizar el repositorio correspondiente para actualizar la URL pública en Vercel.

---

## 🛡️ 3. PROTOCOLO ESTRICTO DE SEGURIDAD Y CREDENCIALES
* **Usuario Oficial Vercel:** `soymarbelismonterocastillo`
* **Correo Electrónico:** `soymarbelismontero@gmail.com`
* **Manejo de Tokens (`vck_...`):** Almacenados en `.vercel_config.json` y protegidos mediante `.gitignore`. NUNCA hardcodear en código fuente.

---

## 🤖 4. CONFIGURACIÓN Y USO DE VERCEL AI GATEWAY

Vercel AI Gateway es la infraestructura unificada para consumir modelos de Inteligencia Artificial (OpenAI, Gemini, Anthropic) de forma segura y centralizada.

### Endpoints Oficiales:
* **Base URL de AI Gateway:** `https://ai-gateway.vercel.sh/v1`
* **Autenticación OIDC Token URL:** `https://api.vercel.com/v1/ai/token`

---

## ⚙️ 5. COMANDOS DE AUTOMATIZACIÓN Y CREACIÓN DE PROYECTOS

### Pasos para Desplegar un Nuevo Proyecto Independiente:

1. **Crear Repositorio Dedicado en GitHub (`github_helper.py`):**
   ```bash
   python github_helper.py create-repo --name realmente-test-maslow --desc "Test Interactivo Maslow - RealMente Club"
   ```

2. **Subir Archivos del Proyecto (ej: `index.html`):**
   ```bash
   python github_helper.py upload --repo realmente-test-maslow --file test_maslow_interactivo.html --target index.html --message "feat: v1.0 test interactivo de Maslow"
   ```

3. **Conectar e Importar en Vercel (`vercel_helper.py`):**
   ```bash
   python vercel_helper.py create-project --name realmente-test-maslow
   ```

4. **Verificar Estado de Proyectos y Despliegues:**
   ```bash
   python vercel_helper.py status
   python vercel_helper.py list-projects
   ```

---

## 📌 6. CHECKLIST MAESTRO ANTES DE SUGERIR O DESPLEGAR
- [ ] ¿El activo web cuenta con su propio repositorio en GitHub con nombre `kebab-case`?
- [ ] ¿El archivo principal de la app fue nombrado `index.html` para despliegue automático e instantáneo en Vercel?
- [ ] ¿Se le informó al usuario la sugerencia de despliegue y su beneficio público/interactivo?
- [ ] ¿Se verificó que los tokens sensibles están seguros e ignorados en Git?
