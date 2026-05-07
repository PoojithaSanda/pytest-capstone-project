from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def remove_ads(driver):
    driver.execute_script("""
        document.querySelectorAll('iframe').forEach(el => el.remove());
    """)


def scroll_to_element(driver, element):
    driver.execute_script("""
        arguments[0].scrollIntoView({
            behavior: 'smooth',
            block: 'center'
        });
    """, element)


def test_logout_functionality(driver):

    from pages.login_page import LoginPage

    wait = WebDriverWait(driver, 20)

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)

    # LOGIN
    login.login(
        "sandapoojitha7396@gmail.com",
        "Poojitha@2k4"
    )

    remove_ads(driver)

    # PROFILE BUTTON
    profile_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class,'btn')]"
            )
        )
    )

    scroll_to_element(driver, profile_btn)

    driver.execute_script(
        "arguments[0].click();",
        profile_btn
    )

    remove_ads(driver)

    # LOGOUT BUTTON
    logout_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[contains(text(),'Logout')]"
            )
        )
    )

    scroll_to_element(driver, logout_btn)

    driver.execute_script(
        "arguments[0].click();",
        logout_btn
    )

    # VERIFY LOGIN PAGE
    login_text = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(),'Login')]"
            )
        )
    )

    assert login_text.is_displayed()