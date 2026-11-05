import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        await page.set_content('<html><body style="background:#4C078C;color:white;display:flex;align-items:center;justify-content:center;height:100vh;"><h1>Playwright Ready</h1></body></html>')
        await page.screenshot(path='test_thumb.png')
        await browser.close()
        print('Playwright test passed')

if __name__ == '__main__':
    asyncio.run(test())
