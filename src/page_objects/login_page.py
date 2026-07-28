from typing import Optional

from src.locators.login_locators import LoginLocators
from src.page_objects.base_page import BasePage


class LoginPage(BasePage):
    def open(self, path: Optional[str] = None):
        if path is None:
            self.page.goto('https://www.saucedemo.com')
        else:
            super().open(path)

    def login(self, username: str, password: str):
        self.page.fill(LoginLocators.USERNAME, username)
        self.page.fill(LoginLocators.PASSWORD, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def expect_login_page_visible(self):
        self.page.wait_for_selector(LoginLocators.LOGIN_BUTTON)

    def expect_inventory_visible(self):
        self.page.wait_for_selector(LoginLocators.INVENTORY_TITLE)
