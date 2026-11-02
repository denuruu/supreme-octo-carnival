from .base_page import BasePage

class InventoryPage(BasePage):
    def get_add_to_cart_button(self, item_name: str) -> str:
        return f"#add-to-cart-{item_name.lower().replace(' ', '_')}"

    INVENTORY_ITEM = ".inventory-item"

    def is_loaded(self) -> bool:
        return self.page.locator(self.INVENTORY_ITEM).first.is_visible()