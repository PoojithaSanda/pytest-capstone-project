# def test_delete_existing_note_ui(driver):
#     from pages.login_page import LoginPage
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#     import time

#     driver.get("https://practice.expandtesting.com/notes/app")

#     login = LoginPage(driver)
#     wait = WebDriverWait(driver, 15)

#     # ---------------- LOGIN ----------------
#     login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

#     # ---------------- SCROLL AFTER LOGIN ----------------
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

#     # ---------------- GET ALL NOTES ----------------
#     notes = wait.until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, "//div[contains(@class,'note') or contains(@class,'card')]")
#         )
#     )

#     initial_count = len(notes)

#     if initial_count == 0:
#         import pytest
#         pytest.skip("No notes available to delete")

#     # ---------------- FIND FIRST DELETE BUTTON ----------------
#     delete_btn = wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[4]/div[2]/div/div[4]/div/button[2]")
#         )
#     )

#     # ---------------- SCROLL TO DELETE BUTTON ----------------
#     driver.execute_script("arguments[0].scrollIntoView(true);", delete_btn)
#     time.sleep(1)

#     # ---------------- CLICK DELETE ----------------
#     wait.until(EC.element_to_be_clickable(delete_btn)).click()

#     # ---------------- WAIT FOR COUNT TO REDUCE ----------------
#     wait.until(
#         lambda d: len(d.find_elements(By.XPATH, "//div[contains(@class,'note') or contains(@class,'card')]")) < initial_count
#     )

#     updated_notes = driver.find_elements(
#         By.XPATH, "//div[contains(@class,'note') or contains(@class,'card')]"
#     )

#     # ---------------- ASSERT ----------------
#     assert len(updated_notes) == initial_count - 1
