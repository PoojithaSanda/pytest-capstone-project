def test_invalid_login(driver):
    from pages.login_page import LoginPage
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)
    wait = WebDriverWait(driver, 10)

    # ---------------- INVALID LOGIN ----------------
    login.login("wronguser@test.com", "wrongpass")

    # ---------------- VERIFY ERROR MESSAGE ----------------
    error_msg = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Incorrect') or contains(text(),'Invalid')]")
        )
    )

    assert error_msg.is_displayed()