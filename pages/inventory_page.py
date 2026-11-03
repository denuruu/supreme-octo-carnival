from .base_page import BasePage

class InventoryPage(BasePage):

    INVENTORY_ITEM = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    SHOPPING_CART = ".shopping_cart_link"

    def is_loaded(self) -> bool:
        return self.page.locator(self.INVENTORY_ITEM).first.is_visible()

    def get_inventory_item_name(self) -> str:
        return self.page.locator(self.INVENTORY_ITEM_NAME).first.text_content().lower().replace(" ", "-")

    def add_item_to_cart(self, item_name: str):
        selector = f"#add-to-cart-{item_name}"
        self.page.click(selector)
        return self

    def get_cart_count(self) -> int:
        badge = self.page.locator(self.SHOPPING_CART)
        # self.add_item_to_cart(item_name)
        count = badge.get_attribute("aria-label").split()
        if badge == 0:
            return 0
        return int(count[1])