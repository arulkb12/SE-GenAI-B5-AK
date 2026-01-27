from playwright.async_api import async_playwright
import asyncio


async def playwright_functions():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # navigation
        await page.goto("https://www.google.com")

        await page.wait_for_timeout(10000)

        await browser.close()

        #CSS selector & xpath
        


asyncio.run(playwright_functions())

#if __name__ == "__main__":
  