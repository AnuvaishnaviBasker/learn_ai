import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
