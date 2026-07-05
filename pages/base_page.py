from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    #Basic actions
    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator, timeout = 5000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

   # assertions
    def assert_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def assert_text(self, locator, expected_text):
        expect(self.page.locator(locator)).to_have_text(expected_text)

    def assert_url_contains(self, text):
        expect(self.page).to_have_url(lambda url: text in url)
