
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

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