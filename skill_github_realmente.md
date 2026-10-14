# SKILL Y GUÍA MAESTRA DE GESTIÓN, RESPALDO Y SINCRONIZACIÓN EN GITHUB - REALMENTE
**Creadora y Titular:** Marbelis Montero (@soymarbelismonterocastillo)  
**Repositorio Central:** `https://github.com/soymarbelismonterocastillo/realmente-marca`

> **ESTE DOCUMENTO ES LA REFERENCIA OBLIGATORIA Y SKILL DE BUENAS PRÁCTICAS PARA EL MANEJO, RESPALDO EXACTO, SINCRONIZACIÓN BIDIRECCIONAL Y AUTOMATIZACIÓN EN GITHUB.**

---

## 🎯 1. REGLA FUNDAMENTAL DE RESPALDO Y SINCRONIZACIÓN CONTINUA

1. **GitHub como Espejo de Respaldo Exacto:**
   * El repositorio `realmente-marca` debe contener una copia fiel, exacta y completa de todos los archivos y recursos del espacio de trabajo local (documentos, imágenes, scripts, guiones, episodios y skills).
   * Cada vez que se culmine una sesión de trabajo o un episodio, se realiza la sincronización con GitHub.

2. **Sincronización Bidireccional (GitHub <-> Workspace Local):**
   * **GitHub -> Local (Pull):** Si hay archivos nuevos o editados en GitHub, se descargan al entorno local.
   * **Local -> GitHub (Push):** Todos los archivos locales creados o modificados se detectan mediante Git Blob SHA-1 y se respaldan en GitHub.

---

## 🛡️ 2. PROTOCOLO ESTRICTO DE SEGURIDAD Y CREDENCIALES

* **Usuario Oficial:** `soymarbelismonterocastillo`
* **Manejo de Tokens de Acceso Personal (PAT):**
  * NUNCA hardcodear ni subir el Token (`ghp_...`) al repositorio público.
  * Almacenar en `.github_config.json` en la raíz del espacio de trabajo local.
  * Excluir siempre en `.gitignore`.

---

## ⚙️ 3. AUTOMATIZACIÓN CON `github_helper.py`

### Comandos Principales:

* **Sincronización Bidireccional Completa (Pull + Push):**
  ```bash
  python github_helper.py sync --repo realmente-marca
  ```

* **Respaldo Completo Local -> GitHub (Push):**
  ```bash
  python github_helper.py push --repo realmente-marca
  ```

* **Descarga de Cambios GitHub -> Local (Pull):**
  ```bash
  python github_helper.py pull --repo realmente-marca
  ```

* **Verificar Conexión y Repositorios:**
  ```bash
  python github_helper.py status
  ```

* **Crear un Repositorio Dedicado (para despliegues en Vercel):**
  ```bash
  python github_helper.py create-repo --name realmente-app --desc "Descripción"
  ```

* **Subir un Archivo Específico:**
  ```bash
  python github_helper.py upload --repo realmente-app --file index.html
  ```

* **Invitar a un Colaborador:**
  ```bash
  python github_helper.py add-collaborator --repo realmente-marca --user usuario_github --permission push
  ```

---

## 🏷️ 4. CONVENCIÓN DE COMMITS SEMÁNTICOS
* `feat:` Nuevos recursos visuales, carruseles, presentaciones interactivas, flyers o imágenes (`.html`, `.png`, `.jpg`, `.pdf`).
* `docs:` Actualización de guiones, escaletas, transcripciones, registro de episodios y skills (`.md`, `.agents/skills/`).
* `chore:` Mantenimiento de scripts, sincronización general o dependencias (`.py`, `.json`, `.csv`).

---

## 📌 5. CHECKLIST DE SINCRONIZACIÓN
- [ ] ¿El repositorio en GitHub refleja fielmente todos los episodios y recursos del workspace local?
- [ ] ¿Están excluidos del commit los archivos sensibles (`.env`, `.github_config.json`, `.vercel_config.json`)?
- [ ] ¿Se ejecutó `python github_helper.py sync` para garantizar respaldo bidireccional?
