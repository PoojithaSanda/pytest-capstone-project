# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage

# class LoginPage(BasePage):

#     EMAIL = (By.XPATH, "//input[@type='email']")
#     PASSWORD = (By.XPATH, "//input[@type='password']")
#     LOGIN_BTN = (By.XPATH, "//*[@id="root"]/div/div/div/div[1]/div[1]/a[1]")

#     def login(self, email, password):
#         self.send_keys(self.EMAIL, email)
#         self.send_keys(self.PASSWORD, password)
#         self.click(self.LOGIN_BTN)
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