from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)

    def enter_email(self, email: str) -> "LoginPage":
        self.wait_for_page_load()
        self.page.locator(LoginPageLocators.EMAIL_INPUT).fill(email)
        return self

    def click_continue_button(self) -> "LoginPage":
        self.page.locator(LoginPageLocators.CONTINUE_BUTTON).click()
        return self

    def get_error_message(self) -> str:
        self.page.wait_for_selector(
            selector=LoginPageLocators.ERROR_MESSAGE, state="visible"
        )
        return self.page.locator(LoginPageLocators.ERROR_MESSAGE).text_content().strip()
