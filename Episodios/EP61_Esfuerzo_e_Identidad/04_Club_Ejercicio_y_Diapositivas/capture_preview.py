import asyncio
from playwright.async_api import async_playwright
import os

async def capture_slides():
    output_dir = r"c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP61_Esfuerzo_e_Identidad\04_Club_Ejercicio_y_Diapositivas\previews"
    os.makedirs(output_dir, exist_ok=True)
    html_path = r"c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\presentacion_episodio_61.html"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        await page.wait_for_timeout(1000)
        
        deck = await page.query_selector("#deck")
        
        for i in range(11):
            await page.evaluate(f"showSlide({i})")
            await page.wait_for_timeout(400)
            img_path = os.path.join(output_dir, f"slide_{i+1:02d}.png")
            if deck:
                await deck.screenshot(path=img_path)
            else:
                await page.screenshot(path=img_path)
            print(f"Captured: {img_path}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_slides())
