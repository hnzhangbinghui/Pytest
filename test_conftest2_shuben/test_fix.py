# coding :utf-8


import pytest


# # 不带参数默认是scope=“function”
# @pytest.fixture()
# def login():
#     print("\n输入账号密码登录")


def test_s1(login):
    print("\n用例1:登录后其它动作111")


def test_s2(): #不传login
    print("\n用例2:不需要登录操作222")


def test_s3(login):
    print("\n用例3:登录后其它动作333")


if __name__=='__main__':
    pytest.main(["-s","test_fix.py"])










