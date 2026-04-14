# tests/test_saucedemo.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 测试1：标准用户登录成功
def test_standard_user_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 等待登录成功后 URL 包含 inventory.html
    WebDriverWait(driver, 5).until(EC.url_contains("inventory.html"))
    # 验证页面标题是 "Products"
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

# 测试2：锁定用户登录失败（异常测试）
def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error_msg = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "locked out" in error_msg.text

# 测试3：错误密码登录失败
def test_wrong_password(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error_msg = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Username and password do not match" in error_msg.text

# 测试4：添加商品到购物车（依赖登录成功）
def test_add_to_cart(driver):
    # 先登录
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 5).until(EC.url_contains("inventory.html"))

    # 点击第一个商品的 Add to cart 按钮
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # 点击购物车图标
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # 验证商品在购物车中
    cart_item = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    item_name = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_name == "Sauce Labs Backpack"