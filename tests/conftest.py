"""Module for setting up the Playwright browser fixture for tests"""

import logging
import pytest
from typing import Generator
from pytest import FixtureRequest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="function")
def browser(request: FixtureRequest) -> Generator[Page, None, None]:
    """
    Pytest fixture for initializing and tearing down a Playwright browser instance

    Args:
        request (FixtureRequest): Pytest fixture request object that provides test metadata

    Yields:
        Page: A Playwright page instance for interaction during the test
    """
    test_name = request.node.name

    with sync_playwright() as playwright:
        logging.info("Starting the '%s' test", test_name)
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)

        yield page

        logging.info("Finishing the '%s' test", test_name)
        page.close()
        browser.close()
