from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page:Page):
        self.page = page

    def open(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.page.locator("#username").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Submit").click()

