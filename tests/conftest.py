import os
import pytest
from pages.login_page import LoginPage
from utils.config import BASE_URL
from pytest_html import extras

def pytest_configure():
    print(f"\nRunning tests in ENV: {os.getenv('ENV', 'dev')}\n")

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open(BASE_URL)
    return lp

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Run only after test execution
    if report.when == "call":

        # Get login_page fixture
        login_page = item.funcargs.get("login_page", None)

        # Extract actual Playwright page
        page = login_page.page if login_page else None

        if page and report.failed:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Take screenshot
            page.screenshot(path=file_path)

            # Attach to HTML report
            extras_list = getattr(report, "extras", [])
            extras_list.append(extras.image(file_path))
            report.extras = extras_list

            print(f"\nScreenshot saved: {file_path}")