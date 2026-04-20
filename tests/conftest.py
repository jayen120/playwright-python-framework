import os
import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL


def pytest_configure():
    print(f"\nRunning tests in ENV: {os.getenv('ENV', 'dev')}\n")

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open(BASE_URL)
    return lp