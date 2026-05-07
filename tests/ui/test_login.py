def test_login_success(driver):
    from pages.login_page import LoginPage

    driver.get("https://practice.expandtesting.com/notes/app")

    login = LoginPage(driver)

    # Use your real credentials
    login.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    # Validation: check if redirected to dashboard (URL change)
    assert "notes" in driver.current_url