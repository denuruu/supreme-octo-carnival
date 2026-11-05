from .base_page import BasePage


class LoginPage(BasePage):

    # Локаторы
    PAGE_LOGO = ".login_logo"
    LOGIN_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    # Метод для заполнения полей кредов и клик по кнопке логина.
    # TODO: переименовать метод на что-то более подходящее
    def fill_data_and_click(self, username: str, password: str):
        self.page.fill(self.LOGIN_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    # Метод для успешного логина. Возвращает страницу товаров, поэтому передать надо только правильные креды.
    def login(self, username: str, password: str):
        self.fill_data_and_click(username, password)

        from .inventory_page import InventoryPage
        return InventoryPage(self.page)