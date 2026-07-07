import os
import pytest
from playwright.sync_api import sync_playwright

from utils.config import get_config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against: qa, uat, prod"
    )

    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests against: chromium, firefox, webkit"
    )


# ENV FIXTURE
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


# CONFIG FIXTURE
@pytest.fixture(scope="session")
def config(env):
    return get_config(env)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser(playwright_instance, config, browser_name):
    browser_type = browser_name
    headless = config["headless"]

    if os.getenv("CI") == "true":
        headless = True

    if browser_type == "chromium":
        browser = playwright_instance.chromium.launch(headless=headless)

    elif browser_type == "firefox":
        browser = playwright_instance.firefox.launch(headless=headless)

    elif browser_type == "webkit":
        browser = playwright_instance.webkit.launch(headless=headless)

    else:
        raise ValueError(f"Unsupported browser: {browser_type}")

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, config):
    context = browser.new_context(
        viewport=config["viewport"]
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    context.tracing.stop(path="reports/trace.zip")
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
