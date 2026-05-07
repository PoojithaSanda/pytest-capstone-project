# import pytest
# import os
# import logging
# import time
# from datetime import datetime
# from selenium import webdriver


# # =========================================
# # CREATE REQUIRED FOLDERS
# # =========================================
# def pytest_configure(config):
#     os.makedirs("reports", exist_ok=True)
#     os.makedirs("reports/screenshots", exist_ok=True)
#     os.makedirs("logs", exist_ok=True)


# # =========================================
# # GET WORKER ID (PARALLEL SUPPORT)
# # =========================================
# def get_worker_id():
#     return os.environ.get("PYTEST_XDIST_WORKER", "master")


# worker_id = get_worker_id()


# # =========================================
# # LOGGER
# # =========================================
# logging.basicConfig(
#     filename=f"logs/test_{worker_id}.log",
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s"
# )


# # =========================================
# # REMOVE ADS HELPER (GLOBAL USE)
# # =========================================
# def remove_ads(driver):
#     try:
#         driver.execute_script("""
#             document.querySelectorAll('iframe').forEach(el => el.remove());
#         """)
#     except Exception as e:
#         logging.warning(f"Ad removal failed: {e}")


# # =========================================
# # SAFE CLICK HELPER
# # =========================================
# def safe_click(driver, element):
#     import selenium.common.exceptions as ex

#     try:
#         driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         time.sleep(0.5)
#         element.click()

#     except ex.ElementClickInterceptedException:
#         driver.execute_script("arguments[0].click();", element)


# # =========================================
# # DRIVER FIXTURE
# # =========================================
# @pytest.fixture(scope="function")
# def driver():

#     chrome_options = webdriver.ChromeOptions()

#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-popup-blocking")
#     chrome_options.add_argument("--start-maximized")

#     chrome_options.add_experimental_option(
#         "excludeSwitches", ["enable-automation"]
#     )
#     chrome_options.add_experimental_option(
#         "useAutomationExtension", False
#     )

#     prefs = {
#         "profile.default_content_setting_values.notifications": 2,
#         "profile.default_content_setting_values.popups": 0,
#         "profile.default_content_setting_values.automatic_downloads": 1
#     }

#     chrome_options.add_experimental_option("prefs", prefs)

#     USE_GRID = False

#     if USE_GRID:
#         driver = webdriver.Remote(
#             command_executor="http://localhost:4444/wd/hub",
#             options=chrome_options
#         )
#         logging.info("Running on Selenium Grid")
#     else:
#         driver = webdriver.Chrome(options=chrome_options)
#         logging.info("Running on Local ChromeDriver")

#     driver.implicitly_wait(3)

#     logging.info("Browser launched")

#     yield driver

#     logging.info("Browser closed")
#     driver.quit()


# # =========================================
# # AUTO CLEAN ADS BEFORE EVERY TEST
# # =========================================
# @pytest.fixture(autouse=True)
# def clean_ads_every_test(driver):
#     remove_ads(driver)
#     yield


# # =========================================
# # SCREENSHOT ON FAILURE
# # =========================================
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:

#         logging.error(f"Test Failed -> {item.name}")

#         driver = item.funcargs.get("driver", None)

#         if driver:

#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             worker = get_worker_id()

#             file_name = f"{item.name}_{worker}_{timestamp}.png"

#             file_path = os.path.join(
#                 "reports",
#                 "screenshots",
#                 file_name
#             )

#             try:
#                 driver.save_screenshot(file_path)
#                 logging.info(f"Screenshot saved -> {file_path}")
#                 print(f"\n📸 Screenshot saved -> {file_path}")

#             except Exception as e:
#                 logging.error(f"Screenshot failed -> {e}")
#                 print(f"\n⚠️ Screenshot failed -> {e}")






import pytest
import os
import logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# =========================================
# CREATE REQUIRED FOLDERS (PARALLEL SAFE)
# =========================================
def pytest_configure(config):

    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


# =========================================
# GET PYTEST WORKER ID (PARALLEL SUPPORT)
# =========================================
def get_worker_id():

    return os.environ.get("PYTEST_XDIST_WORKER", "master")


# =========================================
# LOGGER
# =========================================
worker_id = get_worker_id()

logging.basicConfig(
    filename=f"logs/test_{worker_id}.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# =========================================
# REMOVE ADS / POPUPS
# =========================================
def remove_ads(driver):

    try:
        driver.execute_script("""
            document.querySelectorAll('iframe').forEach(el => el.remove());
        """)
        logging.info("Ads iframe removed")

    except Exception as e:
        logging.warning(f"Ad removal failed -> {e}")


# =========================================
# CLOSE POPUPS IF PRESENT
# =========================================
def close_popups(driver):

    possible_close_buttons = [
        "//button[contains(text(),'Close')]",
        "//button[contains(text(),'close')]",
        "//button[contains(text(),'✕')]",
        "//button[contains(text(),'×')]",
        "//button[contains(@class,'close')]",
        "//div[contains(@class,'close')]"
    ]

    for locator in possible_close_buttons:

        try:
            elements = driver.find_elements(By.XPATH, locator)

            for element in elements:

                if element.is_displayed():

                    driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                    logging.info("Popup closed")

        except Exception:
            pass


# =========================================
# SCROLL TO ELEMENT
# =========================================
def scroll_to_element(driver, element):

    try:

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        ActionChains(driver).move_to_element(element).perform()

        logging.info("Scrolled to element")

    except Exception as e:

        logging.warning(f"Scrolling failed -> {e}")


# =========================================
# SELENIUM DRIVER FIXTURE
# =========================================
@pytest.fixture(scope="function")
def driver():

    chrome_options = webdriver.ChromeOptions()

    # -------------------------
    # BASIC STABILITY OPTIONS
    # -------------------------
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")

    # BLOCK ADS
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    chrome_options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 0,
        "profile.managed_default_content_settings.images": 1
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # =========================================
    # GRID SWITCH
    # =========================================
    USE_GRID = False

    if USE_GRID:

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )

        logging.info("Running on Selenium Grid")

    else:

        driver = webdriver.Chrome(options=chrome_options)

        logging.info("Running on Local ChromeDriver")

    driver.maximize_window()

    logging.info("Browser launched")

    # REMOVE ADS IMMEDIATELY
    remove_ads(driver)

    yield driver

    logging.info("Browser closed")

    driver.quit()


# =========================================
# SCREENSHOT ON FAILURE
# =========================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        logging.error(f"Test Failed -> {item.name}")

        driver = item.funcargs.get("driver", None)

        if driver:

            try:
                remove_ads(driver)
                close_popups(driver)

            except Exception:
                pass

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            worker = get_worker_id()

            file_name = f"{item.name}_{worker}_{timestamp}.png"

            file_path = os.path.join(
                "reports",
                "screenshots",
                file_name
            )

            try:

                driver.save_screenshot(file_path)

                logging.info(f"Screenshot saved -> {file_path}")

                print(f"\n📸 Screenshot saved -> {file_path}")

            except Exception as e:

                logging.error(f"Screenshot failed -> {e}")

                print(f"\n⚠️ Screenshot failed -> {e}")