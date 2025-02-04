import logging
from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductsPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    def get_products_number(self) -> int:
        logging.info("Getting the number of all products")
        return len(self.page.locator(ProductsPageLocators.PRODUCT_LIST).all())
