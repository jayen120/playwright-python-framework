from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD, BASE_URL

# def test_login_valid(page: Page):
def test_login_valid(page):
    login_page = LoginPage(page)
    
    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_inventory_page_visible()

def test_login_invalid(page):
    login_page = LoginPage(page)
    
    login_page.open(BASE_URL)
    login_page.login("locked_out_user", PASSWORD)
    
    error = login_page.get_error()
    assert "locked out" in error.lower()

def test_login_empty(page):
    login_page = LoginPage(page)
    
    login_page.open(BASE_URL)
    login_page.login("", "")
    
    error = login_page.get_error()
    assert "username is required" in error.lower()

