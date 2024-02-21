import pytest

# pytest 可以支持自定义标记，自定义标记可以把一个 web 顷目划
# 分多个模块，然后指定模块名称执行。

@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app


def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass
    def test_method2(self):
        pass


if __name__ == '__main__':
    # pytest.main(["-v test_mark.py::TestClass"])
    pytest.main(["-v -k another test_mark.py"])




























