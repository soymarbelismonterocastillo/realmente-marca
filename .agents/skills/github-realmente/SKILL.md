---
name: github-realmente
description: >-
  Protocolo de sincronización, respaldo exacto bidireccional y automatización en GitHub para el ecosistema RealMente de Marbelis Montero. Establece la política de respaldo continuo del espacio de trabajo local (workspace) hacia el repositorio 'realmente-marca', la verificación de cambios remotos para actualización local y la protección estricta de credenciales y variables de entorno.
---

# 🐙 Skill Oficial: Gestión, Respaldo y Sincronización en GitHub — RealMente
**Titular y Creadora:** Marbelis Montero (@soymarbelismonterocastillo)  
**Repositorio Central de Marca:** `https://github.com/soymarbelismonterocastillo/realmente-marca`

Esta skill rige los protocolos técnicos y operativos para garantizar que el repositorio de GitHub sea siempre un **espejo exacto y copia de seguridad íntegra** del espacio de trabajo local de RealMente, así como la sincronización inmediata de cualquier cambio realizado remotamente hacia el entorno local.

---

## 🎯 1. Filosofía de Respaldo y Sincronización Continua

1. **Copia de Seguridad Permanente en GitHub:**
   * Cada vez que se culmine un episodio nuevo (guion, escaleta, transcripción, presentación, carruseles, reels, skills), se debe ejecutar el respaldo hacia GitHub (`realmente-marca`).
   * Ningún activo (código, documentos markdown, imágenes, HTML interactivos, skills) debe quedar huérfano fuera de GitHub.

2. **Sincronización Bidireccional (GitHub <-> Workspace Local):**
   * **GitHub -> Local (Pull):** Si se subieron cambios directamente en GitHub (o desde otro equipo/colaborador), se descargan e integran al proyecto local sin sobreescribir modificaciones locales más recientes.
   * **Local -> GitHub (Push):** Cualquier archivo nuevo o modificado localmente se detecta automáticamente mediante cálculo de hashes Git Blob (SHA-1) y se sube con commits semánticos.

---

## 🛡️ 2. Seguridad y Protección de Credenciales

* **Archivos Estrictamente Ignorados (`.gitignore`):**
  * `.github_config.json` (contiene el token personal `ghp_...`).
  * `.vercel_config.json` y carpetas `.vercel/`.
  * Archivos `.env`.
  * Archivos de sistema operativo (`desktop.ini`, `Thumbs.db`, `.DS_Store`).
  * Archivos temporales de Python (`__pycache__/`, `*.pyc`).
* **Principio:** Las credenciales NUNCA se suben al repositorio bajo ninguna circunstancia.

---

## ⚙️ 3. Comandos Oficiales con `github_helper.py`

El asistente automatizado `github_helper.py` opera directamente con la API REST de GitHub para máxima velocidad y fiabilidad:

### A. Sincronización Bidireccional Completa (Recomendado)
Descarga primero lo nuevo de GitHub y luego sube todas las modificaciones locales:
```bash
python github_helper.py sync --repo realmente-marca
```

### B. Respaldo Completo Local -> GitHub (Push)
Detecta archivos nuevos o modificados en el workspace y genera la copia exacta en GitHub:
```bash
python github_helper.py push --repo realmente-marca
```

### C. Descarga de Cambios GitHub -> Local (Pull)
Descarga archivos creados o actualizados en GitHub que no existan o sean más recientes:
```bash
python github_helper.py pull --repo realmente-marca
```

### D. Verificación de Estado y Repositorios
Comprueba la conexión con la cuenta `@soymarbelismonterocastillo` y muestra los repositorios:
```bash
python github_helper.py status
```

---

## 🏷️ 4. Estándar de Commits Semánticos

Cada archivo subido recibe automáticamente una etiqueta de acuerdo a su naturaleza:
* `docs:` Documentos Markdown, guiones, escaletas, transcripciones y skills (`.agents/skills/`, `skill_*.md`, `.md`).
* `feat:` Páginas interactivas, carruseles web, presentaciones, flyers, mapas mentales e imágenes (`.html`, `.png`, `.jpg`, `.pdf`).
* `chore:` Scripts auxiliares, configuraciones, listas o sincronización general (`.py`, `.json`, `.csv`).

---

## 📐 5. Arquitectura de Repositorios (1 Activo Web = 1 Repositorio)

Cuando se crea una aplicación web independiente (desplegable en Vercel como un test interactivo o una calculadora):
1. Crear repositorio dedicado:
   ```bash
   python github_helper.py create-repo --name realmente-nombre-app --desc "Descripción"
   ```
2. Subir el archivo principal como `index.html`:
   ```bash
   python github_helper.py upload --repo realmente-nombre-app --file mi_archivo.html --target index.html
   ```
3. Todo el resto de la base de conocimiento y contenidos generales reside siempre en `realmente-marca`.
