# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 元素定位（就像遥控器上的按钮位置）
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        """打开登录页"""
        self.driver.get(self.url)

    def enter_username(self, username):
        """输入用户名"""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """输入密码"""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """点击登录按钮"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """一步完成登录（组合上面三个动作）"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """获取错误提示文本"""
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.ERROR_MSG)
        ).text