# -*-coding:utf-8 -*-
# coding:utf-8
"""
# @time : 20230330
# @author: Zhangbinghui
# @description:关于module前置和后置条件的设置de实际操作
"""
# 函数式
"""
模块
setup_module 是所有用例开始前叧执行一次，
teardown_module 是所有用例结束后叧执行一次

从结果看出，运行的优先级：setup_class》setup_method》
setup 》用例》teardown》teardown_method》teardown_class
"""

import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

lgoin_url = "http://192.168.99.158:9080/acp-custody/login.html"
account = "ab"
passwd = "Ysstech123!@#"
driver = webdriver.Chrome()


def setup_module():
    print("setup_module,整个 .py 模块只执行一次，比如所有用例开始前打开一次浏览器")
    print("开始执行模块... ..")
    driver.get(url=lgoin_url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    zhanghao = driver.find_element(By.XPATH, "//input[@id='pwdUserName']")
    zhanghao.click()
    sleep(1)
    zhanghao.clear()
    sleep(1)
    zhanghao.send_keys(account)
    sleep(1)
    mima = driver.find_element(By.XPATH, "//input[@id='pwdPassword']")
    mima.click()
    sleep(1)
    mima.clear()
    sleep(1)
    mima.send_keys(passwd)
    sleep(2)
    # 点击登录按钮
    driver.find_element(By.XPATH, "//button[@id='login-btn']").click()
    sleep(3)
    assert "托管综合业务平台" in driver.page_source
    print("登录成功... ...")


def teardown_module():
    sleep(3)
    print("关闭浏览器")
    driver.quit()
    # print("teardown_module，整个 .py 模块只执行一次，比如所有用例结束后关闭浏览器")
    # print("结束整个模块的执行，测试结束。")


# def setup_function():
#     print("\nsetup_function,每个用例开始前都会执行")
#     print("开始执行测试用例... ...")
#
#
# def teardown_function():
#     print("\nteardown_function,每个用例结束后都会执行")
#     print("用例测试结束了，拜拜。")


def test1():
    print('\n开始第一个用例测试... ...')
    # 打开流程管理
    driver.find_element(By.XPATH, "//span[contains(text(),'流程管理')]").click()
    sleep(2)
    assert "ICR配置" in driver.page_source


def test2():
    print('\n开始第二个用例测试... ...')
    driver.find_element(By.XPATH, "//span[contains(text(),'ICR配置')]").click()
    sleep(2)
    assert "产品映射" in driver.page_source

if __name__ == "__main__":
    pytest.main(["-s test_module_qianzhi_shicao.py"])
