# calculator_playwright_google.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # open Google Calculator via search
    page.goto("https://www.google.com/search?q=calculator")

    # simulate clicks
    page.get_by_role("button", name="7").click()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="5").click()
    page.get_by_role("button", name="=").click()

    # get result from calculator display
    result = page.locator("span[jsname='VssY5c']").inner_text()
    print(f"✅ 7 + 5 = {result}")

    browser.close()
