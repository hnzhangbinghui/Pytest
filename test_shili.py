import pytest
import allure

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

@allure.feature('*****测试类*****')
class TestFunc():
    @classmethod
    def setup_class(cls):
        print('setup_class')

    def setup(self):
        print('setup')

    @pytest.mark.fail
    @allure.story('测试用例1')
    def test_answer1(self):
        print('test_answer1')
        assert func(3) == 5

    @pytest.mark.success
    @pytest.mark.parametrize("input,expect", {
        (5, 6),
        (7, 8),
        (0, 1),
        (2, 2)
    })
    @allure.story('测试用例2并进行参数化')
    def test_answer2(self, input, expect):
        print('test_answer2')
        assert func(input) == expect
    @allure.story('测试用例3')
    def test_answer3(self):
        print('test_answer3')
        assert func(7) == 8
        with allure.step("测试"):
            allure.attach('添加数据成功！！！')

    def teardown(self):
        print('teardown')

    @classmethod
    def teardown_class(cls):
        print("teardown_class")


'''
pytest支持分组：
1、@pytest.mark.webtest
2、@pytest.mark.sec
3、pytest -m "webtest and not sec"
4、在terminal里输入命令，pytest -m fail 来实现只执行指定的用例case的目的；
5、参数化用例方法可以达到代码重复利用的效果，单独来执行test_answer2这个用例方法会发现实际执行了4次该方法，
    input和expect的值分别是参数化（5,6），（7,8），（0,1），（2,2）
'''
