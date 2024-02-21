# -*-coding:utf-8 -*-
# coding:utf-8
"""
# @time : 20230330
# @author: Zhangbinghui
# @description:关于函数式的前置和后置条件的设置
"""

"""
函数的前置和后置
setup_function/teardown_function,每个用例开始和结束调用一次
"""

import pytest


def setup_function():
    print("\nsetup_function,每个用例开始前都会执行")
    print("开始执行测试用例... ...")


def teardown_function():
    print("\nteardown_function,每个用例结束后都会执行")
    print("用例测试结束了，拜拜。")


def test1():
    print('\n开始第一个用例测试... ...')
    x=2
    assert x == 2


def test2():
    print('\n开始第二个用例测试... ...')
    x='hello'
    assert x in "hellopython"


if __name__=="__main__":
    pytest.main(["-s test_hanshu_qianzhi.py"])

































