from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_until_loaded(self, selector, timeout=30000):
        return self.page.wait_for_selector(selector, timeout=timeout)