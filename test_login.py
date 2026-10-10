from conftest import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    driver.get(BASE_URL)
    driver.find_element('name', 'username').send_keys('admin')
    driver.find_element('name', 'password').send_keys('123456')
    driver.find_element('css selector', 'button[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, '学生管理'))
    )
    assert '首页' in driver.page_source

def test_login_wrong_password(driver):
    driver.get(BASE_URL)
    driver.find_element('name', 'username').send_keys('admin')
    driver.find_element('name', 'password').send_keys('wrongpass')
    driver.find_element('css selector', 'button[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-danger'))
    )
    assert '用户名或密码错误' in driver.page_source

def test_login_empty_username(driver):
    driver.get(BASE_URL)
    driver.find_element('name', 'password').send_keys('123456')
    driver.find_element('css selector', 'button[type="submit"]').click()
    assert '登录' in driver.page_source