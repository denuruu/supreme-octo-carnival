from .base_page import BasePage


class LoginPage(BasePage):

    PAGE_LOGO = ".login_logo"
    LOGIN_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.page.fill(self.LOGIN_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

        from .inventory_page import InventoryPage
        return InventoryPage(self.page)