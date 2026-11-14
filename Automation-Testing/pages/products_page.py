from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.CLASS_NAME, "inventory_item")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    product_prices = (By.CLASS_NAME, "inventory_item_price")
    backpack_link = (By.ID, "item_4_title_link")
    product_name = (By.CLASS_NAME, "inventory_details_name")

    def get_product_count(self):
        return len(self.driver.find_elements(*self.products))

    def sort_products(self, option):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text(option)

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.product_prices)
        return [float(price.text.replace("$", "")) for price in prices]

    def open_backpack(self):
        self.driver.find_element(*self.backpack_link).click()

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text