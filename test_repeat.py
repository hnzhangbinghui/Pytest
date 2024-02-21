
import pytest

# @pytest.mark.repeat(100)
# def test_1():
#     print("\n重新运行测试")
#     import random
#     flag = random.choice([True, False])
#     print(flag)
#     assert flag

def test_2():
    print("重新运行测试")
    assert 1 == 1
if __name__=="__main__":
    pytest.main(["-vs" ,'test_repeat.py'])
#pytest -vs --count=20 -x C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test_repeat.py
#pytest -vs  --count=10 --repeat-scope=function -x C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test_repeat.py
