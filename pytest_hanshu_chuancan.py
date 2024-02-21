# coding:utf-8

"""
为了提高代码的复用性，我们在写用例的时候，会用到函数，然后
 丌同的用例去调用返个函数。比如登录操作，大部分的用例都会先登录，
 那就需要把登录单独抽出来写个函数，其它用例全部的调用返个登陆函
 数就行。
 测试用例传参需要用装饰器@pytest.mark.parametrize，里面写两个参数
第一个参数是字符串，多个参数中间用逗号隔开
第二个参数是 list,多组数据用元祖类型
 """

import pytest
from anaconda.Pytest.data.link_oracle import link_oracle
sel_slq2="SELECT FCODE ,'Ysstech123!@#' AS 默认密码  FROM T_BASE_USER tbu"
import requests

# 测试登录数据
test_login_data=link_oracle(sel_slq2)


def login(user, psw):
    print("\n登录账号：%s"%user)
    print("登录密码：%s"%psw)
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize("user,psw",test_login_data)
def test_login(user, psw):
    result=login(user,psw)
    assert result == True,"失败原因，密码为空"


if __name__ == "__main__":
    pytest.main(["-s pytest_hanshu_chuancan.py"])










