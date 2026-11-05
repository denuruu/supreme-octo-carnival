# Проверка, что страница товаров открылась.
def test_inventory_page_is_loaded(inventory_page):
    assert inventory_page.is_loaded()

# Проверка, что товар добавлен в корзину.
def test_add_to_cart_button(inventory_page):
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == 1

# TODO: подумать, может можно ещё какие-то кейсы проверить