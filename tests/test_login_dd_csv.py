from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest
import csv

login_data = []

with open("data/login_data.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        login_data.append((row["username"], row["password"],row["validity"]))

@pytest.mark.parametrize("username,password,validity", login_data)
def test_login_and_url(username, password, validity,page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username,password)

    if validity.lower() == "valid":
        logout_link = page.get_by_role("link", name="Log out")
        expect(logout_link).to_be_visible(timeout=3000)
    else:
        error_message = page.locator(".show")
        expect(error_message).to_be_visible(timeout=3000)
