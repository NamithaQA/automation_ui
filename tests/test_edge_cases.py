import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


def test_broken_link_detection(page, config):
    """Find all the links and click on the click and verify link redirects to correct page"""
    home = HomePage(page)
    home.goto(config["base_url"])

    # click on Company nav item
    page.get_by_role("link", name="Company", exact=True).first.click()

    # Find all the links in bottom list and verify links redirect to correct page
    list_l = page.locator("//ul[@role='list']").locator("li a")
    for i in range(list_l.count()):
        link = page.locator("//ul[@role='list']").locator("li a").nth(i).get_attribute("href")

        s = page.locator("//ul[@role='list']").locator("li a").nth(i).click()
        expect(page).to_have_url(f"https://mb.io{link}")

def test_invalid_route_handling(page, config):
    """Navigate to some wrong url and verify response is as expected"""
    home = HomePage(page)
    home.goto(config["base_url"])

    # click on Company nav item
    wrong =  page.goto(config["base_url"]+"logs")
    assert wrong.status == 404, "Status is not 404, should be 404 for wrong url"

