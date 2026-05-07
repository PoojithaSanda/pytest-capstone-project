
# import pytest
# import os
# import logging
# from datetime import datetime

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# # =========================================
# # CREATE REPORT FOLDERS
# # =========================================
# def pytest_configure(config):

#     os.makedirs("reports", exist_ok=True)

#     os.makedirs("reports/screenshots", exist_ok=True)


# # =========================================
# # LOGGING CONFIGURATION
# # =========================================
# logging.basicConfig(
#     filename="reports/test.log",
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s"
# )


# # =========================================
# # SELENIUM DRIVER FIXTURE
# # =========================================
# @pytest.fixture(scope="function")
# def driver():

#     chrome_options = webdriver.ChromeOptions()

#     # Disable notifications
#     chrome_options.add_argument("--disable-notifications")

#     # Disable popup blocking
#     chrome_options.add_argument("--disable-popup-blocking")

#     # Disable ads
#     chrome_options.add_argument("--disable-features=VizDisplayCompositor")

#     # Disable automation banners
#     chrome_options.add_experimental_option(
#         "excludeSwitches",
#         ["enable-automation"]
#     )

#     chrome_options.add_experimental_option(
#         'useAutomationExtension',
#         False
#     )

#     # BLOCK ADS / POPUPS
#     prefs = {
#         "profile.default_content_setting_values.notifications": 2,
#         "profile.default_content_setting_values.popups": 0,
#         "profile.managed_default_content_settings.images": 1
#     }

#     chrome_options.add_experimental_option("prefs", prefs)

#     driver = webdriver.Chrome(options=chrome_options)

#     driver.maximize_window()

#     logging.info("Browser launched")

#     yield driver

#     logging.info("Browser closed")

#     driver.quit()


# # =========================================
# # SCREENSHOT ON FAILURE
# # =========================================
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     outcome = yield

#     report = outcome.get_result()

#     # Only if test failed
#     if report.when == "call" and report.failed:

#         print(f"\nDEBUG: Failed test -> {item.name}")

#         logging.error(f"Test Failed -> {item.name}")

#         driver = item.funcargs.get("driver", None)

#         if driver:

#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

#             file_name = f"{item.name}_{timestamp}.png"

#             file_path = os.path.join(
#                 "reports",
#                 "screenshots",
#                 file_name
#             )

#             try:

#                 driver.save_screenshot(file_path)

#                 logging.info(
#                     f"Screenshot saved -> {file_path}"
#                 )

#                 print(
#                     f"\n📸 Screenshot saved -> {file_path}"
#                 )

#             except Exception as e:

#                 logging.error(
#                     f"Screenshot failed -> {e}"
#                 )

#                 print(
#                     f"\n⚠️ Screenshot failed -> {e}"
#                 )

import pytest
import os
import logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# =========================================
# CREATE REPORT FOLDERS (SAFE FOR PARALLEL)
# =========================================
def pytest_configure(config):

    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


# =========================================
# PARALLEL WORKER SAFE LOGGING
# =========================================
def get_worker_id():

    # pytest-xdist adds worker info like gw0, gw1
    worker = os.environ.get("PYTEST_XDIST_WORKER", "master")
    return worker


logging.basicConfig(
    filename=f"reports/test_{get_worker_id()}.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# =========================================
# SELENIUM DRIVER FIXTURE (PARALLEL READY)
# =========================================
@pytest.fixture(scope="function")
def driver():

    chrome_options = webdriver.ChromeOptions()

    # Disable notifications
    chrome_options.add_argument("--disable-notifications")

    # Disable popup blocking
    chrome_options.add_argument("--disable-popup-blocking")

    # Automation stealth options
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
    # GRID SUPPORT (OPTIONAL SWITCH)
    # =========================================

    use_grid = False  # change to True if using Selenium Grid

    if use_grid:

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )

    else:

        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    logging.info("Browser launched")

    yield driver

    logging.info("Browser closed")

    driver.quit()


# =========================================
# SCREENSHOT ON FAILURE (PARALLEL SAFE)
# =========================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        logging.error(f"Test Failed -> {item.name}")

        driver = item.funcargs.get("driver", None)

        if driver:

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