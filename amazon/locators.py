"""Module containing locators for different pages"""


class HomePageLocators:
    """Locators for the home page elements"""

    NAV_HAMBURGER_MENU = "#nav-hamburger-menu"
    CUSTOMER_PROFILE_OPTION = "#hmenu-customer-profile"
    MENU_LIST = "//div[@class='hmenu-item hmenu-title ' and @role='heading']"
    OPTION_LIST = "../following-sibling::li/a[@class='hmenu-item']"
    PRODUCT_TYPE_LIST = (
        "//ul[@class='hmenu hmenu-visible hmenu-translateX']/li/a[@class='hmenu-item']"
    )


class LoginPageLocators:
    """Locators for the login page elements"""

    EMAIL_INPUT = "#ap_email"
    CONTINUE_BUTTON = "//span[@id='continue']"
    CREATE_USER_BUTTON = "#createAccountSubmit"
    ERROR_MESSAGE = "//div[@id='auth-email-invalid-claim-alert']"


class RegisterPageLocators:
    """Locators for the registration page elements"""

    pass


class CartPageLocators:
    """Locators for the cart page elements"""

    pass


class ProductsPageLocators:
    """Locators for the product listing and details page elements"""

    PRODUCT_LIST = "//div[@role='listitem']"
