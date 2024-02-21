# coding:utf-8
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from anaconda.Pytest.test_conftest.func import get_yaml


def test_login_success(login):
    driver = login
    print("登录成功，当前用户是：%s" % (get_yaml("account")))
    if get_yaml("passwd"):
        return True
    else:
        return False


# param = get_yaml("account")  # [{'account': 'ab'}, {'passwd': 'Ysstech123!@#'}]
param=[{'zhanghao': 'ab', 'mima': 'Ysstech123!@#'}]
@pytest.fixture(scope="module")
def panduan(request):
    account = request.param["zhanghao"]
    print(account)
    if account:
        return True
    else:
        return False


# @pytest.fixture(scope="module")
# def panduan(login):
#     if login:
#         return True
#     else:
#         return False


@pytest.mark.parametrize("panduan", param, indirect=True)
class TestLiuCheng():
    def test_open_liuchengguanli(self,panduan,login):
        result=panduan
        if not result:
            pytest.xfail("登录失败，无法测试，标记为xfail")
            print("\n打开流程管理页面")
            driver = login
            assert "托管" in driver.page_source
            driver.find_element(By.XPATH, "//span[contains(text(),'流程管理')]").click()
            sleep(5)
            assert "ICR配置" in driver.page_source, "打开失败"


    def test_open_hesuan(self,panduan,login):
        result=panduan
        if result:
            print("\n打开核算页面")
            driver = login
            driver.find_element(By.XPATH, "//span[contains(text(),'核算管理')]").click()
            sleep(2)
            assert "报表中心" in driver.page_source


if __name__ == "__main__":
    pytest.main(["-s test_login.py"])
