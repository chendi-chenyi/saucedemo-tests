# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_first_item_name(self):
        """获取购物车中第一个商品的名字"""
        item = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.CART_ITEM)
        )
        return item.find_element(*self.ITEM_NAME).text