def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element("xpath", "//input[@id='user-name']").send_keys("wrong_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("wrong_password")
    driver.find_element("xpath", "//input[@id='login-button']").click()

    error = driver.find_element("xpath", "//h3[@data-test='error']")

    assert "Username and password do not match" in error.text


def test_empty_username(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@id='login-button']").click()

    error = driver.find_element("xpath", "//h3[@data-test='error']")

    assert "Username is required" in error.text


def test_empty_password(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='login-button']").click()

    error = driver.find_element("xpath", "//h3[@data-test='error']")

    assert "Password is required" in error.text