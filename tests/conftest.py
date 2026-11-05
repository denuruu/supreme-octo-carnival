import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

# Фикстура для открытия сайта.
@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    return LoginPage(page)

# Фикстура для успешного логина (верные креды).
@pytest.fixture
def inventory_page(login_page):
    return login_page.login("standard_user", "secret_sauce")

# TODO: подумать, может можно добавить фикстуры для неуспешного логина (неверные креды).