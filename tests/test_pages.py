import pytest
from amazon.home_page import HomePage


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


@pytest.mark.parametrize(
    "lang, iso, expected_nav_bar_items",
    [
        (
            "es",
            "US",
            [
                "Todo",
                "Ofertas del Día",
                "Servicio al Cliente",
                "Listas",
                "Tarjetas de Regalo",
                "Vender",
            ],
        ),
        (
            "de",
            "DE",
            [
                "Alle",
                "Angebote des Tages",
                "Kundenservice",
                "Wunschlisten",
                "Geschenkkarten",
                "Verkaufen bei Amazon",
            ],
        ),
        (
            "en",
            "US",
            [
                "All",
                "Today's Deals",
                "Customer Service",
                "Registry",
                "Gift Cards",
                "Sell",
            ],
        ),
    ],
)
def test_home_page(browser, lang, iso, expected_nav_bar_items) -> None:
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
