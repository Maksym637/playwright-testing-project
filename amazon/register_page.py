import logging
from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    def enter_name(self, name: str) -> "RegisterPage":
        logging.info("Entering name '%s'", name)
        input_name = self.page.locator(RegisterPageLocators.NAME_INPUT)

        input_name.clear()
        input_name.fill(name)

        return self

    def enter_email(self, email: str) -> "RegisterPage":
        logging.info("Entering email '%s'", email)
        input_email = self.page.locator(RegisterPageLocators.EMAIL_INPUT)

        input_email.clear()
        input_email.fill(email)

        return self

    def enter_password(self, password: str) -> "RegisterPage":
        logging.info("Entering password '%s'", password)
        input_password = self.page.locator(RegisterPageLocators.PASSWORD_INPUT)

        input_password.clear()
        input_password.fill(password)

        return self

    def re_enter_password(self, password: str) -> "RegisterPage":
        logging.info("Entering re-password '%s'", password)
        input_password_check = self.page.locator(
            RegisterPageLocators.PASSWORD_CHECK_INPUT
        )

        input_password_check.clear()
        input_password_check.fill(password)

        return self

    def click_continue_verify_button(self) -> "RegisterPage":
        logging.info("Clicking on the 'Continue/Verify email' button")
        self.page.locator(RegisterPageLocators.CONTINUE_VERIFY_BUTTON).click()

        return self

    def get_error_messages(self) -> list[str]:
        logging.info("Getting all error messages")
        error_messages = self.page.locator(RegisterPageLocators.ERROR_MESSAGES).all()

        visible_error_messages = [
            element.text_content().strip()
            for element in error_messages
            if element.is_visible()
        ]

        return visible_error_messages
