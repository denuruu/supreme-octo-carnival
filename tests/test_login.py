def test_login_success(inventory_page):
    assert inventory_page.is_loaded()

def test_login_wrong_password(login_page):
    login_page.fill_data_and_click("standard_user", "wrong_password")
    error = login_page.page.text_content("[data-test='error']")
    assert "Username and password do not match" in error