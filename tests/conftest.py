import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    return LoginPage(page)

@pytest.fixture
def inventory_page(login_page):
    return login_page.login("standard_user", "secret_sauce")