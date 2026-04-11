from playwright.sync_api import Page
from pages.login_page import LoginPage

# def test_login_valid(page: Page):
def test_login_valid(page):
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_inventory_page_visible()

def test_login_invalid(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("locked_out_user", "secret_sauce")
    
    error = login_page.get_error_message()
    
    assert "Sorry, this user has been locked out." in error

def test_login_empty(page):
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("", "")
    error = login_page.get_error_message()


    assert "required" in error.lower()

