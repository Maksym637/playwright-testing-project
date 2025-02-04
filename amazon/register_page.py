"""Module for initializing the register page"""

import logging
from playwright.sync_api import Page
from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    """Represents the register page"""

    def __init__(self, page: Page) -> None:
        """
        Initializes the RegisterPage with a Playwright Page instance

        Args:
            page (Page): The Playwright page object representing the current browser context
        """
        super().__init__(page)

    def enter_name(self, name: str) -> "RegisterPage":
        """
        Enters the given name into the name input field

        Args:
            name (str): The name to be entered

        Returns:
            RegisterPage: Returns the current instance
        """
        logging.info("Entering name '%s'", name)
        input_name = self.page.locator(RegisterPageLocators.NAME_INPUT)

        input_name.clear()
        input_name.fill(name)

        return self

    def enter_email(self, email: str) -> "RegisterPage":
        """
        Enters the given email into the email input field

        Args:
            email (str): The email address to be entered

        Returns:
            RegisterPage: Returns the current instance
        """
        logging.info("Entering email '%s'", email)
        input_email = self.page.locator(RegisterPageLocators.EMAIL_INPUT)

        input_email.clear()
        input_email.fill(email)

        return self

    def enter_password(self, password: str) -> "RegisterPage":
        """
        Enters the given password into the password input field

        Args:
            password (str): The password to be entered

        Returns:
            RegisterPage: Returns the current instance
        """
        logging.info("Entering password '%s'", password)
        input_password = self.page.locator(RegisterPageLocators.PASSWORD_INPUT)

        input_password.clear()
        input_password.fill(password)

        return self

    def re_enter_password(self, password: str) -> "RegisterPage":
        """
        Re-enters the password into the re-password input field

        Args:
            password (str): The password to be entered

        Returns:
            RegisterPage: Returns the current instance
        """
        logging.info("Entering re-password '%s'", password)
        input_password_check = self.page.locator(
            RegisterPageLocators.PASSWORD_CHECK_INPUT
        )

        input_password_check.clear()
        input_password_check.fill(password)

        return self

    def click_continue_verify_button(self) -> "RegisterPage":
        """
        Clicks on the 'Continue/Verify email' button

        Returns:
            RegisterPage: Returns the current instance
        """
        logging.info("Clicking on the 'Continue/Verify email' button")
        self.page.locator(RegisterPageLocators.CONTINUE_VERIFY_BUTTON).click()

        return self

    def get_error_messages(self) -> list[str]:
        """
        Retrieves all visible error messages from the page

        Returns:
            list[str]: A list of error messages displayed on the page
        """
        logging.info("Getting all error messages")
        error_messages = self.page.locator(RegisterPageLocators.ERROR_MESSAGES).all()

        visible_error_messages = [
            element.text_content().strip()
            for element in error_messages
            if element.is_visible()
        ]

        return visible_error_messages
