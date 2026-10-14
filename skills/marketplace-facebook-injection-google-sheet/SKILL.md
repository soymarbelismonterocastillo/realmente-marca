# 🛒 Skill: Marketplace Facebook Injection to Google Sheet

Esta skill documenta el proceso específico para inyectar datos de publicaciones locales de Facebook Marketplace en el Spreadsheet de gestión de **Trenzas Sheshi**. 

> [!IMPORTANT]
> Este flujo es **específico para este proyecto**. Depende del acceso al Google Workspace CLI (gws) con los tokens correspondientes y del acceso a las carpetas de Drive indicadas.

## 📍 Configuración del Entorno (Mis Datos)
- **Spreadsheet ID:** `1fU-WipohJpqGX6oz1RMfUznarbf8_BcFbmNOknZtvJI`
- **Hoja de Destino:** `marketplace-publicaciones-pendientes`
- **Raíz de Drive (Marketplace):** `1EY2-W6HNfwM0ZA9ElBH15YuavYBDEWKt`
- **Categoría Default:** `Salud y belleza` (Apropiado para servicios de trenzas).

## 🔄 Proceso de Replicación

### 1. Lectura y Limpieza de Metadata Local
Acceder a la subcarpeta en `entrega/marketplace/`.
- El archivo `copy.md` contiene el **Título**, **Precio** y **Descripción**.
- **Limpieza Meta-Friendly:** 
    - Eliminar formato de negrita (`**`) de todos los campos.
    - Descartar la sección interactiva `📸 Imágenes Recomendadas` (solo para uso interno).
- El precio debe cargarse como número puro (ej: `160000` en lugar de `$160.000`).

### 2. Mapeo con Google Drive
Encontrar la carpeta equivalente por nombre en la raíz de Drive (`1EY2...`).
- Obtener los IDs únicos (`fileId`) de las imágenes contenidas en la carpeta.
- **Nota:** Solo usar las imágenes que existan (algunas tienen 2, otras 3).

### 3. Preparación de Enlaces Públicos
Para que el sistema de automatización (n8n u otros) pueda descargar las imágenes, se debe habilitar el acceso público:
`gws drive permissions create --params '{"fileId": "ID"}' --json '{"role": "reader", "type": "anyone"}'`

### 4. Inyección en Google Sheets
Constructir la fila y ejecutar el comando de actualización.
- **Estructura de Fila:** `[titulo, precio, descripcion, categoria, img1_url, img2_url, img3_url, estado, publicado_el]`
- **Formato URL:** `https://drive.google.com/uc?export=download&id=ID_DE_DRIVE`

## 💡 Guía de Operación
Siempre que se pida "inyectar" o "completar" el sheet desde las carpetas locales, seguir este patrón para asegurar que los enlaces de Drive sean persistentes y públicos.
