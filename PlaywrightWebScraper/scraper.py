from urllib.request import urlretrieve
import sys
import asyncio
import asyncio
import sys
import os

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
from playwright.sync_api import sync_playwright


def download_arxiv_pdfs(search_term: str) -> int:
    pdf_count = 0
    os.makedirs("data", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://arxiv.org/search")

        page.get_by_placeholder("Search term...").fill(search_term)
        page.get_by_role("button").get_by_text("Search").nth(1).click()
        page.wait_for_selector("a[href*='arxiv.org/pdf']")

        pdf_links = page.locator("xpath=//a[contains(@href, 'arxiv.org/pdf')]").all()

        for link in pdf_links:
            url = link.get_attribute("href")
            if url:
                file_name = "data/" + url.split("/")[-1] + ".pdf"
                urlretrieve(url, file_name)
                pdf_count += 1

        browser.close()

    return pdf_count