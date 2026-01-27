from flask import Flask, render_template_string
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)

# Async function to run Bing search and open first result
async def run_bing_search_and_extract():
    async with async_playwright() as p:
        # Launch Chromium browser
        browser = await p.chromium.launch(
            headless=True,  # headless=True for server
            slow_mo=100     # optional for human-like behavior
        )
        page = await browser.new_page()

        # Go to Bing
        await page.goto("https://www.bing.com", wait_until="domcontentloaded")

        # Type search query
        await page.fill('xpath=//*[@id="sb_form_q"]', "Amazon top selling product in India")
        await page.keyboard.press("Enter")

        # Wait for search results to appear
        await page.wait_for_selector("#sb_form_q", timeout=30000)

        # Click the first search result (robust)
        first_result = page.locator("#sb_form_q").first
        await first_result.scroll_into_view_if_needed()
        await first_result.click()

        # Wait for new page to load
        await page.wait_for_load_state("domcontentloaded")

        return "✅ Bing search completed and first result opened successfully."


@app.route("/")
def home():
    # Run Playwright async function safely inside Flask
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(run_bing_search_and_extract())
    except Exception as e:
        result = f"❌ Error occurred: {e}"

    # Return simple HTML
    html = f"""
    <html>
        <head><title>Bing Search</title></head>
        <body>
            <h1>Bing Search Result</h1>
            <p>{result}</p>
        </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
