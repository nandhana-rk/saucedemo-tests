from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.items = page.locator('[data-test="inventory-item"]')
        self.names = page.locator('[data-test="inventory-item-name"]')
        self.prices = page.locator('[data-test="inventory-item-price"]')
        self.images = page.locator('[data-test="inventory-item"] img')
        self.sort = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')

    def add_to_cart(self, slug: str):
        self.page.locator(f'[data-test="add-to-cart-{slug}"]').click()

    def remove_from_cart(self, slug: str):
        self.page.locator(f'[data-test="remove-{slug}"]').click()

    def sort_by(self, value: str):
        """value: az | za | lohi | hilo"""
        self.sort.select_option(value)

    def item_names(self) -> list[str]:
        return self.names.all_inner_texts()

    def item_prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
