from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator('[data-test="inventory-item"]')
        self.names = page.locator('[data-test="inventory-item-name"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping = page.locator('[data-test="continue-shopping"]')
