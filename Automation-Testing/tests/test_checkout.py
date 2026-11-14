
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_and_add_product(driver):
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    cart = CartPage(driver)
    cart.add_backpack()

    # Wait until product is added
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "shopping_cart_badge"), "1"
        )
    )

    cart.open_cart()

    # Wait until cart page is loaded
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )


# TC13 - Checkout with Valid Customer Details

def test_checkout_valid_details(driver):
    wait = WebDriverWait(driver, 15)

    login_and_add_product(driver)

    checkout = CheckoutPage(driver)
    checkout.click_checkout()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    checkout.enter_first_name("Subhakar")
    checkout.enter_last_name("M")
    checkout.enter_postal_code("625001")

    checkout.click_continue()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_info")
        )
    )

    assert driver.find_element(
        By.CLASS_NAME, "summary_info"
    ).is_displayed()


# TC14 - Checkout with Empty Mandatory Fields

def test_checkout_empty_fields(driver):
    wait = WebDriverWait(driver, 15)

    login_and_add_product(driver)

    checkout = CheckoutPage(driver)
    checkout.click_checkout()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    checkout.click_continue()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message-container")
        )
    )

    error_message = checkout.get_error_message()

    assert "First Name is required" in error_message


# TC15 - Verify Successful Order

def test_successful_order(driver):
    wait = WebDriverWait(driver, 15)

    login_and_add_product(driver)

    checkout = CheckoutPage(driver)
    checkout.click_checkout()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    checkout.enter_first_name("Subhakar")
    checkout.enter_last_name("M")
    checkout.enter_postal_code("625001")

    checkout.click_continue()

    wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )

    checkout.click_finish()

    success_message = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert success_message.text == "Thank you for your order!"
