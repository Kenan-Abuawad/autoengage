from playwright.sync_api import sync_playwright



def get_page_title(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        title = page.title()
        browser.close()
    return title

def read_page_text(url: str, max_chars: int = 4000) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        text = page.locator("body").inner_text()

        browser.close()
        
        return text[:max_chars]

