from pages.login_page import LoginPage


def test_login_success(login_page):
    inventory = login_page.login("standard_user", "secret_sauce")
    assert inventory.is_loaded()

def test_login_wrong_password(login_page):
    login_page.page.fill("#user-name", "standard_user")
    login_page.page.fill("#password", "wrong")
    login_page.page.click("#login-button")
    error = login_page.page.text_content("[data-test='error']")
    assert "Username and password do not match" in error