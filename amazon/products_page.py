"""Module for initializing the products page"""

import logging
from playwright.sync_api import Page
from .base_page import BasePage
from .locators import ProductsPageLocators


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
