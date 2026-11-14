from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_to_application(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )


# TC5 - Verify Products Displayed
def test_products_displayed(driver):

    login_to_application(driver)

    products = ProductsPage(driver)

    assert products.get_product_count() == 6


# TC6 - Sort Products by Price (Low to High)
def test_sort_price_low_to_high(driver):

    login_to_application(driver)

    products = ProductsPage(driver)
    products.sort_products("Price (low to high)")

    price_values = products.get_product_prices()

    assert price_values == sorted(price_values)


# TC7 - Sort Products by Price (High to Low)
def test_sort_price_high_to_low(driver):

    login_to_application(driver)

    products = ProductsPage(driver)
    products.sort_products("Price (high to low)")

    price_values = products.get_product_prices()

    assert price_values == sorted(price_values, reverse=True)


# TC8 - Verify Product Details
def test_view_product_details(driver):

    login_to_application(driver)

    products = ProductsPage(driver)
    products.open_backpack()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_details_name")
        )
    )

    assert products.get_product_name() == "Sauce Labs Backpack"
