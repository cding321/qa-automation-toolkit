from playwright.sync_api import Playwright, Page

def test_login(page: Page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()



