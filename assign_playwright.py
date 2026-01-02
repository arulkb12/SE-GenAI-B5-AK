import asyncio
from playwright.async_api import async_playwright

async def run_bing_search_and_extract():
    async with async_playwright() as p:
        # Launch Chromium browser
        browser = await p.chromium.launch(
            headless=False,  # Show browser
            slow_mo=100      # Human-like actions
        )

        # Open a new page
        page = await browser.new_page()

        # Navigate to Bing
        await page.goto("https://www.bing.com", wait_until="domcontentloaded")

        # XPath for Bing search bar
        search_box_xpath = 'xpath=//*[@id="sb_form_q"]'

        # Wait for search bar
        await page.wait_for_selector(search_box_xpath, timeout=15000)

        # Click and type search query
        await page.click(search_box_xpath)
        await page.type(
            search_box_xpath,
            "Amazon top selling product in India",
            delay=120
        )

        # Press Enter
        await page.keyboard.press("Enter")

        # Wait for search results to load
        await page.wait_for_timeout(5000)

        # XPath for element to click
        new_xpath = 'xpath=//*[@id="gs_main"]/div[2]/div[3]/div/div[2]/a/div/div[1]/div[2]'

        # Wait for element and click
        await page.wait_for_selector(new_xpath, timeout=15000)
        await page.locator(new_xpath).scroll_into_view_if_needed()
        await page.click(new_xpath)

        # Wait for the new page to load
        await page.wait_for_timeout(5000)

        # Extract the visible text from the page
        page_content = await page.evaluate('''() => {
            return document.body.innerText;
        }''')

        # Simple summarization: take first 1000 characters
        summary = page_content[:1000] + "\n\n[Summary truncated]"

        # Save to a text file
        with open("article_summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)

        print("✅ Page content extracted and saved to 'article_summary.txt'.")

        # Optional wait to inspect the page
        await page.wait_for_timeout(5000)

        # Close browser
        await browser.close()


# Run the async function
asyncio.run(run_bing_search_and_extract())
