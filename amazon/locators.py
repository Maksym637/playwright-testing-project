"""Module containing locators for different pages"""


class HomePageLocators:
    """Locators for the home page elements"""

    LANGUAGE_ICON = "//span[@class='icp-nav-link-inner']"
    LANGUAGE_OPTION = (
        lambda LANG, ISO: f"//div[@id='nav-flyout-icp']//a[@lang='{LANG}-{ISO}']"
    )
    NAV_BAR_ITEMS = "//div[@id='nav-main']//a"
    NAV_HAMBURGER_MENU = "#nav-hamburger-menu"
    CART_ICON = "//header//a[@id='nav-cart']"
    PRODUCT_TITLE = "//li[@class='sc-item-product-title-cont']"
    TRASH_BUTTON = "//span[@class='a-icon a-icon-small-trash']"
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

    NAME_INPUT = "#ap_customer_name"
    EMAIL_INPUT = "#ap_email"
    PASSWORD_INPUT = "#ap_password"
    PASSWORD_CHECK_INPUT = "#ap_password_check"
    CONTINUE_VERIFY_BUTTON = "//input[@class='a-button-input']"
    ERROR_MESSAGES = "//div[@class='a-alert-content']"


class CartPageLocators:
    """Locators for the cart page elements"""

    pass


class ProductsPageLocators:
    """Locators for the product listing and details page elements"""

    PRODUCT_LIST = "//div[@role='listitem']"
    PRODUCT_TITLE = "//h1/span[@id='productTitle']"
    ADD_TO_CART_BUTTON = "//input[@id='add-to-cart-button']"
