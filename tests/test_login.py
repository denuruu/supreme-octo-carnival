# Тест для успешного логина.
def test_login_success(inventory_page):
    assert inventory_page.is_loaded() # Проверка, что страница товаров загрузилась (метод описан в inventory_page.py).

# Тест логина с неправильным паролем.
def test_login_wrong_password(login_page):
    login_page.fill_data_and_click("standard_user", "wrong_password") # Заполняем поля для кредов.
    error = login_page.page.text_content("[data-test='error']") # Получаем текст ошибки.
    assert "Username and password do not match" in error # Проверка, что текст пришёл в ошибке.

# TODO: подумать, может можно ещё какие-то кейсы проверить (например, логин с неправильным логином).