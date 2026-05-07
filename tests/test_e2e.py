def test_ui_to_api(driver):
    from pages.login_page import LoginPage
    from api.api_client import APIClient
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    def remove_ads(driver):
        driver.execute_script("""
            document.querySelectorAll('iframe').forEach(el => el.remove());
        """)
    title = "Hybrid Test"
    desc = "UI to API"

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)
    wait = WebDriverWait(driver, 15)

    
    # STEP 1: LOGIN
    
    login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    
    # STEP 2: OPEN ADD NOTE
    
    add_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
    )
    add_btn.click()

    
    # STEP 3: ENTER TITLE
    title_input = wait.until(
        EC.element_to_be_clickable((By.ID, "title"))
    )
    title_input.clear()
    title_input.send_keys(title)

    # STEP 4: ENTER DESCRIPTION
    desc_input = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    desc_input.clear()
    desc_input.send_keys(desc)

    # STEP 5: SAVE NOTE
    remove_ads(driver)

    submit_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        submit_btn
    )

    remove_ads(driver)

    driver.execute_script("arguments[0].click();", submit_btn)
    # STEP 6: VERIFY UI
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(),'{title}')]")
        )
    )

    # STEP 7: API VALIDATION
    api = APIClient("https://practice.expandtesting.com/notes/api")
    api.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    res = api.get_notes()

    # IMPORTANT: safe parsing
    assert res.status_code == 200

    notes_list = res.json().get("data", [])

    # STEP 8: STRONG VALIDATION
    matching_notes = [
        note for note in notes_list
        if note.get("title") == title and note.get("description") == desc
    ]

    assert len(matching_notes) > 0, "Created note not found in API response"
