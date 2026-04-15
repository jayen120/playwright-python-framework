import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open(BASE_URL)
    return lp