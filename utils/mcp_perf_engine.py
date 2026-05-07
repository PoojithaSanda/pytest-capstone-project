import random
import time
from selenium.webdriver.common.by import By

# SIMPLE DATA GENERATOR
class LLMDataGenerator:

    @staticmethod
    def generate_note():
        categories = ["Home", "Work", "Personal"]

        timestamp = int(time.time())

        return {
            "title": "AI Note " + str(timestamp),
            "description": "Generated test note",
            "category": random.choice(categories)
        }


# SIMPLE PERFORMANCE CHECK
class PerformanceMonitor:

    MAX_TIME = 20

    @staticmethod
    def evaluate_response(response):

        response_time = response.elapsed.total_seconds()

        print("Response Time:", response_time, "sec")

        if response_time < 2:
            print("Excellent")
        elif response_time < 5:
            print("Good")
        elif response_time < 10:
            print("Average")
        else:
            print("Slow")

        assert response_time < PerformanceMonitor.MAX_TIME


# SIMPLE FAILURE CHECKER
class FailureAnalyzer:

    @staticmethod
    def analyze(error_message):

        msg = str(error_message)

        if "NoSuchElementException" in msg:
            return "Locator issue"

        if "TimeoutException" in msg:
            return "Timeout issue"

        if "ElementClickInterceptedException" in msg:
            return "Click blocked"

        if "AssertionError" in msg:
            return "Assertion failed"

        return "Unknown error"


# SIMPLE LOCATOR HELPER
class LocatorAdvisor:

    @staticmethod
    def suggest(locator):

        by, value = locator

        if by == By.XPATH:
            return ["Avoid XPath, use ID or CSS"]

        if by == By.CLASS_NAME:
            return ["Class may change, use ID"]

        if by == By.CSS_SELECTOR:
            return ["Check CSS stability"]

        if by == By.ID:
            return ["Good locator"]

        return ["OK locator"]