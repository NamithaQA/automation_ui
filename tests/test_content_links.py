import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.parametrize(("nav", "nav_url"), [
    ('Explore', '/explore'),
    ('Features', '/features'),
    ('OTC Desk', '/features/otc-desk'),
    ('Company', '/company'),
    ('$MBG', '/token.mb.io')
])
def test_navigation(page, config, nav, nav_url):
    """Test Nav bar exists, all menu items are visible, nav items are linked correctly"""
    home = HomePage(page)
    home.goto(config["base_url"])
    expect(page).to_have_url(config["base_url"] + "en-AE")
    expect(page.get_by_role("navigation", name="Main")).to_be_visible()  # Check Nav is visible

    if nav == "$MBG":  # MBG nav item opens a new tab
        with page.expect_popup() as mbg_page:
            page.get_by_role("link", name=nav, exact=True).first.click()
        assert nav_url in mbg_page.value.url, "MBG redirected to wrong URL"
    else:
        expect(page.get_by_role('link', name=nav).first).to_be_visible()  # Nav items are visible
        page.get_by_role('link', name=nav).first.click()  # Click Nav item
        expect(page).to_have_url(config["base_url"] + "en-AE" + nav_url)  # Verify nav item redirection
