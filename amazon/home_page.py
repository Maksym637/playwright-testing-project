"""Module for initializing the home page"""

from playwright.sync_api import expect
from .base_page import BasePage
from .login_page import LoginPage
from .products_page import ProductsPage
from .locators import HomePageLocators
from utils.constants import TimeConstants


class HomePage(BasePage):
    """Represents the home page"""

    def __init__(self, page) -> None:
        """
        Initializes the HomePage with a Playwright Page instance

        Args:
            page (Page): The Playwright page object representing the current browser context
        """
        super().__init__(page)

    def go_to_language_icon(self) -> "HomePage":
        language_icon = self.page.locator(HomePageLocators.LANGUAGE_ICON)

        # TODO explanation
        for _ in range(3):
            language_icon.hover()

        return self

    def select_language(self, lang: str, iso: str) -> "HomePage":
        self.page.wait_for_selector(
            selector=HomePageLocators.LANGUAGE_OPTION(lang, iso), state="visible"
        )
        self.page.locator(HomePageLocators.LANGUAGE_OPTION(lang, iso)).click()
        expect(self.page.locator(HomePageLocators.LANGUAGE_ICON)).to_have_text(
            lang.upper()
        )
        return self

    def get_nav_bar_items(self) -> list[str]:
        nav_bar_items = self.page.locator(HomePageLocators.NAV_BAR_ITEMS).all()

        visible_nav_bar_items = [
            element.text_content().strip()
            for element in nav_bar_items
            if element.is_visible()
        ]

        return visible_nav_bar_items[0:-1]

    def go_to_all_menu(self) -> "HomePage":
        """
        Clicks on the hamburger menu to open the navigation menu

        Returns:
            HomePage: Returns the current instance
        """
        self.page.locator(HomePageLocators.NAV_HAMBURGER_MENU).click()
        return self

    def go_to_sign_in_option(self) -> LoginPage:
        """
        Clicks on the 'Sign in' option in the navigation menu

        Returns:
            LoginPage: Returns an instance of the LoginPage class
        """
        self.page.locator(HomePageLocators.CUSTOMER_PROFILE_OPTION).first.click()
        self.wait_for_page_load()
        return LoginPage(self.page)

    def select_option_from_menu(self, menu: str, option: str) -> "HomePage":
        self.page.wait_for_selector(
            selector=HomePageLocators.MENU_LIST, state="visible"
        )

        # TODO explanation
        self.page.wait_for_timeout(TimeConstants.POP_UP_EXPLICIT_WAIT)

        menu_list = self.page.locator(HomePageLocators.MENU_LIST)
        visible_menu_element = self.find_visible_element(menu_list, menu)

        option_list = visible_menu_element.locator(HomePageLocators.OPTION_LIST)
        visible_option_element = self.find_visible_element(option_list, option)

        visible_option_element.click()

        # TODO explanation
        self.page.wait_for_timeout(TimeConstants.POP_UP_EXPLICIT_WAIT)

        return self

    def select_product_type_from_option(self, product_type: str) -> ProductsPage:
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
