# pages/inventory_page.py
from selenium.webdriver.common.by import By

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def get_title_text(self):
        return self.driver.find_element(*self.TITLE).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def go_to_cart(self):
        self.driver.find_element(*self.SHOPPING_CART).click()