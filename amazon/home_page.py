"""Module for initializing the home page"""

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

        return ProductsPage(self.page)
