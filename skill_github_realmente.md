# SKILL Y GUÍA MAESTRA DE GESTIÓN Y AUTOMATIZACIÓN EN GITHUB - REALMENTE
**Creadora y Titular:** Marbelis Montero (@soymarbelismonterocastillo)

> **ESTE DOCUMENTO ES LA REFERENCIA OBLIGATORIA Y SKILL DE BUENAS PRÁCTICAS PARA EL MANEJO, RESPALDO Y AUTOMATIZACIÓN DE PROYECTOS EN GITHUB.**

---

## 🛡️ 1. PROTOCOLO ESTRICTO DE SEGURIDAD Y CREDENCIALES
* **Usuario Oficial:** `soymarbelismonterocastillo`
* **Manejo de Tokens de Acceso Personal (PAT):**
  * NUNCA hardcodear o escribir el Token (`ghp_...`) directamente en repositorios públicos, archivos de código rastreados por Git ni en guiones compartidos.
  * Almacenar las credenciales de manera segura en un archivo local `.env` o `.github_config.json` en la raíz del espacio de trabajo.
  * **Regla Inflexible:** El archivo `.env` o `.github_config.json` DEBE estar registrado en `.gitignore` para evitar filtraciones accidentales.
* **Política de Erradicación de Fugas:** Si un token es expuesto públicamente por error en un commit, debe revocarse de inmediato desde los ajustes de seguridad de GitHub (`Settings > Developer Settings > Personal Access Tokens`).

---

## 📐 2. BUENAS PRÁCTICAS Y ESTÁNDARES EN GITHUB

### A. Nombres de Repositorios (Kebab-Case Naming)
* Usar minúsculas separadas por guiones cortos (`-`).
* Nombres descriptivos y claros según el ecosistema RealMente:
  * `realmente-marca` (Repositorio central de documentos de marca, skills y guías maestras).
  * `realmente-podcasts` (Guiones, transcripciones y audios/metadatos por episodio).
  * `realmente-club` (Recursos, tests interactivos HTML, diapositivas y clases).

### B. Convención de Commits Semánticos (Conventional Commits)
Cada actualización o subida de archivos debe ir acompañada de un mensaje de commit estructurado:
* `feat:` Nueva funcionalidad o recurso (ej: `feat: agregar test interactivo de Maslow en HTML`).
* `docs:` Actualización de documentación o skills (ej: `docs: actualizar skill de edición de podcast`).
* `fix:` Corregir un error de formato, enlace o script (ej: `fix: corregir ruta de estilos en diapositivas`).
* `style:` Cambios visuales o de diseño sin alterar lógica (ej: `style: ajustar paleta de colores a glassmorphic violeta`).
* `refactor:` Reestructuración de archivos o código sin cambiar funcionalidad.
* `chore:` Tareas de mantenimiento o respaldos automáticos (ej: `chore: respaldo periódico de contenidos`).

### C. Archivos Fundamentales Obligatorios por Repositorio
Todo repositorio oficial debe contener:
1. `README.md`: Documento de presentación en Markdown con título, descripción clara, autoría y cómo visualizar/usar los archivos.
2. `.gitignore`: Filtro de archivos temporales (`.env`, `*.log`, `__pycache__/`, etc.).
3. `LICENSE` / Nota de Derechos: Declaración clara de propiedad intelectal de Marbelis Montero.

---

## ⚙️ 3. AUTOMATIZACIÓN Y HERRAMIENTA DE ASISTENCIA (`github_helper.py`)
Dado que el entorno local opera mediante scripts y APIs en Python, se implementa la herramienta automatizada `github_helper.py` para interactuar con la API REST de GitHub usando el token autenticado.

### Comandos de Operación Rápida:
* **Verificar Autenticación y Estado:**
  ```bash
  python github_helper.py status
  ```
* **Crear un Nuevo Repositorio:**
  ```bash
  python github_helper.py create-repo --name realmente-marca --desc "Recursos y Skills Oficiales de RealMente"
  ```
* **Subir o Actualizar un Archivo:**
  ```bash
  python github_helper.py upload --repo realmente-marca --file skill_github_realmente.md --message "docs: agregar skill maestra de GitHub"
  ```
* **Sincronizar Múltiples Archivos / Respaldo Completo:**
  ```bash
  python github_helper.py sync-all --repo realmente-marca --message "chore: respaldo integral de archivos de marca"
  ```

---

## 📌 4. CHECKLIST MAESTRO ANTES DE PUBLICAR O SINCRONIZAR
- [ ] ¿Las credenciales y tokens están protegidos en `.env` / `.github_config.json` y excluidos por `.gitignore`?
- [ ] ¿El repositorio de destino tiene un nombre claro en minúsculas y separado por guiones (`kebab-case`)?
- [ ] ¿El mensaje de commit sigue el estándar semántico (`feat:`, `docs:`, `fix:`, `chore:`)?
- [ ] ¿Los archivos subidos mantienen la estética, tipografía y calidad oficial de la marca RealMente?
- [ ] ¿Se verificó la carga limpia y sin errores mediante `python github_helper.py status`?
