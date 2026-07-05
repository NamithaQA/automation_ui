import pytest
from pages.home_page import HomePage


@pytest.mark.parametrize("nav_url", ['/explore',
                                     '/features',
                                     '/features/otc-desk',
                                     '/company',
                                     # ('mbg', '' )
                                     ])
def test_navigation(page, config, nav_url):
    home = HomePage(page)
    home.goto(config["base_url"])
    assert page.url == config["base_url"] + "en-AE", "Home page opened is wrong"

    home.assert_visible(f"(//a[@href='/en-AE{nav_url}'])[1]")
    home.click(f"(//a[@href='/en-AE{nav_url}'])[1]")
    page.wait_for_url(f"**{nav_url}")
    assert page.url == config["base_url"] + "en-AE" + nav_url.lower(), "Nav page navigated is wrong"



