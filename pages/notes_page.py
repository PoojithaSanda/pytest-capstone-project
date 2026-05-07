from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class NotesPage(BasePage):

    # 🔥 FIXED LOCATORS (VERY IMPORTANT)
    ADD_BTN = (By.XPATH, "//button[contains(.,'Add Note')]")
    TITLE = (By.XPATH, "//input[@placeholder='Title']")
    DESC = (By.XPATH, "//textarea[@placeholder='Description']")
    SAVE = (By.XPATH, "//button[contains(.,'Save')]")

    def create_note(self, title, desc):

        # Wait for dashboard to fully load
        self.wait.until(
            EC.visibility_of_element_located(self.ADD_BTN)
        )

        # 🔥 Force click (ensures modal opens)
        self.driver.execute_script(
            "arguments[0].click();",
            self.wait.until(EC.element_to_be_clickable(self.ADD_BTN))
        )

        print("✅ Add button clicked")

        # 🔥 Wait until modal is actually visible
        self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )

        print("✅ Modal opened")

        # Enter data
        self.send_keys(self.TITLE, title)
        self.send_keys(self.DESC, desc)

        # Save note
        self.click(self.SAVE)

        print("✅ Note saved")