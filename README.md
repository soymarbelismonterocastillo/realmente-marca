# 🧠 RealMente - Repositorio Oficial de Marca y Recursos

**Creadora & Directora:** Marbelis Montero (Master Trainer en PNL / RealMente Club)  
**Usuario GitHub:** [@soymarbelismonterocastillo](https://github.com/soymarbelismonterocastillo)  
**Repositorio Central:** [realmente-marca](https://github.com/soymarbelismonterocastillo/realmente-marca)

Bienvenido al repositorio oficial del ecosistema **RealMente**. Aquí se almacenan, organizan y respaldan todos los recursos estratégicos, guiones de podcast, transcripciones oficiales, presentaciones interactivas, evaluaciones PNL, contenido para redes sociales y skills maestras de marca.

---

## 📚 Estructura del Ecosistema

```
MARCA/
├── 📄 README.md                        # Presentación oficial del repositorio
├── 🤖 .agents/skills/                  # Skills oficiales de Antigravity (IA)
│   ├── carretes-instagram-realmente/
│   ├── edicion-podcast-realmente/
│   ├── frase-inicio-semana-realmente/
│   ├── github-realmente/
│   └── historias-instagram-realmente/
├── 🛡️ skill_github_realmente.md        # Skill y guía de sincronización en GitHub
├── 🎨 skill_carretes_instagram_realmente.md
├── 🎙️ skill_edicion_podcast_realmente.md
├── 📋 registro_episodios_realmente.md   # Catálogo maestro de episodios (59, 60, 61...)
├── 🐍 github_helper.py                # Asistente de sincronización bidireccional en Python
├── 📂 Episodios/                       # Guiones, transcripciones y materiales por episodio
│   ├── EP59_Necesidad_vs_Poder/
│   ├── EP60_Decision_y_Evasion/
│   └── EP61_Esfuerzo_e_Identidad/
├── 📂 Redes_Sociales/                  # Lluvia de ideas, carruseles, reels y contenidos
├── 📂 Realmente_Club/                  # Material exclusivo para miembros del club
└── 🌐 Presentations & Interactive HTML # Diapositivas 16:9 y Tests PNL Interactivos
```

---

## 🎨 Paleta de Colores Oficial de Marca

| Elemento | Color | Código Hex |
| :--- | :--- | :--- |
| **Fondo Principal** | Morado Oscuro Berenjena | `#12091c` - `#1e0d32` |
| **Acento Principal** | Turquesa brillante | `#00f2fe` / `#2ad2c5` |
| **Acento Secundario** | Lila Claro / Violeta Suave | `#d8b4fe` / `#c084fc` |
| **Texto Principal** | Blanco Lavanda | `#f5f3ff` |
| **Tarjetas** | Glassmorphism Transparente | `rgba(30, 15, 48, 0.85)` |

---

## 🛠️ Automatización y Sincronización Bidireccional

Este repositorio cuenta con sincronización automática mediante **`github_helper.py`**, permitiendo mantener una copia de seguridad exacta del espacio de trabajo y sincronizar cambios remotos:

* **Sincronización Bidireccional Completa:**
  ```bash
  python github_helper.py sync --repo realmente-marca
  ```
* **Respaldo Local -> GitHub (Push):**
  ```bash
  python github_helper.py push --repo realmente-marca
  ```
* **Descarga de Cambios GitHub -> Local (Pull):**
  ```bash
  python github_helper.py pull --repo realmente-marca
  ```

---

*© RealMente por Marbelis Montero. Todos los derechos reservados.*
