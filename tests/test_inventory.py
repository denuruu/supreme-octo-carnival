def test_inventory_page_is_loaded(inventory_page):
    assert inventory_page.is_loaded()

def test_add_to_cart_button(inventory_page):
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == 1
