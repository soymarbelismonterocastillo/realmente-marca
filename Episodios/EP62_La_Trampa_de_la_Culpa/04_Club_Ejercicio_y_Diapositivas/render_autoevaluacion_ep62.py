import asyncio
import os
import fitz
from playwright.async_api import async_playwright

async def render():
    folder = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas"
    html_file = os.path.join(folder, "autoevaluacion_culpa_inconsciente_ep62.html")
    pdf_file = os.path.join(folder, "autoevaluacion_culpa_inconsciente_ep62.pdf")
    preview_mobile = os.path.join(folder, "preview_mobile.png")
    preview_desktop = os.path.join(folder, "preview_desktop.png")
    
    html_url = f"file:///{html_file.replace(os.sep, '/')}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Capture Mobile View
        mobile_context = await browser.new_context(
            viewport={"width": 430, "height": 932},
            device_scale_factor=2
        )
        mobile_page = await mobile_context.new_page()
        await mobile_page.goto(html_url, wait_until="networkidle")
        await mobile_page.wait_for_timeout(800)
        await mobile_page.screenshot(path=preview_mobile, full_page=False)
        print("Mobile preview captured:", preview_mobile)
        await mobile_context.close()
        
        # 2. Capture Desktop View
        desktop_context = await browser.new_context(
            viewport={"width": 1200, "height": 1400},
            device_scale_factor=2
        )
        desktop_page = await desktop_context.new_page()
        await desktop_page.goto(html_url, wait_until="networkidle")
        await desktop_page.wait_for_timeout(800)
        await desktop_page.screenshot(path=preview_desktop, full_page=False)
        print("Desktop preview captured:", preview_desktop)
        
        # 3. Generate High-Quality Printable PDF Continuous
        await desktop_page.pdf(
            path=pdf_file,
            format="A4",
            print_background=True,
            margin={"top": "8mm", "bottom": "8mm", "left": "8mm", "right": "8mm"}
        )
        print("PDF generated successfully:", pdf_file)
        await browser.close()
        
    doc = fitz.open(pdf_file)
    print("NEW PDF PAGE COUNT:", len(doc))

if __name__ == "__main__":
    asyncio.run(render())
