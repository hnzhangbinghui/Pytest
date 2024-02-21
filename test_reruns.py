
import pytest

@pytest.mark.flaky(reruns=5)
def test_1():
    print("重新运行测试")
    assert 1 == 1


if __name__=="__main__":
    pytest.main(["-vs" ,'test_reruns.py'])

# pytest -vs --reruns 5 --reruns-delay 3   C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test_reruns.py












