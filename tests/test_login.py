import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL
from tests.test_data import valid_users, empty_users, invalid_users, security_test_data


@pytest.mark.smoke
@pytest.mark.parametrize("username,password", valid_users)
def test_login_valid(login_page, username, password):
    login_page.login(username, password)
    assert login_page.is_inventory_page_visible()

@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected_error", invalid_users)
def test_login_invalid(login_page, username, password, expected_error):
    login_page.login(username, password)
    error = login_page.get_error()
    assert expected_error in error.lower()

@pytest.mark.regression
@pytest.mark.parametrize("username,password", empty_users)
def test_login_empty(login_page, username, password):
    login_page.login(username, password)
    error = login_page.get_error()
    assert "required" in error.lower()

@pytest.mark.security
@pytest.mark.parametrize("username,password,expected", security_test_data)
def test_sql_injection(login_page, username, password, expected):
    login_page.login(username, password)

    error = login_page.get_error()

    # System should not allow login
    assert "epic sadface" in error.lower()

@pytest.mark.security
def test_bruteforce_attempt(login_page):
    for _ in range(5):
        login_page.login("standard_user", "wrong_password")

    error = login_page.get_error()

    # System should not allow login
    assert "sadface" in error.lower()
