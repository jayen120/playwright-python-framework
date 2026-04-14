from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    # Locators
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = '[data-test="error"]'
    inventory_list = ".inventory_list"


    #Actions
    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error(self):
        return self.get_text(self.error_message)
    
    def is_inventory_page_visible(self):
        self.page.wait_for_selector(self.inventory_list)
        return self.page.locator(self.inventory_list).is_visible()
        