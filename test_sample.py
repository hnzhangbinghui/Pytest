# -*- coding: utf-8 -*-
"""
# @Time    : 2023/03/18
# @Author  : zhangbinghui
# @Description : 关于pytest的学习；
"""

import pytest


class TestClass:
    # def __init__(self):
    #     self.x = 1
    #     self.y = "hello"
    x = 1
    y = "hello"

    def test_one(self):
        print('第一个测试方法')
        assert self.x == 1

    def test_two(self):
        print('第二个测试方法')
        assert 'h' in self.y
    #
    # def test_three(self):
    #     print('第三个测试方法')
    #     assert hasattr(self.y, "hello")


if __name__ == '__main__':
    pytest.main(["-q test_sample.py"])
