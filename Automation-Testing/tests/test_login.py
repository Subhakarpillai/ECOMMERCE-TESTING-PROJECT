from pages.login_page import LoginPage


def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("wrong_user")
    login.enter_password("wrong_password")
    login.click_login()

    error = login.get_error_message()

    assert "Username and password do not match" in error


def test_empty_username(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_password("secret_sauce")
    login.click_login()

    error = login.get_error_message()

    assert "Username is required" in error


def test_empty_password(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.click_login()

    error = login.get_error_message()

    assert "Password is required" in error
