from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TC9 - Add a Single Product to Cart

def test_add_single_product_to_cart(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert cart_badge.text == "1"



    # TC10 - Add Multiple Products to Cart

def test_add_multiple_products_to_cart(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "2"
        )
    )

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert cart_badge.text == "2"


    # TC11 - Remove Product from Cart

def test_remove_product_from_cart(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0


    # TC12 - Verify Cart Contents

def test_verify_cart_contents(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    product_names = [item.text for item in cart_items]

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names