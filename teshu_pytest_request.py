# coding:utf-8

"""
1、pytest的request是个数的fixture，用于访问测试用例的上下文信息，例如测试用例的名称，参数，标记等；
2、可以讲request作为参数传递给测试用例中的函数或者fixture，以便在测试用例中使用这些上下文信息；
3、具体讲，如果需要在测试用例中访问request，可以讲其作为参数传递给测试用例中的函数；

"""

# encoding:utf-8
import pytest


@pytest.fixture()
def login(request):
    print("\n=======================request start=================================")
    print('测试方法的参数化数据：{}'.format(request.param))
    print('测试方法所处模块的信息：{}'.format(request.module))
    print('测试方法信息：{}'.format(request.function))
    print('测试方法所在的类的信息：{}'.format(request.cls))
    print('测试方法所在路径信息：{}'.format(request.fspath))
    print('测试方法调用的多个fixture函数（比如fixture函数之间的嵌套调用（包括pytest内嵌的fixture函数））信息：{}'.format(request.fixturenames))
    print('测试方法调用的单个fixture函数（自己在程序中定义在测试方法中调用的fixture函数）信息：{}'.format(request.fixturename))
    print('测试方法级别信息：{}'.format(request.scope))
    print("\n=======================request end=================================")


import pytest

user = [('张三', '123456'), ('李四', 'abcdefg')]


class TestA:
    @pytest.mark.parametrize(argnames='login', argvalues=user, indirect=True)
    def test_one_param(self, login):
        assert True










