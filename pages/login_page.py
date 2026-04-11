class LoginPage:
    def __init__(self, page):
        self.page = page

    # Locators
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = '[data-test="error"]'

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    #Actions
    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()
    
    def is_inventory_page_visible(self):
        self.page.wait_for_selector(".inventory_list")
        return self.page.locator(".inventory_list").is_visible()
        