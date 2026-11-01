import asyncio
import os
from playwright.async_api import async_playwright
import fitz  # PyMuPDF

async def generate():
    base_dir = r"c:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP63_El_Arte_de_Sostenerte\04_Club_Ejercicio_y_Diapositivas"
    html_file = os.path.join(base_dir, "hoja_de_trabajo_sostenerte_ep63.html")
    pdf_file = os.path.join(base_dir, "hoja_de_trabajo_sostenerte_ep63.pdf")
    png_file = os.path.join(base_dir, "hoja_de_trabajo_sostenerte_ep63.png")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_url = f"file:///{html_file.replace(os.sep, '/')}"
        await page.goto(file_url, wait_until="networkidle")
        await page.emulate_media(media="print")
        
        # Generar PDF A4
        await page.pdf(
            path=pdf_file,
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
        )
        await browser.close()
        print(f"PDF generado: {pdf_file}")

    # Verificar páginas con PyMuPDF y exportar PNG
    doc = fitz.open(pdf_file)
    page_count = len(doc)
    print(f"Total de páginas en el PDF: {page_count}")
    
    if page_count > 0:
        first_page = doc[0]
        pix = first_page.get_pixmap(dpi=150)
        pix.save(png_file)
        print(f"Vista previa guardada en: {png_file}")
        
    doc.close()

if __name__ == "__main__":
    asyncio.run(generate())
