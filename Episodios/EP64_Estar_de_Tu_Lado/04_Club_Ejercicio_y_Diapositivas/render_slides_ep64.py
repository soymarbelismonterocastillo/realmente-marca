import asyncio
import os
import shutil
from playwright.async_api import async_playwright

async def render_and_distribute():
    src_html = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\presentacion_episodio_64.html"
    dest_folder = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP64_Estar_de_Tu_Lado\04_Club_Ejercicio_y_Diapositivas"
    previews_dir = os.path.join(dest_folder, "previews")
    desktop_dir = os.path.join(os.environ.get("USERPROFILE", r"C:\Users\soyma"), "Desktop")
    
    os.makedirs(previews_dir, exist_ok=True)
    
    # 1. Copy to Episode Folder
    shutil.copy2(src_html, os.path.join(dest_folder, "presentacion_episodio_64.html"))
    
    # 2. Copy to Desktop
    desktop_html = os.path.join(desktop_dir, "PRESENTACION_EPISODIO_64.html")
    shutil.copy2(src_html, desktop_html)
    
    # Desktop .url shortcut
    desktop_url = os.path.join(desktop_dir, "PRESENTACION_EPISODIO_64.url")
    with open(desktop_url, "w", encoding="utf-8") as f:
        f.write(f'[InternetShortcut]\nURL=file:///{desktop_html.replace(os.sep, "/")}\nIconIndex=0\n')
    
    # 3. Copy to Google Drive if available
    gdrive_ep = r"G:\Mi unidad\MARCA\Episodios\EP64_Estar_de_Tu_Lado\04_Club_Ejercicio_y_Diapositivas"
    os.makedirs(gdrive_ep, exist_ok=True)
    gdrive_dest = os.path.join(gdrive_ep, "presentacion_episodio_64.html")
    shutil.copy2(src_html, gdrive_dest)
    print(f"Synced to Google Drive: {gdrive_dest}")

    # 4. Playwright Screenshot Capture (8 slides)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 850})
        await page.goto(f"file:///{src_html.replace(os.sep, '/')}")
        await page.wait_for_timeout(1000)
        
        deck = await page.query_selector(".deck-container")
        total_slides = 27
        
        for i in range(total_slides):
            slide_idx = i + 1
            await page.evaluate(f"updateDeck({i})")
            await page.wait_for_timeout(350)
            
            out_png = os.path.join(previews_dir, f"slide_{slide_idx:02d}.png")
            slide_el = await page.query_selector(f".slide:nth-child({slide_idx})")
            if slide_el:
                await slide_el.screenshot(path=out_png)
                print(f"Rendered: {out_png}")
                
        await browser.close()
    print("All 8 slides rendered and distributed successfully!")

if __name__ == "__main__":
    asyncio.run(render_and_distribute())
