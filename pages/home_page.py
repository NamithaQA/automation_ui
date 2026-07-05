from pages.base_page import BasePage
class HomePage(BasePage):

    def open(self, config):
        self.goto(config["base_url"])
