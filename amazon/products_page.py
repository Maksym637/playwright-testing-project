"""Module for initializing the products page"""

import logging
from playwright.sync_api import Page
from .base_page import BasePage
from .locators import ProductsPageLocators
from utils.constants import TimeConstants


class ProductsPage(BasePage):
    """Represents the products page"""

    def __init__(self, page: Page) -> None:
        """
        Initializes the ProductsPage with a Playwright Page instance

        Args:
            page (Page): The Playwright page object representing the current browser context
        """
        super().__init__(page)

    def get_products_number(self) -> int:
        """
        Retrieves the total number of products listed on the page

        Returns:
            int: The number of products displayed on the page
        """
        logging.info("Getting the number of all products")
        return len(self.page.locator(ProductsPageLocators.PRODUCT_LIST).all())

    def select_first_product(self) -> "ProductsPage":
        """
        Selects the first available product from the product list

        Returns:
            ProductsPage: Returns the current instance
        """
        logging.info("Selecting the first product")

        #
        # Explicit wait that prevents the item from not being clicked
        #
        self.page.wait_for_timeout(TimeConstants.ITEM_EXPLICIT_WAIT)

        self.page.locator(ProductsPageLocators.PRODUCT_LIST).all()[0].click(force=True)
        self.wait_for_page_load()

        return self

    def get_product_title(self) -> str:
        """
        Retrieves the product title on the products page

        Returns:
            str: The text content of the product title
        """
        logging.info("Getting the product title")
        return (
            self.page.locator(ProductsPageLocators.PRODUCT_TITLE).text_content().strip()
        )

    def click_add_to_cart_button(self) -> "ProductsPage":
        """
        Clicks on the 'Add to Cart' button

        Returns:
            ProductsPage: Returns the current instance
        """
        logging.info("Clicking on the 'Add to Cart' button")
        self.page.locator(ProductsPageLocators.ADD_TO_CART_BUTTON).click()

        return self
