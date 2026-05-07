from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

# AGENTIC RETRY ENGINE (CORE LOGIC)
    def retry(self, action, retries=3):

        for attempt in range(retries):

            try:
                return action()

            except (StaleElementReferenceException, Exception) as e:
                print(f"[Agentic Retry] Attempt {attempt + 1} failed: {e}")
                time.sleep(1)

        raise Exception("Action failed after retries")

# SELF-HEALING LOCATOR SUPPORT
    def find_element(self, primary_locator, fallback_locators=[]):

        try:
            return self.wait.until(
                EC.presence_of_element_located(primary_locator)
            )

        except Exception:

            for locator in fallback_locators:

                try:
                    return self.wait.until(
                        EC.presence_of_element_located(locator)
                    )
                except:
                    continue

            raise Exception("Element not found using any locator strategy")

    # CLOSE POPUP (SAFE)

    def close_popup(self):

        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(@class,'close') or contains(text(),'Close')]"
                    )
                )
            )
            popup.click()
            print("Popup closed")

        except:
            pass

# CLICK (AGENTIC + STABLE)

    def click(self, locator):

        def action():

            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

            try:
                element.click()
            except:
                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

        self.retry(action)

# SEND KEYS (AGENTIC + STABLE)
    def send_keys(self, locator, value):

        def action():

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

            element.clear()
            element.send_keys(value)

        self.retry(action)

# GET TEXT
    def get_text(self, locator):

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.text

        except TimeoutException:
            raise Exception(f"Unable to get text from: {locator}")

# IS VISIBLE
    def is_visible(self, locator):

        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True

        except:
            return False

# WAIT FOR ELEMENT
    def wait_for_element(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
# SMART WAIT (INTELLIGENT WAITING SYSTEM)
    def smart_wait(self, condition, timeout=10):

        end_time = time.time() + timeout

        while time.time() < end_time:

            if condition():
                return True

            time.sleep(0.5)

        raise TimeoutException("Smart wait failed")

    # SCROLL TO ELEMENT
    def scroll_to_element(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        return element

    # REFRESH PAGE
    def refresh_page(self):

        self.driver.refresh()

    # JS CLICK (FALLBACK ONLY)
    def js_click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )