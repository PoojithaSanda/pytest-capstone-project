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


def test_empty_note_submission(driver):

    from pages.login_page import LoginPage

    wait = WebDriverWait(driver, 20)

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)

    #  LOGIN 
    login.login(
        "sandapoojitha7396@gmail.com",
        "Poojitha@2k4"
    )

    remove_ads(driver)

    # CLICK ADD NOTE 
    add_note_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(text(),'Add Note')]"
            )
        )
    )

    scroll_to_element(driver, add_note_btn)

    driver.execute_script(
        "arguments[0].click();",
        add_note_btn
    )

    remove_ads(driver)

    #  WAIT FOR ADD NOTE MODAL 
    wait.until(
        EC.visibility_of_element_located(
            (
                By.CLASS_NAME,
                "modal-content"
            )
        )
    )

    # CLICK CREATE BUTTON WITHOUT ENTERING DATA 
    create_btn = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(text(),'Create')]"
            )
        )
    )

    scroll_to_element(driver, create_btn)

    driver.execute_script(
        "arguments[0].click();",
        create_btn
    )

    # -VALIDATION: TITLE REQUIRED 
    title_error = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(),'Title is required')]"
            )
        )
    )

    # VALIDATION: DESCRIPTION REQUIRED 
    desc_error = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(),'Description is required')]"
            )
        )
    )

    # ASSERTIONS 
    assert title_error.is_displayed()
    assert desc_error.is_displayed()

    print("Validation messages displayed successfully")