def test_ui_to_api(driver):
    from pages.login_page import LoginPage
    from api.api_client import APIClient
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    title = "Hybrid Test"
    desc = "UI to API"

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)
    wait = WebDriverWait(driver, 15)

    # -----------------------
    # STEP 1: LOGIN
    # -----------------------
    login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    # -----------------------
    # STEP 2: OPEN ADD NOTE
    # -----------------------
    add_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
    )
    add_btn.click()

    # -----------------------
    # STEP 3: ENTER TITLE
    # -----------------------
    title_input = wait.until(
        EC.element_to_be_clickable((By.ID, "title"))
    )
    title_input.clear()
    title_input.send_keys(title)

    # -----------------------
    # STEP 4: ENTER DESCRIPTION
    # -----------------------
    desc_input = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    desc_input.clear()
    desc_input.send_keys(desc)

    # -----------------------
    # STEP 5: SAVE NOTE
    # -----------------------
    save_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[3]/div/div/form/div[2]/button[1]")))
        
    
    driver.execute_script("arguments[0].click();", save_btn)

    # -----------------------
    # STEP 6: VERIFY UI
    # -----------------------
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(),'{title}')]")
        )
    )

    # -----------------------
    # STEP 7: API VALIDATION
    # -----------------------
    api = APIClient("https://practice.expandtesting.com/notes/api")
    api.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    res = api.get_notes()

    # IMPORTANT: safe parsing
    assert res.status_code == 200

    notes_list = res.json().get("data", [])

    # -----------------------
    # STEP 8: STRONG VALIDATION
    # -----------------------
    matching_notes = [
        note for note in notes_list
        if note.get("title") == title and note.get("description") == desc
    ]

    assert len(matching_notes) > 0, "Created note not found in API response"


#working code 
#  def test_ui_to_api(driver):
#     from pages.login_page import LoginPage
#     from api.api_client import APIClient
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC

#     title = "Hybrid Test"
#     desc = "UI to API"

#     driver.get("https://practice.expandtesting.com/notes/app")

#     login = LoginPage(driver)
#     wait = WebDriverWait(driver, 15)

#     # -----------------------
#     # STEP 1: LOGIN
#     # -----------------------
#     login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

#     # Wait for dashboard Add button
#     add_btn = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add')]"))
#     )

#     # IMPORTANT: use normal click (not JS click)
#     add_btn.click()

#     # -----------------------
#     # STEP 2: WAIT FOR MODAL
#     # -----------------------
#     title_input = wait.until(
#         EC.element_to_be_clickable((By.ID, "title"))
#     )

#     # -----------------------
#     # STEP 3: ENTER TITLE (REAL USER INPUT)
#     # -----------------------
#     title_input.clear()
#     title_input.send_keys(title)

#     # -----------------------
#     # STEP 4: ENTER DESCRIPTION
#     # -----------------------
#     desc_input = wait.until(
#         EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
#     )
#     desc_input.clear()
#     desc_input.send_keys(desc)

#     # -----------------------
#     # STEP 5: CLICK SAVE
#     # -----------------------
#     save_btn = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[3]/div/div/form/div[2]/button[1]")))
#     save_btn.click()

#     # -----------------------
#     # STEP 6: VERIFY UI UPDATE
#     # -----------------------
#     wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, f"//*[contains(text(),'{title}')]")
#         )
#     )

#     # -----------------------
#     # STEP 7: API VALIDATION
#     # -----------------------
#     api = APIClient("https://practice.expandtesting.com/notes/api")
#     api.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

#     res = api.get_notes()
#     notes_list = res.json()["data"]

#     assert any(note["title"] == title for note in notes_list)
