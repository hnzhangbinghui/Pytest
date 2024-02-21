# coding :utf-8


import pytest


@pytest.fixture(scope="module")
def open():
    print("\n打开浏览器，并且打开百度首页")

    yield
    print("执行teardown")
    print("最后关闭浏览器")


def test_s1(open):
    print("\n用例 1：搜索 python-1")


def test_s2():
    print("\n用例 2：搜索 python-2")

@pytest.mark.teshu
def test_s3(open):
    print("\n用例 3：搜索 python-3")


if __name__=='__main__':
    pytest.main(["-s","test_f1.py","-m='teshu'"])










