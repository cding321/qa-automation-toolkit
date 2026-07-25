from wsgiref.validate import validator

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest
import openpyxl

login_data = []

workbook = openpyxl.load_workbook("data/login_data.xlsx")
sheet = workbook.active # or worksheet["sheetname"]

for row in sheet.iter_rows(min_row=2, values_only=True):
    # login_data.append(row) - recognize blank value to None
    username, password, validity = row
    login_data.append((str(username or ""), str(password or ""), str(validity or "")))
    # login_data.append(tuple("" if value is None else str(value) for value in row)) - recognize blank value to ""
workbook.close()

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
