from conftest import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_add_grade(logged_in_driver):
    driver = logged_in_driver
    driver.get(BASE_URL + '/grades')

    # 选第一个学生
    student_select = Select(driver.find_element(By.NAME, 'student_id'))
    assert len(student_select.options) > 1, '没有学生可选，请先在项目一里添加学生'
    student_select.select_by_index(1)

    # 选第一个课程
    course_select = Select(driver.find_element(By.NAME, 'course_id'))
    assert len(course_select.options) > 1, '没有课程可选，请先在项目一里添加课程'
    course_select.select_by_index(1)

    driver.find_element(By.NAME, 'score').send_keys('88')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-success'))
    )
    assert '成绩录入成功' in driver.page_source
    assert '88' in driver.page_source


def test_stats_page(logged_in_driver):
    driver = logged_in_driver
    driver.get(BASE_URL + '/stats')
    # 统计页应该有课程统计和全部成绩两个表格
    assert '成绩统计' in driver.page_source
    assert '课程统计' in driver.page_source