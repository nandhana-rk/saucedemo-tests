import pytest
from playwright.sync_api import expect

from tests.conftest import PASSWORD


@pytest.mark.inventory
def test_tc_inv_01_sort_name_az(logged_in):
    """TC-INV-01: sort A to Z."""
    logged_in.sort_by("az")
    names = logged_in.item_names()
    assert names == sorted(names)


@pytest.mark.inventory
def test_tc_inv_02_sort_name_za(logged_in):
    """TC-INV-02: sort Z to A."""
    logged_in.sort_by("za")
    names = logged_in.item_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.inventory
def test_tc_inv_03_sort_price_low_high(logged_in):
    """TC-INV-03: sort price low to high."""
    logged_in.sort_by("lohi")
    prices = logged_in.item_prices()
    assert prices == sorted(prices)


@pytest.mark.inventory
def test_tc_inv_04_sort_price_high_low(logged_in):
    """TC-INV-04: sort price high to low."""
    logged_in.sort_by("hilo")
    prices = logged_in.item_prices()
    assert prices == sorted(prices, reverse=True)


@pytest.mark.inventory
def test_tc_inv_05_every_product_has_distinct_image(logged_in):
    """TC-INV-05: each product shows its own image (standard_user)."""
    srcs = logged_in.images.evaluate_all("els => els.map(e => e.getAttribute('src'))")
    assert len(srcs) == 6
    assert len(set(srcs)) == 6


@pytest.mark.inventory
@pytest.mark.known_bug
@pytest.mark.xfail(reason="BUG-001: problem_user sees the same image for every product", strict=False)
def test_tc_inv_06_problem_user_images(login_page, inventory):
    """TC-INV-06: problem_user should also see distinct images."""
    login_page.login("problem_user", PASSWORD)
    srcs = inventory.images.evaluate_all("els => els.map(e => e.getAttribute('src'))")
    assert len(set(srcs)) == 6


@pytest.mark.inventory
@pytest.mark.known_bug
@pytest.mark.xfail(reason="BUG-002: problem_user sorting has no effect", strict=False)
def test_tc_inv_07_problem_user_sort(login_page, inventory):
    """TC-INV-07: problem_user sort Z to A should reorder products."""
    login_page.login("problem_user", PASSWORD)
    inventory.sort_by("za")
    names = inventory.item_names()
    assert names == sorted(names, reverse=True)
