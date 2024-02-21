# -*-coding:utf-8 -*-
# coding:utf-8
"""
# @time : 20230330
# @author: Zhangbinghui
# @description:关于module前置和后置条件的设置
"""
# 函数式
"""
模块
setup_module 是所有用例开始前叧执行一次，
teardown_module 是所有用例结束后叧执行一次
"""

import pytest


def setup_module():
    print("setup_module,整个 .py 模块只执行一次，比如所有用例开始前打开一次浏览器")
    print("开始执行模块... ..")


def teardown_module():
    print("teardown_module，整个 .py 模块只执行一次，比如所有用例结束后关闭浏览器")
    print("结束整个模块的执行，测试结束。")


def setup_function():
    print("\nsetup_function,每个用例开始前都会执行")
    print("开始执行测试用例... ...")


def teardown_function():
    print("\nteardown_function,每个用例结束后都会执行")
    print("用例测试结束了，拜拜。")


def test1():
    print('\n开始第一个用例测试... ...')
    x = 2
    assert x == 2


def test2():
    print('\n开始第二个用例测试... ...')
    x = 'hello'
    assert x in "hellopython"


if __name__ == "__main__":
    pytest.main(["-s test_module_qianzhi.py"])



