# Copy updated schema to Desktop
$schemaSrc = 'C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP66_Te_Enamoraste_de_la_Idea\02_Podcast_Guion_y_Grabacion\esquema_detallado_ep66.html'
Copy-Item $schemaSrc -Destination 'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_EPISODIO_66.html' -Force
Copy-Item $schemaSrc -Destination 'C:\Users\soyma\Desktop\ESQUEMA_EPISODIO_66.html' -Force

# Items to remove from both Desktop paths
$itemsToRemove = @(
    # Word and md documents that were unreadable
    'C:\Users\soyma\Desktop\Contenido_Flyer_Marbelis_Montero.docx',
    'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_EPISODIO_66.md',
    'C:\Users\soyma\Desktop\ESQUEMA_EPISODIO_66.md',
    
    # Old schema files for EP64 and EP65 (already recorded)
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
    
    # YouTube thumbnails (already uploaded)
    'C:\Users\soyma\OneDrive\Desktop\miniatura_ep64.png',
    'C:\Users\soyma\OneDrive\Desktop\MINIATURA_EPISODIO_64_YOUTUBE.png',
    'C:\Users\soyma\OneDrive\Desktop\MINIATURA_YOUTUBE_EPISODIO_64.png',
    'C:\Users\soyma\Desktop\miniatura_ep64.png',
    'C:\Users\soyma\Desktop\MINIATURA_EPISODIO_64_YOUTUBE.png',
    
    # Old flyer files and tests (backed up in MARCA)
    'C:\Users\soyma\OneDrive\Desktop\contenido_flyer_arraial.txt',
    'C:\Users\soyma\Desktop\contenido_flyer_arraial.txt',
    'C:\Users\soyma\OneDrive\Desktop\documento_flyer_arraial.html',
    'C:\Users\soyma\Desktop\documento_flyer_arraial.html',
    'C:\Users\soyma\OneDrive\Desktop\DOCUMENTO_OFICIAL_FLYER_MARBELIS_MONTERO.pdf',
    'C:\Users\soyma\Desktop\DOCUMENTO_OFICIAL_FLYER_MARBELIS_MONTERO.pdf',
    'C:\Users\soyma\OneDrive\Desktop\test_evaluacion_maslow.pdf',
    'C:\Users\soyma\Desktop\test_evaluacion_maslow.pdf',
    
    # EP66 presentation (lives in MARCA folder, accessible via the esquema)
    'C:\Users\soyma\OneDrive\Desktop\PRESENTACION_EPISODIO_66.html',
    'C:\Users\soyma\Desktop\PRESENTACION_EPISODIO_66.html',
    
    # Old name of detailed schema to avoid duplicate icons
    'C:\Users\soyma\OneDrive\Desktop\ESQUEMA_DETALLADO_EPISODIO_66.html',
    'C:\Users\soyma\Desktop\ESQUEMA_DETALLADO_EPISODIO_66.html'
)

foreach ($filePath in $itemsToRemove) {
    if (Test-Path $filePath) {
        Remove-Item -Path $filePath -Force
        Write-Host "Removed: $filePath"
    }
}

Write-Host "Cleanup completed successfully."
