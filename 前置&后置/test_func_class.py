# coding:utf-8

import pytest


# 类和方法
"""
从运行结果看出，setup_module/teardown_module 的优先级
是最大的，然后函数里面用到的 setup_function/teardown_function
不类里面的 setup_class/teardown_class 互丌干涉
"""

def setup_module():
    print("\nsetup_module：整个.py 模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("\nteardown_module：整个.py 模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")


def setup_function():
    print("setup_function：每个用例开始前都会执行11111")


def teardown_function():
    print("teardown_function：每个用例结束前都会执行11111")


def test_one():
    print("\n正在执行----test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("\n正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')


class TestCase():


    def setup_class(self):
        print("setup_class：所有用例执行之前22222")


    def teardown_class(self):
        print("teardown_class：所有用例执行之前22222")

    def test_three(self):
        print("\n正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("\n正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')


if __name__ == "__main__":
    pytest.main(["-v", "test_func_class.py"])
