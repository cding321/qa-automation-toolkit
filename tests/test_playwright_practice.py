from playwright.sync_api import Page, expect

from pages.practice_page import PracticePage

# def test_login_and_url(page: Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#     page.get_by_placeholder("Username").fill("Admin")
#     page.get_by_placeholder("Password").fill("admin123")
#     page.get_by_role("button", name="Login").click()
#
#     expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
#     expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()

def test_radiobutton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_label("Address").fill("123 happy rd, dallas, TX 77777")

    page.get_by_role("radio", name="Male", exact=True).check()
    expect(page.get_by_role("radio", name="Male",exact=True)).to_be_checked()
    expect(page.get_by_role("radio", name="Female")).not_to_be_checked()

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_role("checkbox", name="Tuesday").check()
    page.get_by_role("checkbox", name="Thursday").check()
    page.get_by_role("checkbox", name="Saturday").check()
    expect(page.get_by_role("checkbox", name="Saturday")).to_be_checked()
    expect(page.get_by_role("checkbox", name="Sunday")).not_to_be_checked()

def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_label("Country").select_option(label="China")
    expect(page.get_by_label("Country")).to_have_value("china")
    page.get_by_label("Country").select_option(label="United States")
    expect(page.get_by_label("Country")).to_have_value("usa")

def test_listbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    color = page.get_by_label("Colors")
    color.select_option(label="Green")
    expect(color).to_have_value("green")
    expect(color).not_to_have_value("red")

def test_datepicker1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#datepicker").fill("05/06/2020")
    expect(page.locator("#datepicker")).to_have_value("05/06/2020")

def test_datepicker2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#datepicker").click()
    page.get_by_title("Prev").click()
    page.locator("#ui-datepicker-div").get_by_text("1",exact=True).click()
    expect(page.locator("#datepicker")).to_have_value("06/01/2026")

def test_link_popup(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Posts (Atom)").click()

    popup = popup_info.value
    expect(popup).to_have_url("https://testautomationpractice.blogspot.com/feeds/posts/default")


def test_table_select(page:Page):
    practice_page = PracticePage(page)

    practice_page.open()

    practice_page.select_product("Laptop")
    laptop_row = page.locator("#productTable tr").filter(has_text="Laptop")
    expect(laptop_row.get_by_role("checkbox")).to_be_checked()

    practice_page.go_to_page("3")
    practice_page.select_product("Router")
    router_row = page.locator("#productTable tr").filter(has_text="Router")
    expect(router_row.get_by_role("checkbox")).to_be_checked()

    # rows = page.locator("#productTable tr")
    # row1 = rows.filter(has_text="Laptop")
    # checkbox1 = row1.get_by_role("checkbox")
    # checkbox1.check()
    # expect(checkbox1).to_be_checked()

    # next_pg = page.locator(".pagination").get_by_role("link",name="3")
    # next_pg.click()
    # row2 = rows.filter(has_text="Router")
    # checkbox2 = row2.get_by_role("checkbox")
    # checkbox2.check()
    # expect(checkbox2).to_be_checked()
