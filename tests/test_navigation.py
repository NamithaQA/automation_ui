import pytest

from pages.home_page import HomePage
from pages.base_page import BasePage


@pytest.mark.parametrize(("nav_name", "url"), [('Explore', '/explore'),
                                             ('Features', '/features'),
                                            ('Otc Desk', '/features/otc_desk'),
                                             ('Company', '/company'),
                                             ('Support', '/support'),
                                             # ('mbg', '' )
                                             ])
def test_navigation(page, config, nav_name, url):
    home = HomePage(page)
    home.goto(config["base_url"])
    assert page.url == config["base_url"]+"en-AE", "Home page opened is wrong"

    BasePage(page).assert_visible(f"(//a[@href='/en-AE{url}'])[1]")
    BasePage(page).click(f"(//a[@href='/en-AE{url}'])[1]")
    BasePage(page).assert_url_contains(config["base_url"] + "en-AE" + url.lower())


