# coding:utf-8

import pytest

"""
pytest.mark.parametrize装饰器实现测试用例参数化
"""


@pytest.mark.parametrize("a,b",[(1,2),(3,3),(4,5),('abc','abc')])
@pytest.mark.canshuhua      # pytest的自定义标记
def test01(first,a,b):
    """调用conftest和进行参数化测试"""
    assert a == b

#
# # 通过标记为失败的用例就不运行了，直接跳过显示xfailed
# @pytest.mark.parametrize("m,n",[(1,2),(2,2),pytest.param(1,2,marks=pytest.mark.xfail),])
# def test02(m,n):
#     print("********开始用例*******")
#     assert m == n


# 参数组合,如果想要多个参数化参数的所有组合，可以堆叠参数化装饰器
# 如下图结果得到25个测试用例
@pytest.mark.skip(reason="test_skip")
@pytest.mark.parametrize("x",[1,2,3,4,5])
@pytest.mark.parametrize("y",[2,1,3,5,4])
def test03(x,y):
    """添加断言，并输出异常信息，方便定位问题"""
    # assert x == y,"判断两个数值{0},{1}是否相等:".format(x,y)
    assert x == y, "判断两个数值x,y是否相等:x=%s,y=%s"%(x,y)




if __name__=='__main__':
    pytest.main(["-s","test_parametrize.py,-m='canshuhua'"])








