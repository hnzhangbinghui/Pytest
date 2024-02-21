import pytest
from time import sleep
@pytest.fixture()
def jiaju1():
    from selenium import webdriver
    # 前置条件，打开浏览器
    print("打开浏览器")
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver2 = webdriver.Firefox()
    driver2.maximize_window()
    driver2.implicitly_wait(10)
    yield driver,driver2  # yield，返回函数值，可以继续执行下面的代码；
    # 后置条件；
    print("关闭浏览器")
    driver.quit()
    driver2.quit()

@pytest.fixture()
def jiaju2():
    # 前置条件，链接数据库
    print("链接数据库成功")
    name = "python_ceshijiaju"
    age="222"
    yield name,age
    # 后置处理
    print("\n断开数据库成功")
@pytest.fixture()
def jiaju3(jiaju2):
    a,b=jiaju2
    yield a,b





