from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ----------------------------
    # Close Popup / Ads
    # ----------------------------
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

    # ----------------------------
    # Click Element (Robust)
    # ----------------------------
    def click(self, locator):

        try:

            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

        # REMOVE ADS / IFRAMES
            self.driver.execute_script("""
                let ads = document.querySelectorAll(
                    'iframe, .adsbygoogle, [id*="google"]'
                );

                ads.forEach(ad => {
                    ad.remove();
                });
            """)

            time.sleep(1)

        # JS CLICK
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

        except TimeoutException:

            raise Exception(
                f"Element not clickable: {locator}"
            )

    # ----------------------------
    # Send Keys
    # ----------------------------
    def send_keys(self, locator, value):

        try:

        # Wait for element
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
        )

        # Scroll to element
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
        )

        # HANDLE ADS / IFRAMES
            try:

                self.driver.switch_to.default_content()

                ads = self.driver.find_elements(By.TAG_NAME, "iframe")

                for ad in ads:

                    try:
                        self.driver.execute_script(
                            "arguments[0].style.display='none';",
                            ad
                    )
                    except:
                        pass

            except:
                pass

        # JS CLICK (better for blocked elements)
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

        # Clear field
            element.clear()

        # Type text
            element.send_keys(value)

        except TimeoutException:

            raise Exception(
                f"Element not ready for typing: {locator}"
        )
    # ----------------------------
    # Get Text
    # ----------------------------
    def get_text(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.text

        except TimeoutException:
            raise Exception(f"Unable to get text from: {locator}")

    # ----------------------------
    # Is Visible
    # ----------------------------
    def is_visible(self, locator):

        try:

            self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except:
            return False

    # ----------------------------
    # Wait For Element
    # ----------------------------
    def wait_for_element(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # ----------------------------
    # Scroll To Element
    # ----------------------------
    def scroll_to_element(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        return element

    # ----------------------------
    # Refresh Page
    # ----------------------------
    def refresh_page(self):

        self.driver.refresh()

    # ----------------------------
    # JS Click
    # ----------------------------
    def js_click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )



# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import time


# class BasePage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 15)  # increased wait

#     # ----------------------------
#     # Click Element (Robust)
#     # ----------------------------
#     def click(self, locator):
#         try:
#             element = self.wait.until(
#                 EC.element_to_be_clickable(locator)   # ✅ FIXED
#             )

#             # Scroll into view
#             self.driver.execute_script(
#                 "arguments[0].scrollIntoView({block: 'center'});", element
#             )

#             time.sleep(0.5)

#             try:
#                 element.click()
#             except:
#                 # Fallback if normal click fails
#                 self.driver.execute_script("arguments[0].click();", element)

#         except TimeoutException:
#             raise Exception(f"Element not clickable: {locator}")

#     # ----------------------------
#     # Send Keys
#     # ----------------------------
#     def send_keys(self, locator, value):
#         try:
#         # 🔥 Wait until element is clickable (IMPORTANT)
#             element = self.wait.until(
#                 EC.element_to_be_clickable(locator)
#             )

#         # Scroll into view
#             self.driver.execute_script(
#                 "arguments[0].scrollIntoView({block: 'center'});", element
#             )

#         # 🔥 Click first to activate field
#             element.click()

#         # Clear and type
#             element.clear()
#             element.send_keys(value)

#         # 🔥 VERIFY text entered (VERY IMPORTANT)
#             entered = element.get_attribute("value")

#             if entered != value:
#             # Fallback using JS (handles stubborn inputs)
#                 self.driver.execute_script(
#                     "arguments[0].value = arguments[1];", element, value
#                 )

#         except TimeoutException:
#             raise Exception(f"Element not ready for typing: {locator}")
#     # ----------------------------
#     # Get Text
#     # ----------------------------
#     def get_text(self, locator):
#         try:
#             element = self.wait.until(
#                 EC.visibility_of_element_located(locator)
#             )
#             return element.text
#         except TimeoutException:
#             raise Exception(f"Unable to get text from: {locator}")

#     # ----------------------------
#     # Is Element Visible
#     # ----------------------------
#     def is_visible(self, locator):
#         try:
#             self.wait.until(
#                 EC.visibility_of_element_located(locator)
#             )
#             return True
#         except:
#             return False

#     # ----------------------------
#     # Wait for Element
#     # ----------------------------
#     def wait_for_element(self, locator):
#         return self.wait.until(
#             EC.visibility_of_element_located(locator)   # ✅ FIXED
#         )

#     # ----------------------------
#     # Scroll to Element
#     # ----------------------------
#     def scroll_to_element(self, locator):
#         element = self.wait.until(
#             EC.visibility_of_element_located(locator)   # ✅ FIXED
#         )
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block: 'center'});", element
#         )
#         return element

#     # ----------------------------
#     # Refresh Page
#     # ----------------------------
#     def refresh_page(self):
#         self.driver.refresh()

#     # ----------------------------
#     # JS Click (Direct)
#     # ----------------------------
#     def js_click(self, locator):
#         element = self.wait.until(
#             EC.presence_of_element_located(locator)
#         )
#         self.driver.execute_script("arguments[0].click();", element)