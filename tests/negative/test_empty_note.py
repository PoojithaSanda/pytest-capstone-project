def test_empty_note_submission(driver):
    from pages.login_page import LoginPage
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)
    wait = WebDriverWait(driver, 10)

    # ---------------- LOGIN ----------------
    login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    # ---------------- OPEN ADD NOTE ----------------
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
    ).click()

    # ---------------- CLICK SAVE WITHOUT ENTERING DATA ----------------
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[3]/div/div/form/div[2]/button[1]"))
    ).click()

    # ---------------- VALIDATION: TITLE REQUIRED ----------------
    title_error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Title is required')]")
        )
    )

    # ---------------- VALIDATION: DESCRIPTION REQUIRED ----------------
    desc_error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Description is required')]")
        )
    )

    # ---------------- ASSERTIONS ----------------
    assert title_error.is_displayed()
    assert desc_error.is_displayed()