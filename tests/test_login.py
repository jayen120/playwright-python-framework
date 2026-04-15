import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL
from tests.test_data import valid_users, empty_users, invalid_users


@pytest.mark.parametrize("username,password", valid_users)
def test_login_valid(login_page, username, password):
    login_page.login(username, password)
    assert login_page.is_inventory_page_visible()


@pytest.mark.parametrize("username,password,expected_error", invalid_users)
def test_login_invalid(login_page, username, password, expected_error):
    login_page.login(username, password)
    error = login_page.get_error()
    assert expected_error in error.lower()


@pytest.mark.parametrize("username,password", empty_users)
def test_login_empty(login_page, username, password):
    login_page.login(username, password)
    error = login_page.get_error()
    assert "required" in error.lower()

