import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'http://127.0.0.1:5000'

@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('--headless')
    d = webdriver.Edge(options=options)
    d.maximize_window()
    d.implicitly_wait(3)
    yield d
    d.quit()

@pytest.fixture()
def logged_in_driver(driver):
    """已登录的 driver，供需要登录的用例使用"""
    driver.get(BASE_URL)
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('123456')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # 关键：等导航栏出现"学生管理"，确认登录成功再返回
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, '学生管理'))
    )
    return driver