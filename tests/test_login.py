from playwright.sync_api import Page

from src.page_objects.login_page import LoginPage
from src.utils.test_data import LOCKED_OUT_USER, VALID_USER


def test_successful_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.expect_login_page_visible()
    login_page.login(VALID_USER['username'], VALID_USER['password'])
    login_page.expect_inventory_visible()

    assert '/inventory' in page.url


def test_failed_login_shows_error(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(LOCKED_OUT_USER['username'], LOCKED_OUT_USER['password'])

    assert 'Sorry, this user has been locked out' in page.text_content('[data-test="error"]')
