from playwright.sync_api import Page


class PracticePage:

    def __init__(self, page:Page):
        self.page = page

    def open(self):
        self.page.goto("https://testautomationpractice.blogspot.com/")

    def select_product(self,product_name:str):
        row = self.page.locator("#productTable tr").filter(has_text=product_name)
        checkbox = row.get_by_role("checkbox")
        checkbox.click()
        return checkbox

    def go_to_page(self, page_number: str):
        self.page.locator("#pagination").get_by_role("link",name=page_number).click()
