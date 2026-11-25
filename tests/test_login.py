import pytest
from playwright.sync_api import expect

from tests.conftest import PASSWORD


@pytest.mark.smoke
@pytest.mark.login
def test_tc_login_01_valid_login(login_page, inventory, page):
    """TC-LOGIN-01: valid credentials open the products page."""
    login_page.login("standard_user", PASSWORD)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory.title).to_have_text("Products")
    expect(inventory.items).to_have_count(6)


@pytest.mark.login
def test_tc_login_02_wrong_password(login_page, page):
    """TC-LOGIN-02: valid user + wrong password shows an error."""
    login_page.login("standard_user", "wrong_password")
    expect(login_page.error).to_contain_text(
        "Username and password do not match any user in this service"
    )
    expect(page).to_have_url("https://www.saucedemo.com/")


@pytest.mark.login
def test_tc_login_03_unknown_user(login_page):
    """TC-LOGIN-03: unknown username shows an error."""
    login_page.login("not_a_user", PASSWORD)
    expect(login_page.error).to_contain_text("do not match any user")


@pytest.mark.login
def test_tc_login_04_locked_out_user(login_page):
    """TC-LOGIN-04: locked-out user is refused."""
    login_page.login("locked_out_user", PASSWORD)
    expect(login_page.error).to_contain_text("this user has been locked out")


@pytest.mark.login
@pytest.mark.parametrize(
    "user,pwd,message",
    [
        ("", PASSWORD, "Username is required"),
        ("standard_user", "", "Password is required"),
        ("", "", "Username is required"),
    ],
    ids=["empty-username", "empty-password", "both-empty"],
)
def test_tc_login_05_required_fields(login_page, user, pwd, message):
    """TC-LOGIN-05: empty fields are validated."""
    login_page.login(user, pwd)
    expect(login_page.error).to_contain_text(message)


@pytest.mark.login
def test_tc_login_06_username_is_case_sensitive(login_page):
    """TC-LOGIN-06: usernames are case sensitive."""
    login_page.login("STANDARD_USER", PASSWORD)
    expect(login_page.error).to_be_visible()


@pytest.mark.login
def test_tc_login_07_direct_url_requires_login(page):
    """TC-LOGIN-07: protected page cannot be opened without logging in."""
    page.goto("/inventory.html")
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "only access '/inventory.html' when you are logged in"
    )


@pytest.mark.login
def test_tc_login_08_logout(logged_in, login_page, page):
    """TC-LOGIN-08: logout returns to the login page."""
    logged_in.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.login_button).to_be_visible()


@pytest.mark.login
@pytest.mark.known_bug
@pytest.mark.xfail(reason="BUG-004: performance_glitch_user login is very slow", strict=False)
def test_tc_login_09_performance_user_logs_in_quickly(login_page, inventory, page):
    """TC-LOGIN-09: login should finish within 2 seconds."""
    login_page.login("performance_glitch_user", PASSWORD)
    expect(inventory.title).to_be_visible(timeout=2000)
