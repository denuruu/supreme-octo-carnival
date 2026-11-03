from .base_page import BasePage


class LoginPage(BasePage):

    PAGE_LOGO = ".login_logo"
    LOGIN_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    def fill_data_and_click(self, username: str, password: str):
        self.page.fill(self.LOGIN_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.fill_data_and_click(username, password)

        from .inventory_page import InventoryPage
        return InventoryPage(self.page)