from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # First click login button (IMPORTANT)
    LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Login')]")

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Login')]")

    def login(self, email, password):
        # Click login button first
        self.click(self.LOGIN_BTN)

        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.SUBMIT)
