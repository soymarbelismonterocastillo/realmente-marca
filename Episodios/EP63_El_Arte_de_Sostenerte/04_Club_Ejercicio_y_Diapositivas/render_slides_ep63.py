import asyncio
import os
import shutil
from playwright.async_api import async_playwright

async def render_and_distribute():
    src_html = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP63_El_Arte_de_Sostenerte\04_Club_Ejercicio_y_Diapositivas\presentacion_episodio_63.html"
    root_html = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\presentacion_episodio_63.html"
    previews_dir = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP63_El_Arte_de_Sostenerte\04_Club_Ejercicio_y_Diapositivas\previews"
    artifact_dir = r"C:\Users\soyma\.gemini\antigravity\brain\3242c367-2c19-4fb8-ac90-ddfe9bdd3949"
    desktop_dir = os.path.join(os.environ.get("USERPROFILE", r"C:\Users\soyma"), "Desktop")
    
    os.makedirs(previews_dir, exist_ok=True)
    os.makedirs(artifact_dir, exist_ok=True)
    
    # 1. Copy to Root
    shutil.copy2(src_html, root_html)
    print(f"Copied to root: {root_html}")
    
    # 2. Copy to Desktop
    desktop_html = os.path.join(desktop_dir, "CLASE_SABADO_EP63.html")
    shutil.copy2(src_html, desktop_html)
    print(f"Copied to desktop: {desktop_html}")
    
    # Desktop .bat launcher
    desktop_bat = os.path.join(desktop_dir, "ABRIR_CLASE_SABADO_EP63.bat")
    with open(desktop_bat, "w", encoding="utf-8") as f:
        f.write(f'@echo off\nstart "" "{desktop_html}"\nexit\n')
    print(f"Created launcher: {desktop_bat}")
    
    # Desktop .url shortcut
    desktop_url = os.path.join(desktop_dir, "CLASE_SABADO_EP63.url")
    with open(desktop_url, "w", encoding="utf-8") as f:
        f.write(f'[InternetShortcut]\nURL=file:///{desktop_html.replace(os.sep, "/")}\nIconIndex=0\n')
    print(f"Created shortcut: {desktop_url}")
    
    # 3. Copy to Google Drive if available
    gdrive_ep = r"G:\Mi unidad\MARCA\Episodios\EP63_El_Arte_de_Sostenerte\04_Club_Ejercicio_y_Diapositivas"
    if os.path.exists(gdrive_ep):
        gdrive_dest = os.path.join(gdrive_ep, "presentacion_episodio_63.html")
        shutil.copy2(src_html, gdrive_dest)
        print(f"Synced to Google Drive: {gdrive_dest}")
        
    gdrive_club = r"G:\Mi unidad\MARCA\Realmente_Club"
    if os.path.exists(gdrive_club):
        gdrive_club_dest = os.path.join(gdrive_club, "Presentacion_Clase_Sabado_EP63_Marbelis_Montero.html")
        shutil.copy2(src_html, gdrive_club_dest)
        print(f"Synced to Google Drive Club: {gdrive_club_dest}")

    # 4. Playwright Screenshot Capture (9 slides)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 850})
        await page.goto(f"file:///{src_html.replace(os.sep, '/')}")
        await page.wait_for_timeout(1000)
        
        deck = await page.query_selector("#deck")
        total_slides = 9
        
        for i in range(total_slides):
            await page.evaluate(f"showSlide({i})")
            await page.wait_for_timeout(350)
            filename = f"slide_{i+1:02d}.png"
            img_path = os.path.join(previews_dir, filename)
            if deck:
                await deck.screenshot(path=img_path)
            else:
                await page.screenshot(path=img_path)
            
            artifact_img_path = os.path.join(artifact_dir, filename)
            shutil.copy2(img_path, artifact_img_path)
            print(f"Slide {i+1} captured: {img_path}")
            
        await browser.close()
        print("All 9 slides successfully rendered!")

if __name__ == "__main__":
    asyncio.run(render_and_distribute())
