def test_create_note_ui(driver):
    from pages.login_page import LoginPage
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    def remove_ads(driver):
        driver.execute_script("""
            document.querySelectorAll('iframe').forEach(el => el.remove());
        """)
        
    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)
    wait = WebDriverWait(driver, 15)

    title = "UI Note"
    desc = "Created via UI"

    # ---------------- LOGIN ----------------
    login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    # ---------------- CLICK ADD ----------------
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
    ).click()

    # ---------------- ENTER TITLE ----------------
    title_input = wait.until(
        EC.element_to_be_clickable((By.ID, "title"))
    )
    title_input.clear()
    title_input.send_keys(title)

    # ---------------- ENTER DESCRIPTION ----------------
    desc_input = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    desc_input.clear()
    desc_input.send_keys(desc)

    # REMOVE ADS BEFORE CLICK
    remove_ads(driver)

    save_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    # SCROLL TO BUTTON
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        save_btn
    )

    # REMOVE ADS AGAIN
    remove_ads(driver)

    # JS CLICK
    driver.execute_script("arguments[0].click();", save_btn)
    # ---------------- VERIFY NOTE ----------------
    assert wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(),'{title}')]")
        )
    ).is_displayed()