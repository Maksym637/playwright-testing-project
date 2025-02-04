import logging
import pytest
from typing import Generator
from pytest import FixtureRequest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="function")
def browser(request: FixtureRequest) -> Generator[Page, None, None]:
    test_name = request.node.name

    with sync_playwright() as playwright:
        logging.info("Starting the '%s' test", test_name)
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)

        yield page

        logging.info("Finishing the '%s' test", test_name)
        page.close()
        browser.close()
