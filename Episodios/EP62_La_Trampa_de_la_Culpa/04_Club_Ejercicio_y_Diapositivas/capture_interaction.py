import asyncio
import os
from playwright.async_api import async_playwright

async def capture_details():
    folder = r"C:\Users\soyma\OneDrive\Documents\ANTIGRAVITY\MARCA\Episodios\EP62_La_Trampa_de_la_Culpa\04_Club_Ejercicio_y_Diapositivas"
    html_file = os.path.join(folder, "autoevaluacion_culpa_inconsciente_ep62.html")
    preview_questions_mobile = os.path.join(folder, "preview_mobile_questions.png")
    preview_results_mobile = os.path.join(folder, "preview_mobile_results.png")
    
    html_url = f"file:///{html_file.replace(os.sep, '/')}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 430, "height": 932},
            device_scale_factor=2
        )
        page = await context.new_page()
        await page.goto(html_url, wait_until="networkidle")
        await page.wait_for_timeout(800)
        
        # Click some answers to show the live interactive score in action!
        # Question 1: option 3 (3 pts)
        # Question 2: option 2 (2 pts)
        # Question 3: option 2 (2 pts)
        await page.click('#card-q1 .opt-label:nth-child(4)')
        await page.click('#card-q2 .opt-label:nth-child(3)')
        await page.click('#card-q3 .opt-label:nth-child(3)')
        await page.wait_for_timeout(400)
        
        # Scroll to Question 2 & 3
        q2 = await page.query_selector('#card-q2')
        if q2:
            await q2.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            await page.screenshot(path=preview_questions_mobile)
            print("Questions preview captured:", preview_questions_mobile)
            
        # Complete all questions and show the 70% level highlighted!
        await page.click('#card-q4 .opt-label:nth-child(3)') # 2 pts
        await page.click('#card-q5 .opt-label:nth-child(3)') # 2 pts
        await page.click('#card-q6 .opt-label:nth-child(3)') # 2 pts
        await page.click('#card-q7 .opt-label:nth-child(3)') # 2 pts -> total 15 pts (71%)
        await page.wait_for_timeout(600)
        
        results = await page.query_selector('#resultsSection')
        if results:
            await results.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await page.screenshot(path=preview_results_mobile)
            print("Results preview captured:", preview_results_mobile)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_details())
