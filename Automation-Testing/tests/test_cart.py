from pages.login_page import LoginPage
from pages.cart_page import CartPage
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


# TC9 - Add a Single Product to Cart
def test_add_single_product_to_cart(driver):

    login_to_application(driver)

    cart = CartPage(driver)
    cart.add_backpack()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "1"
        )
    )

    assert cart.get_cart_count() == "1"


# TC10 - Add Multiple Products to Cart
def test_add_multiple_products_to_cart(driver):

    login_to_application(driver)

    cart = CartPage(driver)
    cart.add_backpack()
    cart.add_bike_light()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "2"
        )
    )

    assert cart.get_cart_count() == "2"


# TC11 - Remove Product from Cart
def test_remove_product_from_cart(driver):

    login_to_application(driver)

    cart = CartPage(driver)
    cart.add_backpack()
    cart.open_cart()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    cart.remove_backpack_from_cart()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    assert len(cart.get_cart_items()) == 0


# TC12 - Verify Cart Contents
def test_verify_cart_contents(driver):

    login_to_application(driver)

    cart = CartPage(driver)
    cart.add_backpack()
    cart.add_bike_light()
    cart.open_cart()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    product_names = cart.get_product_names()

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names