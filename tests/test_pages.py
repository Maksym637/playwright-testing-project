import pytest
from playwright.sync_api import sync_playwright
from amazon.home_page import HomePage


@pytest.fixture
def browser():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()


# TC - 1
def test_login_page(browser) -> None:
    """
    This test case verifies if an error pop-up with the appropriate
    error message appears when incorrect user data is entered
    """
    home_page = HomePage(browser)

    actual_error_msg = (
        home_page.navigate_to_website()
        .reload_page()
        .go_to_all_menu()
        .go_to_sign_in_option()
        .enter_email("tuser!gmail.com")
        .click_continue_button()
        .get_error_message()
    )

    assert actual_error_msg == (
        "Wrong or Invalid email address or mobile phone number. "
        "Please correct and try again."
    )


# TC - 2
def test_register_page():
    pass


# TC - 3
def test_products_page(browser) -> None:
    """This test case verifies if 10 products are displayed on the products page"""
    home_page = HomePage(browser)

    actual_products_number = (
        home_page.navigate_to_website()
        .reload_page()
        .go_to_all_menu()
        .select_option_from_menu(menu="Shop by Department", option="Electronics")
        .select_product_type_from_option(product_type="Accessories & Supplies")
        .get_products_number()
    )

    assert actual_products_number == 10


# TC - 4
def test_cart_page():
    pass


# TC - 5
def test_home_page():
    pass
