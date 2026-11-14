from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    complete_message = (By.CLASS_NAME, "complete-header")
    error_message = (By.XPATH, "//h3[@data-test='error']")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.last_name).send_keys(name)

    def enter_postal_code(self, code):
        self.driver.find_element(*self.postal_code).send_keys(code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_complete_message(self):
        return self.driver.find_element(*self.complete_message).text

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text