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
from anaconda.Pytest.data.link_oracle import *
import requests
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] # 设置字体
plt.rcParams["axes.unicode_minus"]=False # 该语句解决图像中的“-”负号的乱码问题
sel_slq2="SELECT FCODE ,'Ysstech123!@#' AS 默认密码  FROM T_BASE_USER tbu WHERE rownum <=10"


# 测试登录数据
test_login_data=link_oracle(sel_slq2)


def login(user, psw):
    url = "http://192.168.99.158:9080/acp-custody/rest/login/extend/userForLogin"

    # payload = "loginName=%s&password=%s&validType=0"%(user,psw)
    payload = {'loginName': user, 'password': psw,'validType':0}
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "192.168.99.158:9080",
        'accept-encoding': "gzip, deflate",
        'content-length': "53",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.elapsed.seconds)
    status= response.status_code
    print("\n登录账号：%s"%user)
    print("登录密码：%s"%psw)
    if status == 200:
        return True
    else:
        return False


succ_num=[]
@pytest.mark.parametrize("user,psw",test_login_data)
def test_login(user, psw):
    result=login(user,psw)
    assert result == True,"登录失败，请查看账号密码是否正确！！"
    if result ==  True:
        succ_num.append(1)
    return succ_num


def test_success():
    labels = link_oracle2(sel_slq2)
    values = succ_num

    # 创建柱状图
    fig, ax = plt.subplots()
    ax.bar(labels, values)

    # 设置标题和标签
    ax.set_title('统计数据库的账号人员登录系统的情况')
    ax.set_xlabel('登录用户名')
    ax.set_ylabel('登录状态')
    # 设置纵坐标刻度
    plt.yticks([0,1])

    # 显示图表
    plt.savefig('aaa.png')
    plt.show()



if __name__ == "__main__":
    pytest.main(["-s pytest_hanshu_chuancan.py"])










