# coding :utf-8


import pytest


def test_s4(login):
    print("\n用例4:登录后其它动作111")


def test_s5(): #不传login
    print("\n用例5:不需要登录操作222")


if __name__=='__main__':
    pytest.main(["-s","test_fix.py"])










