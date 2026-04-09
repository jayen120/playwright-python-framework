from playwright.sync_api import Page


def test_login_valid(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    # page.locator('[data-test="username"]').fill("standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    #Assertion (important)
    assert "inventory" in page.url

def test_login_invalid(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    error = page.locator('[data-test="error"]').inner_text()

    assert "locked out" in error.lower()

def test_login_empty(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.click("#login-button")
    
    error = page.locator('[data-test="error"]').inner_text()
    
    assert "required" in error.lower()

