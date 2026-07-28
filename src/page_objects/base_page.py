from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str | None = None):
        if path is None:
            self.page.goto('https://sauce-demo.myshopify.com', wait_until='domcontentloaded')
        else:
            self.page.goto(f'https://sauce-demo.myshopify.com{path}', wait_until='domcontentloaded')

    def expect_text(self, text: str):
        body_text = self.page.locator('body').inner_text()
        assert text.lower() in body_text.lower(), f'Expected text {text!r} not found in page body.'
