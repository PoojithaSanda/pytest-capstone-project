import time
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AgenticEngine:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # SELF-HEALING LOCATOR SYSTEM
    def find_element(self, primary_locator, fallback_locators=[]):

        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(primary_locator)
            )

        except Exception:

            # TRY FALLBACK LOCATORS
            for locator in fallback_locators:
                try:
                    return WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(locator)
                    )
                except Exception:
                    continue

            raise Exception("Element not found using any locator strategy")

    # AUTO RETRY MECHANISM
    def safe_click(self, locator, retries=3):

        for attempt in range(retries):

            try:
                element = self.driver.find_element(*locator)
                element.click()
                return True

            except (StaleElementReferenceException, Exception):

                time.sleep(1)

        raise Exception("Click failed after retries")

    # INTELLIGENT WAIT SYSTEM
    def smart_wait(self, condition_func, timeout=10):

        end_time = time.time() + timeout

        while time.time() < end_time:

            if condition_func():
                return True

            time.sleep(0.5)

        raise TimeoutException("Smart wait failed")

    # DECISION BASED RETRY (AI STYLE LOGIC)
    def execute_with_recovery(self, action_func, retries=2):

        for attempt in range(retries):

            try:
                return action_func()

            except Exception as e:

                print(f"[Agentic Retry] Attempt {attempt+1} failed: {e}")
                time.sleep(2)

        raise Exception("Agentic execution failed after retries")