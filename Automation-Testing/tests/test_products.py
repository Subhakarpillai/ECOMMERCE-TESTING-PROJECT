from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# TC5 - Verify Products Displayed
def test_products_displayed(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) == 6


# TC6 - Sort Products by Price (Low to High)
def test_sort_price_low_to_high(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    sort_dropdown = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    sort_dropdown.select_by_visible_text("Price (low to high)")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    price_values = [float(price.text.replace("$", "")) for price in prices]

    assert price_values == sorted(price_values)


# TC7 - Sort Products by Price (High to Low)
def test_sort_price_high_to_low(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    sort_dropdown = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    sort_dropdown.select_by_visible_text("Price (high to low)")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    price_values = [float(price.text.replace("$", "")) for price in prices]

    assert price_values == sorted(price_values, reverse=True)


# TC8 - Verify Product Details

def test_view_product_details(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name"))
    )

    product_name = driver.find_element(
        By.CLASS_NAME, "inventory_details_name"
    ).text

    assert product_name == "Sauce Labs Backpack"