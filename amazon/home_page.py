"""Module for initializing the home page"""

import logging
from playwright.sync_api import Page, expect
from .base_page import BasePage
from .login_page import LoginPage
from .products_page import ProductsPage
from .locators import HomePageLocators
from utils.constants import TimeConstants


class HomePage(BasePage):
    """Represents the home page"""

    def __init__(self, page: Page) -> None:
        """
        Initializes the HomePage with a Playwright Page instance

        Args:
            page (Page): The Playwright page object representing the current browser context
        """
        super().__init__(page)

    def go_to_language_icon(self) -> "HomePage":
        """
        Navigates to the language selection icon and hovers over it

        Returns:
            HomePage: Returns the current instance
        """
        logging.info("Navigating to the language icon")
        language_icon = self.page.locator(HomePageLocators.LANGUAGE_ICON)

        #
        # Navigate to the language icon several times to prevent
        # the language pop-up window from disappearing
        #
        for _ in range(3):
            language_icon.hover()

        return self

    def select_language(self, lang: str, iso: str) -> "HomePage":
        """
        Selects a language from the language pop-up window

        Args:
            lang (str): The name of the language to select
            iso (str): The ISO code corresponding to the language

        Returns:
            HomePage: Returns the current instance
        """
        logging.info("Selecting the '%s' language in the pop-up window", lang)

        self.page.wait_for_selector(
            selector=HomePageLocators.LANGUAGE_OPTION(lang, iso), state="visible"
        )
        self.page.locator(HomePageLocators.LANGUAGE_OPTION(lang, iso)).click()

        expect(self.page.locator(HomePageLocators.LANGUAGE_ICON)).to_have_text(
            lang.upper()
        )

        return self

    def get_nav_bar_items(self) -> list[str]:
        """
        Retrieves the text content of all visible navigation items in the header

        Returns:
            list[str]: A list of navigation item texts, excluding the last one
        """
        logging.info("Getting the text of all navigation items in the header")
        nav_bar_items = self.page.locator(HomePageLocators.NAV_BAR_ITEMS).all()

        visible_nav_bar_items = [
            element.text_content().strip()
            for element in nav_bar_items
            if element.is_visible()
        ]

        return visible_nav_bar_items[0:-1]

    def go_to_cart_icon(self) -> "HomePage":
        """
        Clicks on the 'Cart' icon in the navigation menu

        Returns:
            HomePage: Returns the current instance
        """
        logging.info("Navigating to the cart icon")
        self.page.locator(HomePageLocators.CART_ICON).click()

        self.wait_for_page_load()

        return self

    def get_product_title(self) -> str:
        """
        Retrieves the product title on the home page

        Returns:
            str: The text content of the product title
        """
        logging.info("Getting the product title")
        return self.page.locator(HomePageLocators.PRODUCT_TITLE).text_content().strip()

    def remove_product_from_cart(self) -> "HomePage":
        """
        Clicks on the trash icon, which means removing the product

        Returns:
            HomePage: Returns the current instance
        """
        logging.info("Removing a product from the cart")
        self.page.locator(HomePageLocators.TRASH_BUTTON).click()

        return self

    def go_to_all_menu(self) -> "HomePage":
        """
        Clicks on the hamburger menu to open the navigation menu

        Returns:
            HomePage: Returns the current instance
        """
        logging.info("Navigating to the 'All' hamburger menu")
        self.page.locator(HomePageLocators.NAV_HAMBURGER_MENU).click()

        return self

    def go_to_sign_in_option(self) -> LoginPage:
        """
        Clicks on the 'Sign in' option in the navigation menu

        Returns:
            LoginPage: Returns an instance of the LoginPage class
        """
        logging.info("Navigating to the 'Hello, sign in' option")
        self.page.locator(HomePageLocators.CUSTOMER_PROFILE_OPTION).first.click()

        self.wait_for_page_load()

        return LoginPage(self.page)

    def select_option_from_menu(self, menu: str, option: str) -> "HomePage":
        """
        Selects an option from the given menu in the navigation panel

        Args:
            menu (str): The name of the menu to select
            option (str): The option to choose from within the menu

        Returns:
            HomePage: Returns the current instance
        """
        logging.info("Selecting the '%s' option from the '%s' menu", option, menu)

        self.page.wait_for_selector(
            selector=HomePageLocators.MENU_LIST, state="visible"
        )

        #
        # Explicit wait that prevents unexpected popup behavior
        #
        self.page.wait_for_timeout(TimeConstants.POP_UP_EXPLICIT_WAIT)

        menu_list = self.page.locator(HomePageLocators.MENU_LIST)
        visible_menu_element = self.find_visible_element(menu_list, menu)

        option_list = visible_menu_element.locator(HomePageLocators.OPTION_LIST)
        visible_option_element = self.find_visible_element(option_list, option)

        visible_option_element.click()

        #
        # Explicit wait that prevents unexpected popup behavior
        #
        self.page.wait_for_timeout(TimeConstants.POP_UP_EXPLICIT_WAIT)

        return self

    def select_product_type_from_option(self, product_type: str) -> ProductsPage:
        """
        Selects a product type from a category option

        Args:
            product_type (str): The name of the product type to select

        Returns:
            ProductsPage: Returns an instance of the ProductsPage class
        """
        logging.info(
            "Selecting the '%s' product type from the given option", product_type
        )

        self.page.wait_for_selector(
            selector=HomePageLocators.PRODUCT_TYPE_LIST, state="visible"
        )

        product_type_list = self.page.locator(HomePageLocators.PRODUCT_TYPE_LIST)
        visible_product_type_element = self.find_visible_element(
            product_type_list, product_type
        )

        visible_product_type_element.click(force=True)
        self.wait_for_page_load()

        return ProductsPage(self.page)
