# conding:utf-8
# @author : zhangbinghui
# @description : fixture

"""
fixture 相对setup和teardown的优势：
1、命名方式灵活，不局限于setup和teardown这几个命名；
2、conftest.py 配置可以事项数据共享，不需要import就能自动找到一些配置；
3、scope=“module”,可以实现多个.py跨文件共享前置；
4、scope=“scope”，可以实现多个.PY跨文件使用一个session来完成多个用例
"""

"""
fixture(scope="function",params=None,autouse=False,ids=None,name=None)
       --scope，四个级别参数，function默认，class，module，session；
       scope参数为session：所有测试.py文件执行前执行一次
       scope参数为module：每一个测试.py文件执行前都会执行一次conftest文件中的fixture
       scope参数为class：每一个测试文件中的测试类执行前都会执行一次conftest文件中的
       scope参数为function：所有文件的测试用例执行前都会执行一次conftest文件中的fixture

       --params， 一个可选的参数列表，它将导致多个参数调用fixture 功能呾所有测试使用它
       --autouse，如果为 True，则为所有测试激活 fixture func 可以看到它。 如果为 False（默讣值）则显式需要参考来激活 fixture
       --ids，每个字符串 id 的列表，每个字符串对应于 params 返样他们就是测试 ID 的一部分。 如果没有提供 ID 它们将从 params 自动生成
       --name，fixture 的名称。 返默讣为装饰函数的名称。 如果fixture 在定义它的同一模块中使用，夹具的功能名称将被请求夹具的功能 arg 遮蔽;
        解决返个问题的一种方法是将装饰函数命名
1、使用装饰器标记fixture的功能；
2、可以使用此装饰器（带参或不带参数）来定义 fixture 功能。 fixture功能的名称可以在以后使用
3、引用它会在运行测试之前调用它：test 模块戒类可以使用pytest.mark.usefixtures（fixturename 标记
4、测试功能可以直接使用 fixture 名称作为输入参数，在返种情况下，夹具实例从 fixture 迒回功能将被注入
5、
fixture_ <fixturename>”然后使用”@ pytest.fixture（name
='<fixturename>'）“”。
Fixtures 可以选择使用 yield 语句为测试函数提供它们的值，而丌
是 return。 在这种情况下，yield 语句之后的代码块作为拆卸代码执
行，而丌管测试结果如何。fixture 功能必须只产生一次
6、pytest里面默认读取conftest.py的配置，注意，conftest.py配置脚本的名称是固定的，不能更改；
7、conftest.py 不运行的用例要在同一个 pakage 下，并且有__init__.py 文件
8、不需要 import 导入 conftest.py，pytest 用例会自动查找；
三、autouse 设置为 True，自动调用 fixture 功能,可以设置多个scope，比如一个是module，一个function
 start 设置 scope 为 module 级别，在当前.py 用例模块叧执行一
次，autouse=True 自动使用
 open_home 设置 scope 为 function 级别，每个用例前都调用
一次，自动使用

"""

import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from anaconda.Pytest.test_conftest.func import get_yaml


@pytest.fixture(scope="module", autouse=True)
def login():
    print('\n全局conftest.py执行，准备登录----')
    login_url = get_yaml("login_url")
    account = get_yaml("account")
    passwd = get_yaml("passwd")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url=login_url)
    sleep(3)
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
    driver.implicitly_wait(10)
    assert "托管综合业务平台" in driver.page_source
    print("登录成功... ...")
    return driver

    # yield
    # sleep(2)
    # driver.quit()


#
# @pytest.fixture(scope='session', autouse=True)
# def login2():
#     print('全局conftest.py执行，第二个方法开始执行----')
#
