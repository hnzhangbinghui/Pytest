import pytest
from time import sleep
import allure
@allure.story("多线程并发测试")
class TestCase1():
    @pytest.mark.parametrize('keyword',['a','b','c','d','e','f','g','h','i','j'])
    @allure.step("输出对应的字典的值！！！")
    def test_baidu_search(self,keyword):
        sleep(1)
        print(f'搜索关键字是：{keyword}')


class TestCase2():
    @pytest.mark.parametrize('user',['user1','user2','user3','user4','user5','user6','user7','user8','user9','user10'])
    def test_login(self,user):
        sleep(1)
        print(f'用户：{user},登录成功！！')









