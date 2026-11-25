import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"
BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def inventory(page):
    return InventoryPage(page)


@pytest.fixture
def cart(page):
    return CartPage(page)


@pytest.fixture
def checkout(page):
    return CheckoutPage(page)


@pytest.fixture
def logged_in(login_page, inventory):
    """standard_user already on the inventory page."""
    login_page.login("standard_user", PASSWORD)
    assert inventory.title.is_visible()
    return inventory
