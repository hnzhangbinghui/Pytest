'''
1、为了提高复用性，在编写用例时，会用到不同的fixture，比如常见的登录，大部分用例的前置条件；
2、假设不同的用例需要登录不同的测试账号，就需要用传参的方式来登录，不能把登录的fixture写死；
3、如果需要传多个参数，需要通过字典去传；
4、
'''
import pytest

@pytest.fixture()
def aaa(request):
    name = request.param
    print(f"************账号是：{name}")
    return name
data = ["zhangbinghui", "zbh"]
ids = [f"login_name is {name}" for name in data]

# 添加indirect=True，是为了把aaa当成一个函数去执行，而不是一个参数，并把data当做参数传入函数；
@pytest.mark.parametrize("aaa", data, ids=ids, indirect=True)
# 这里是获取aaa是获取fixture的返回值；
def test_name(aaa):
    print(f"\n测试用例的登录账号是：{aaa}")


@pytest.mark.parametrize("test",data)
def test_2(test):
    print("\n直接获取列表参数的值：",test)

data = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
]
@pytest.mark.parametrize("test",data)
def test_2(test):
    print("\n直接获取字典列表参数的值：",test.keys())


#多个fixture，只加一个装饰器；
@pytest.fixture(scope="module")
def input_user(request):
    user=request.param
    return user

@pytest.fixture(scope="module")
def input_psw(request):
    psw=request.param
    return psw

data = [
    ("name1", "pwd1"),
    ("name2", "pwd2")
]
@pytest.mark.parametrize("input_user,input_psw",data,indirect=True)
def test_more_fixture(input_psw,input_user):
    print("\nfixture返回的内容是：",input_user,input_psw)


# 多个fixture(叠加装饰器)
@pytest.fixture(scope="function")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user

@pytest.fixture(scope="function")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw

name = ["name1", "python"]
pwd = ["pwd1", "11111111111"]

@pytest.mark.parametrize("input_user", name, indirect=True)
@pytest.mark.parametrize("input_psw", pwd, indirect=True)
def test_more_fixture(input_user, input_psw):
    print("fixture返回的内容:", input_user, input_psw)

if __name__ == "__main__":
    pytest.main(["-vs", "test_chuancan.py"])
