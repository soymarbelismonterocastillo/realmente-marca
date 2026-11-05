import asyncio
import os
from playwright.async_api import async_playwright

BASE_DIR = r"C:/Users/soyma/OneDrive/Documents/ANTIGRAVITY/MARCA/Episodios/EP64_Estar_de_Tu_Lado/02_Podcast_Guion_y_Grabacion"
HTML_PATH = os.path.join(BASE_DIR, "miniatura_fondo_completo_estilo_mcconaughey.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace hook title with new text: ¿A TU FAVOR O EN TU CONTRA?
old_hook = """    <h1 class="hook-title">
      ¿POR QUÉ
      <span class="highlight">TE FALLAS?</span>
    </h1>"""

new_hook = """    <h1 class="hook-title" style="font-size: 94px; line-height: 0.98;">
      ¿A TU FAVOR O
      <span class="highlight">EN TU CONTRA?</span>
    </h1>"""

if old_hook in html:
    html = html.replace(old_hook, new_hook)
else:
    # Alternative replacement in case of whitespace
    import re
    html = re.sub(r'<h1 class="hook-title">.*?</h1>', new_hook, html, flags=re.DOTALL)

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.set_content(html)
        await page.wait_for_timeout(600)
        
        # Save to both standard names so she has it immediately
        out1 = os.path.join(BASE_DIR, "miniatura_fondo_completo_estilo_mcconaughey.png")
        out2 = os.path.join(BASE_DIR, "miniatura_ep64_a_tu_favor_o_en_tu_contra.png")
        out3 = os.path.join(BASE_DIR, "miniatura_ep64_final.png")
        
        await page.screenshot(path=out1, type="png")
        await page.screenshot(path=out2, type="png")
        await page.screenshot(path=out3, type="png")
        
        print("Rendered successfully:", out1)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(render())
