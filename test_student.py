import time
from conftest import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_student(logged_in_driver):
    driver = logged_in_driver
    # 用时间戳保证学号唯一，避免重复运行冲突
    student_no = 'S' + str(int(time.time()))
    student_name = '测试学生'

    driver.get(BASE_URL + '/students')
    driver.find_element(By.LINK_TEXT, '添加学生').click()

    driver.find_element(By.NAME, 'student_no').send_keys(student_no)
    driver.find_element(By.NAME, 'name').send_keys(student_name)
    driver.find_element(By.NAME, 'class_name').send_keys('测试班级')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # 等待跳回列表页并出现该学生
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//td[text()="{student_no}"]'))
    )
    assert student_name in driver.page_source


def test_add_duplicate_student(logged_in_driver):
    driver = logged_in_driver
    student_no = 'D' + str(int(time.time()))

    # 第一次添加
    driver.get(BASE_URL + '/students/add')
    driver.find_element(By.NAME, 'student_no').send_keys(student_no)
    driver.find_element(By.NAME, 'name').send_keys('重复学生')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//td[text()="{student_no}"]'))
    )

    # 第二次添加同一学号
    driver.get(BASE_URL + '/students/add')
    driver.find_element(By.NAME, 'student_no').send_keys(student_no)
    driver.find_element(By.NAME, 'name').send_keys('重复学生2')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-danger'))
    )
    assert '学号已存在' in driver.page_source


def test_delete_student(logged_in_driver):
    driver = logged_in_driver
    student_no = 'X' + str(int(time.time()))

    # 先添加一个
    driver.get(BASE_URL + '/students/add')
    driver.find_element(By.NAME, 'student_no').send_keys(student_no)
    driver.find_element(By.NAME, 'name').send_keys('待删除学生')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    row_xpath = f'//tr[td[text()="{student_no}"]]'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, row_xpath))
    )

    # 点击该行的删除按钮
    row = driver.find_element(By.XPATH, row_xpath)
    row.find_element(By.LINK_TEXT, '删除').click()

    # 处理 confirm 弹窗
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    # 等待该行消失
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, row_xpath))
    )
    assert student_no not in driver.page_source