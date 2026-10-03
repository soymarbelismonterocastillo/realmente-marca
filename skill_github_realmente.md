# SKILL Y GUÍA MAESTRA DE GESTIÓN Y AUTOMATIZACIÓN EN GITHUB - REALMENTE
**Creadora y Titular:** Marbelis Montero (@soymarbelismonterocastillo)

> **ESTE DOCUMENTO ES LA REFERENCIA OBLIGATORIA Y SKILL DE BUENAS PRÁCTICAS PARA EL MANEJO, RESPALDO Y AUTOMATIZACIÓN DE PROYECTOS EN GITHUB.**

---

## 🛡️ 1. PROTOCOLO ESTRICTO DE SEGURIDAD Y CREDENCIALES
* **Usuario Oficial:** `soymarbelismonterocastillo`
* **Repositorio Oficial de Marca:** `realmente-marca`
* **Manejo de Tokens de Acceso Personal (PAT):**
  * NUNCA hardcodear o escribir el Token (`ghp_...`) directamente en repositorios públicos, archivos de código rastreados por Git ni en guiones compartidos.
  * Almacenar las credenciales de manera segura en un archivo local `.env` o `.github_config.json` en la raíz del espacio de trabajo.
  * **Regla Inflexible:** El archivo `.env` o `.github_config.json` DEBE estar registrado en `.gitignore` para evitar filtraciones accidentales.
* **Política de Erradicación de Fugas:** Si un token es expuesto públicamente por error en un commit, debe revocarse de inmediato desde los ajustes de seguridad de GitHub (`Settings > Developer Settings > Personal Access Tokens`).

---

## 🔄 2. RUTINA AUTOMÁTICA DE SINCRONIZACIÓN OBLIGATORIA
> ⚠️ **REGLA DE RUTINA DE AGENTE (OBLIGATORIA):**  
> Al finalizar cada sesión de trabajo o al realizar modificaciones relevantes en los contenidos (guiones de podcast, presentaciones HTML, archivos de redes sociales, tests PNL o scripts del proyecto), Antigravity **DEBE ejecutar automáticamente la sincronización completa** con el repositorio oficial `realmente-marca` en GitHub mediante la orden:
> ```bash
> python github_helper.py sync-project
> ```

---

## 📐 3. BUENAS PRÁCTICAS Y ESTÁNDARES EN GITHUB

### A. Nombres de Repositorios (Kebab-Case Naming)
* Usar minúsculas separadas por guiones cortos (`-`).
* Repositorio Central de Marca: `realmente-marca` (Repositorio principal que consolida todos los recursos, guiones, diapositivas y contenidos).

### B. Convención de Commits Semánticos (Conventional Commits)
Cada actualización o subida de archivos debe ir acompañada de un mensaje de commit estructurado:
* `feat:` Nueva funcionalidad, presentación HTML, recurso visual o test PNL (ej: `feat: agregar test interactivo de Maslow en HTML`).
* `docs:` Actualización de documentación, guiones o skills (ej: `docs: actualizar skill de edición de podcast`).
* `fix:` Corregir un error de formato, enlace o script (ej: `fix: corregir ruta de estilos en diapositivas`).
* `style:` Cambios visuales o de diseño sin alterar lógica (ej: `style: ajustar paleta de colores a glassmorphic violeta`).
* `refactor:` Reestructuración de archivos o código sin cambiar funcionalidad.
* `chore:` Tareas de mantenimiento o respaldos automáticos de rutina (ej: `chore: sincronización automática de contenidos`).

### C. Archivos Fundamentales Obligatorios por Repositorio
Todo repositorio oficial contiene:
1. `README.md`: Documento de presentación en Markdown con la paleta de colores, estructura del proyecto y créditos oficiales.
2. `.gitignore`: Filtro de archivos temporales (`.env`, `*.log`, `__pycache__/`, `desktop.ini`).
3. `github_helper.py`: Motor de automatización en Python para sincronización con la API de GitHub.

---

## ⚙️ 4. AUTOMATIZACIÓN Y COMANDOS DEL ASISTENTE (`github_helper.py`)

* **Verificar Autenticación y Lista de Repositorios:**
  ```bash
  python github_helper.py status
  ```
* **Sincronización Completa de Rutina del Proyecto:**
  ```bash
  python github_helper.py sync-project
  ```
* **Crear un Nuevo Repositorio Específico:**
  ```bash
  python github_helper.py create-repo --name realmente-podcasts --desc "Repositorio de audios y transcripciones"
  ```
* **Subir o Actualizar un Archivo Individual:**
  ```bash
  python github_helper.py upload --repo realmente-marca --file guion_episodio_59.md --message "docs: actualizar guion final ep 59"
  ```

---

## 📌 5. CHECKLIST MAESTRO DE VERIFICACIÓN DE RUTINA
- [ ] ¿Se ejecutó `python github_helper.py sync-project` al finalizar la sesión o los cambios?
- [ ] ¿Las credenciales y tokens están protegidos en `.env` / `.github_config.json` y excluidos por `.gitignore`?
- [ ] ¿Todos los archivos del proyecto mantienen la estructura oficial y mensajes semánticos?
- [ ] ¿Se confirmó la carga limpia en https://github.com/soymarbelismonterocastillo/realmente-marca?
