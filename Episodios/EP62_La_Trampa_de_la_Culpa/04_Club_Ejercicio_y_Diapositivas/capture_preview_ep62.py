import asyncio
import os
import shutil
from playwright.async_api import async_playwright

async def capture_slides():
    output_dir = r"c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas\previews"
    artifact_dir = r"C:\Users\soyma\.gemini\antigravity\brain\7b5504b3-620a-42bc-9879-e0e1252bfbe5"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(artifact_dir, exist_ok=True)
    
    html_path = r"c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\presentacion_episodio_62.html"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 850})
        await page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        await page.wait_for_timeout(1000)
        
        deck = await page.query_selector("#deck")
        total_slides = 8
        
        for i in range(total_slides):
            await page.evaluate(f"showSlide({i})")
            await page.wait_for_timeout(400)
            filename = f"slide_{i+1:02d}.png"
            img_path = os.path.join(output_dir, filename)
            if deck:
                await deck.screenshot(path=img_path)
            else:
                await page.screenshot(path=img_path)
            
            artifact_img_path = os.path.join(artifact_dir, filename)
            shutil.copy2(img_path, artifact_img_path)
            print(f"Captured: {img_path} -> Copied to: {artifact_img_path}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_slides())
