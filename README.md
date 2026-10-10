# 学生成绩管理系统 Web 自动化测试

基于 Selenium + Pytest 对「学生成绩管理系统」进行 Web 自动化测试，覆盖登录、学生管理、成绩管理等核心功能。

## 项目背景

「学生成绩管理系统」（https://github.com/bearybeary-beary/student-grade-system）是一个 Flask Web 应用。本项目对其核心功能编写自动化测试用例，验证功能正确性。

## 技术栈

- 测试框架：Pytest
- 自动化工具：Selenium WebDriver（Edge）
- 测试报告：pytest-html
- 编程语言：Python 3.10

## 测试用例

| 模块 | 用例 | 验证点 |
| :--- | :--- | :--- |
| 登录 | test_login_success | 正确账号密码能登录成功 |
| 登录 | test_login_wrong_password | 错误密码提示错误信息 |
| 登录 | test_login_empty_username | 空用户名触发 HTML5 校验 |
| 学生管理 | test_add_student | 能添加新学生 |
| 学生管理 | test_add_duplicate_student | 重复学号提示“学号已存在” |
| 学生管理 | test_delete_student | 能删除学生并处理 confirm 弹窗 |
| 成绩管理 | test_add_grade | 能录入成绩并提示成功 |
| 成绩管理 | test_stats_page | 统计页正常展示 |

共 8 条用例。

## 项目结构

student_grade_test/
├── conftest.py # fixture 配置（driver、登录态）
├── test_login.py # 登录模块测试
├── test_student.py # 学生管理模块测试
├── test_grade.py # 成绩管理模块测试
├── requirements.txt
├── report.html # 测试报告
└── README.md

## 如何运行

1. 确保「学生成绩管理系统」已在本机 http://127.0.0.1:5000 运行
2. 安装依赖
   pip install -r requirements.txt
3. 运行测试
   pytest -v
4. 生成测试报告
   pytest -v --html=report.html --self-contained-html

## 测试结果

8 passed

## 作者

胡晓芳 - 宁夏大学 计算机科学与技术 硕士