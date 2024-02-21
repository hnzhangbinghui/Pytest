from selenium import webdriver
from time import sleep
import pytest
from py._xmlgen import html
url="http://219.141.235.67:28088/login"


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('111111111111111111111111'))
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))

def test_shuzi():
    driver=webdriver.Firefox()
    driver.get(url=url)
    sleep(3)
    driver.maximize_window()
    sleep(1)
    account=driver.find_element_by_xpath("//input[@placeholder='登录账号']")
    account.click()
    account.clear()
    account.send_keys("zhangbinghui")
    sleep(2)
    passwd=driver.find_element_by_xpath("//input[@placeholder='密码']")
    passwd.click()
    passwd.clear()
    passwd.send_keys("11111111111")
    sleep(2)
    driver.find_element_by_xpath("//button[@class='el-button login-button el-button--default el-button--small']").click()
    assert '张冰辉' in driver.page_source






