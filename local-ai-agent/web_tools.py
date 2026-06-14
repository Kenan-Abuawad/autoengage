from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import time


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


load_dotenv()
with sync_playwright() as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()

 page.goto("https://www.linkedin.com/login" )
 username = os.getenv("LINKEDIN_USERNAME")
 password = os.getenv("LINKEDIN_PASSWORD")
 if not username or not password:
     raise ValueError("LINKEDIN_USERNAME and LINKEDIN_PASSWORD must be set")
 page.fill("#username", username)
 page.fill("#password", password)
 page.click('button[type="submit"]')

 page.wait_for_selector("div.feed-shared-update-v2", timeout=10000)

 print("!LinkedIn-מחובר ל ✅")


 page.fill('input[aria-label="Search"]', "AI automation")
 page.keyboard.press("Enter")
 page.wait_for_timeout(3000)

 page.screenshot(path="linkedin_search.png")
 print("צילום מסך נשמר ✅")

 browser.close()
