from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    bike_light_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_link = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_items = (By.CLASS_NAME, "cart_item")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    product_names = (By.CLASS_NAME, "inventory_item_name")

    def add_backpack(self):
        self.driver.find_element(*self.backpack_button).click()

    def add_bike_light(self):
        self.driver.find_element(*self.bike_light_button).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def remove_backpack_from_cart(self):
        self.driver.find_element(*self.remove_backpack).click()

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def get_product_names(self):
        return [
            item.text for item in self.driver.find_elements(*self.product_names)
        ]