$backupDir = 'C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Respaldo_Escritorio_20261105'
$flyerDir = 'C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\04_Lead_Magnets\Flyer_Arraial'

New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
New-Item -ItemType Directory -Force -Path $flyerDir | Out-Null

$itemsToBackup = @(
    'C:\Users\soyma\Desktop\Contenido_Flyer_Marbelis_Montero.docx',
    'C:\Users\soyma\OneDrive\Desktop\DOCUMENTO_OFICIAL_FLYER_MARBELIS_MONTERO.pdf',
    'C:\Users\soyma\OneDrive\Desktop\documento_flyer_arraial.html',
    'C:\Users\soyma\OneDrive\Desktop\contenido_flyer_arraial.txt',
    'C:\Users\soyma\OneDrive\Desktop\test_evaluacion_maslow.pdf',
    'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_EPISODIO_64_OPCION_B.md',
    'C:\Users\soyma\Desktop\ESQUEMA_EPISODIO_64.md',
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_64_OPCION_B.html',
    'C:\Users\soyma\Desktop\PRESENTACION_EPISODIO_64.html',
    'C:\Users\soyma\Desktop\PRESENTACION_EPISODIO_64.url',
    'C:\Users\soyma\Desktop\GUIA_GRABACION_EP64.url',
    'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_EPISODIO_65.md',
    'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_EPISODIO_65_OPCION_B.md',
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_65.html',
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_65.url',
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_65_OPCION_B.html',
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_65_OPCION_B.url',
    'C:\Users\soyma\Desktop\PRESENTACION_EPISODIO_65.html',
    'C:\Users\soyma\Desktop\PRESENTACION_EPISODIO_65.url',
    'C:\Users\soyma\OneDrive\Desktop\miniatura_ep64.png',
    'C:\Users\soyma\OneDrive\Desktop\MINIATURA_EPISODIO_64_YOUTUBE.png',
    'C:\Users\soyma\OneDrive\Desktop\MINIATURA_YOUTUBE_EPISODIO_64.png',
    'C:\Users\soyma\Desktop\miniatura_ep64.png',
    'C:\Users\soyma\Desktop\MINIATURA_EPISODIO_64_YOUTUBE.png',
    'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_EPISODIO_66.md',
    'C:\Users\soyma\Desktop\ESQUEMA_EPISODIO_66.md',
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_66.html',
    'C:\Users\soyma\Desktop\PRESENTACION_EPISODIO_66.html'
)

foreach ($filePath in $itemsToBackup) {
    if (Test-Path $filePath) {
        Copy-Item -Path $filePath -Destination $backupDir -Force
        Write-Host "Backed up: $filePath"
    }
}

Copy-Item 'C:\Users\soyma\Desktop\Contenido_Flyer_Marbelis_Montero.docx' -Destination $flyerDir -Force -ErrorAction SilentlyContinue
Copy-Item 'C:\Users\soyma\OneDrive\Desktop\DOCUMENTO_OFICIAL_FLYER_MARBELIS_MONTERO.pdf' -Destination $flyerDir -Force -ErrorAction SilentlyContinue
Copy-Item 'C:\Users\soyma\OneDrive\Desktop\documento_flyer_arraial.html' -Destination $flyerDir -Force -ErrorAction SilentlyContinue
Copy-Item 'C:\Users\soyma\OneDrive\Desktop\contenido_flyer_arraial.txt' -Destination $flyerDir -Force -ErrorAction SilentlyContinue

Write-Host "Backup completed successfully."
