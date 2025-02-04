"""Module for initializing the login page"""

import logging
from playwright.sync_api import Page
from .base_page import BasePage
from .register_page import RegisterPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Represents the login page"""

    def __init__(self, page: Page) -> None:
        """
        Initializes the LoginPage with a Playwright Page instance

        Args:
            page (Page): The Playwright page object representing the current browser context
        """
        super().__init__(page)

    def enter_email(self, email: str) -> "LoginPage":
        """
        Enters the given email into the email input field

        Args:
            email (str): The email address to be entered

        Returns:
            LoginPage: Returns the current instance
        """
        logging.info("Entering email '%s'", email)
        self.page.locator(LoginPageLocators.EMAIL_INPUT).fill(email)

        return self

    def click_continue_button(self) -> "LoginPage":
        """
        Clicks on the 'Continue' button

        Returns:
            LoginPage: Returns the current instance
        """
        logging.info("Clicking on the 'Continue' button")
        self.page.locator(LoginPageLocators.CONTINUE_BUTTON).click()

        return self

    def get_error_message(self) -> str:
        """
        Retrieves the error message displayed on the login page, if any

        Returns:
            str: The text content of the error message
        """
        logging.info("Getting an error message")
        self.page.wait_for_selector(
            selector=LoginPageLocators.ERROR_MESSAGE, state="visible"
        )

        return self.page.locator(LoginPageLocators.ERROR_MESSAGE).text_content().strip()

    def go_to_register_option(self) -> "RegisterPage":
        """
        Clicks on the 'Create your Amazon account' button

        Returns:
            RegisterPage: Returns an instance of the RegisterPage class
        """
        logging.info("Navigating to the 'Create your Amazon account' option")
        self.page.locator(LoginPageLocators.CREATE_USER_BUTTON).click()

        self.wait_for_page_load()

        return RegisterPage(self.page)
