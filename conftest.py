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


# ENV FIXTURE
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


# CONFIG FIXTURE
@pytest.fixture(scope="session")
def config(env):
    return get_config(env)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser(playwright_instance, config):
    browser_type = config["browser"]
    headless = config["headless"]

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

    context.set_default_timeout(config["timeout"])

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
