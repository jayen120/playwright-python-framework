from utils.logger import get_logger

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

        # Locators
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = '[data-test="error"]'

    def open(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.page.goto(url)

    # Actions
    def login(self, username, password):
        self.logger.info(f"Attempting login with user: {username}")

        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error(self):
        self.logger.info("Fetching error message")
        self.logger.warning("Login failed, fetching error message")
        return self.page.locator(self.error_message).inner_text()
    
    def is_inventory_page_visible(self):
        self.logger.info("Checking if inventory page is visible")
        # self.page.wait_for_selector(self.inventory_list)
        return self.page.locator(".inventory_list").is_visible()

