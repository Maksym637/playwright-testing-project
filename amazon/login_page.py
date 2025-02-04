import logging
from .base_page import BasePage
from .register_page import RegisterPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    def enter_email(self, email: str) -> "LoginPage":
        logging.info("Entering email '%s'", email)
        self.page.locator(LoginPageLocators.EMAIL_INPUT).fill(email)

        return self

    def click_continue_button(self) -> "LoginPage":
        logging.info("Clicking on the 'Continue' button")
        self.page.locator(LoginPageLocators.CONTINUE_BUTTON).click()

        return self

    def get_error_message(self) -> str:
        logging.info("Getting an error message")
        self.page.wait_for_selector(
            selector=LoginPageLocators.ERROR_MESSAGE, state="visible"
        )

        return self.page.locator(LoginPageLocators.ERROR_MESSAGE).text_content().strip()

    def go_to_register_option(self) -> "RegisterPage":
        logging.info("Navigating to the 'Create your Amazon account' option")
        self.page.locator(LoginPageLocators.CREATE_USER_BUTTON).click()

        self.wait_for_page_load()

        return RegisterPage(self.page)
