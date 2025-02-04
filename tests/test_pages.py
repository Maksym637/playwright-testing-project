"""Module containing all UI tests"""

import pytest
from playwright.sync_api import Page
from amazon.home_page import HomePage
from .verification_data import ERROR_MSGS, NAV_BAR_ITEMS


def test_login_page(browser: Page) -> None:
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


@pytest.mark.parametrize(
    "name, email, password, re_password, expected_error_msg",
    [
        (" ", " ", " ", " ", ERROR_MSGS["empty"]),
        ("tuser", "tuser!gmail.com", "Tpass123", "Tpass123", ERROR_MSGS["email"]),
        ("tuser", "tuser@gmail.com", "Tpass123", "Tpass1234", ERROR_MSGS["password"]),
    ],
)
def test_register_page(
    browser: Page,
    name: str,
    email: str,
    password: str,
    re_password: str,
    expected_error_msg: list[str],
) -> None:
    """
    This test case verifies if an error messages appear
    when incorrect user data is entered
    """
    home_page = HomePage(browser)

    actual_error_msgs = (
        home_page.navigate_to_website()
        .reload_page()
        .go_to_all_menu()
        .go_to_sign_in_option()
        .go_to_register_option()
        .enter_name(name)
        .enter_email(email)
        .enter_password(password)
        .re_enter_password(re_password)
        .click_continue_verify_button()
        .get_error_messages()
    )

    assert actual_error_msgs == expected_error_msg


def test_products_page(browser: Page) -> None:
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
def test_cart_page(browser: Page) -> None:
    """..."""


@pytest.mark.parametrize(
    "lang, iso, expected_nav_bar_items",
    [
        ("es", "US", NAV_BAR_ITEMS["es"]),
        ("de", "DE", NAV_BAR_ITEMS["de"]),
        ("en", "US", NAV_BAR_ITEMS["en"]),
    ],
)
def test_home_page(
    browser: Page, lang: str, iso: str, expected_nav_bar_items: list[str]
) -> None:
    """
    This test case verifies if text is internalized correctly
    when switching to another language
    """
    home_page = HomePage(browser)

    actual_nav_bar_items = (
        home_page.navigate_to_website()
        .reload_page()
        .go_to_language_icon()
        .select_language(lang, iso)
        .get_nav_bar_items()
    )

    assert actual_nav_bar_items == expected_nav_bar_items
