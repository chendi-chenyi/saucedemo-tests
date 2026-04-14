# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture
def driver():
    """每个测试函数执行前，都会调用这个 fixture，返回一个 WebDriver 实例"""
    service = Service(executable_path=r'.\msedgedriver.exe')
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver          # 测试函数在此处执行
    driver.quit()         # 测试结束后自动关闭浏览器