"""Module for initializing the base page"""

import os
import logging
from typing import TypeVar
from dotenv import load_dotenv
from playwright.sync_api import Page, Locator, ElementHandle


load_dotenv()

AbstractPage = TypeVar("AbstractPage", bound="BasePage")


class BasePage:
    """A base class for all web pages"""

    def __init__(self, page: Page) -> None:
        """
        Initializes the BasePage with a Playwright Page instance

        Args:
            page (Page): The Playwright page object representing the current browser context
        """
        self.page = page

    def find_visible_element(self, locator: Locator, name: str) -> ElementHandle | None:
        """
        Finds the first visible element from the given locator that matches the specified name

        Args:
            locator (Locator): The Playwright locator to find elements
            name (str): The text content of the element to match

        Returns:
            ElementHandle | None: The first visible element with the matching text, or None if not found
        """
        logging.info(
            "Finding the first visible element from the given locator that matches '%s'",
            name,
        )
        elements = locator.all()

        return next(
            (
                element
                for element in elements
                if element.is_visible() and element.inner_text() == name
            ),
            None,
        )

    def wait_for_page_load(self) -> None:
        """
        Waits for the page to fully load by ensuring the document ready state is 'complete'
        """
        logging.info("Waiting for the page to reload")
        self.page.wait_for_function("document.readyState === 'complete'")

    def navigate_to_website(self: AbstractPage) -> AbstractPage:
        """
        Navigates to the website's base URL

        Returns:
            AbstractPage: Returns the current instance or any subclass

        Raises:
            ValueError: If the WEBSITE_URL is not set in environment variables
        """
        website_url: str | None = os.getenv("WEBSITE_URL")

        if website_url:
            logging.info("Navigating to the website '%s'", website_url)
            self.page.goto(website_url)
        else:
            raise ValueError("The website URL is not set in the env variables")

        return self

    def reload_page(self: AbstractPage) -> AbstractPage:
        """
        Reloads the current page

        Returns:
            AbstractPage: Returns the current instance or any subclass
        """
        logging.info("Reloading the website")
        self.page.reload()

        return self
