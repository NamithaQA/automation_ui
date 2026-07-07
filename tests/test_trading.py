import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


def test_trading_functionality(page, config):
    """Test trading func, verify spot trading section is rendered, trading pair entries contain expected data"""
    home = HomePage(page)
    home.goto(config["base_url"])
    page.get_by_role("link", name="Explore").first.click()
    expect(page.get_by_role("heading", name="Spot market")).to_be_visible(timeout=7000)
    expect(page.get_by_text("Discover our cryptocurrency")).to_be_visible()

    ## Verify different trade categories are present
    expect(page.get_by_role("button", name="Hot")).to_be_visible()
    expect(page.get_by_role("button", name="Gainers")).to_be_visible()
    expect(page.get_by_role("button", name="Losers")).to_be_visible()

    ## Get table data for Display Name
    display = page.locator("//tbody[@class='bg-neutral-social']/tr/td[1]")
    for i in range(1, display.count()):
        expect(page.locator("//tbody[@class='bg-neutral-social']/tr/td[1]").nth(i)).to_be_visible()
        d = page.locator("//tbody[@class='bg-neutral-social']/tr/td[1]").nth(i).all_inner_texts()

    ## Get table data for price
    price = page.locator("//tbody[@class='bg-neutral-social']/tr/td[2]")
    for i in range(1, price.count()):
        expect(page.locator("//tbody[@class='bg-neutral-social']/tr/td[2]").nth(i)).to_be_visible()
        d = page.locator("//tbody[@class='bg-neutral-social']/tr/td[2]").nth(i).all_inner_texts()
        assert d[0].startswith("$"), "Price is not starting with $"

    ## Get table data for % change
    change = page.locator("//tbody[@class='bg-neutral-social']/tr/td[3]")
    for i in range(1, change.count()):
        expect(page.locator("//tbody[@class='bg-neutral-social']/tr/td[3]").nth(i)).to_be_visible()
        d = page.locator("//tbody[@class='bg-neutral-social']/tr/td[3]").nth(i).all_inner_texts()
        assert d[0].endswith("%"), "Change is not ending with %"
