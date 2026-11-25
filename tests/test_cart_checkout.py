import pytest
from playwright.sync_api import expect

from tests.conftest import BACKPACK, BIKE_LIGHT, PASSWORD


@pytest.mark.smoke
@pytest.mark.checkout
def test_tc_cart_01_add_item_updates_badge(logged_in):
    """TC-CART-01: adding an item sets the cart badge to 1."""
    logged_in.add_to_cart(BACKPACK)
    expect(logged_in.cart_badge).to_have_text("1")


@pytest.mark.checkout
def test_tc_cart_02_add_two_items(logged_in):
    """TC-CART-02: badge counts multiple items."""
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(BIKE_LIGHT)
    expect(logged_in.cart_badge).to_have_text("2")


@pytest.mark.checkout
def test_tc_cart_03_remove_item(logged_in):
    """TC-CART-03: removing an item clears the badge."""
    logged_in.add_to_cart(BACKPACK)
    logged_in.remove_from_cart(BACKPACK)
    expect(logged_in.cart_badge).to_have_count(0)


@pytest.mark.checkout
def test_tc_cart_04_cart_lists_added_item(logged_in, cart):
    """TC-CART-04: cart page shows the item that was added."""
    logged_in.add_to_cart(BACKPACK)
    logged_in.cart_link.click()
    expect(cart.names).to_have_text(["Sauce Labs Backpack"])


@pytest.mark.smoke
@pytest.mark.checkout
def test_tc_chk_01_complete_purchase(logged_in, cart, checkout):
    """TC-CHK-01: end-to-end purchase of one item."""
    logged_in.add_to_cart(BACKPACK)
    logged_in.cart_link.click()
    cart.checkout_button.click()
    checkout.fill_info("Dasthageer", "Basha", "620001")
    expect(checkout.summary_total).to_contain_text("Total: $")
    checkout.finish_button.click()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")


@pytest.mark.checkout
@pytest.mark.parametrize(
    "first,last,postal,message",
    [
        ("", "Basha", "620001", "First Name is required"),
        ("Dasthageer", "", "620001", "Last Name is required"),
        ("Dasthageer", "Basha", "", "Postal Code is required"),
    ],
    ids=["no-first-name", "no-last-name", "no-postal-code"],
)
def test_tc_chk_02_required_fields(logged_in, cart, checkout, first, last, postal, message):
    """TC-CHK-02: checkout form validates required fields."""
    logged_in.add_to_cart(BACKPACK)
    logged_in.cart_link.click()
    cart.checkout_button.click()
    checkout.fill_info(first, last, postal)
    expect(checkout.error).to_contain_text(message)


@pytest.mark.checkout
@pytest.mark.known_bug
@pytest.mark.xfail(reason="BUG-003: problem_user last-name input overwrites first name", strict=False)
def test_tc_chk_03_problem_user_last_name(login_page, inventory, cart, checkout):
    """TC-CHK-03: last name typed by problem_user should land in the last-name field."""
    login_page.login("problem_user", PASSWORD)
    inventory.add_to_cart(BACKPACK)
    inventory.cart_link.click()
    cart.checkout_button.click()
    checkout.first_name.fill("Dasthageer")
    checkout.last_name.fill("Basha")
    expect(checkout.first_name).to_have_value("Dasthageer")
    expect(checkout.last_name).to_have_value("Basha")
