import pytest
from playwright.sync_api import sync_playwright

from utils.config import BROWSER, HEADLESS, VIEWPORT, TIMEOUT


@pytest.fixture(scope="session")
def playwright_instance():
    """
    Starts Playwright once for the entire test session.
    """
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser(playwright_instance):
    """
    Launches the browser before each test and closes it afterwards.
    """
    if BROWSER.lower() == "chromium":
        browser = playwright_instance.chromium.launch(headless=HEADLESS)

    elif BROWSER.lower() == "firefox":
        browser = playwright_instance.firefox.launch(headless=HEADLESS)

    elif BROWSER.lower() == "webkit":
        browser = playwright_instance.webkit.launch(headless=HEADLESS)

    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    yield browser

    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """
    Creates a new browser context for each test.
    """
    context = browser.new_context(
        viewport=VIEWPORT
    )

    context.set_default_timeout(TIMEOUT)

    yield context

    context.close()


@pytest.fixture(scope="function")
def page(context):
    """
    Creates a new page for each test.
    """
    page = context.new_page()

    yield page

    page.close()