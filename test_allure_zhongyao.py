import pytest
import allure

#参考url：https://www.cnblogs.com/linuxchao/p/linuxchao-pytest-allure.html
@allure.feature("测试用例功能")  # feature定义功能；
class TestClass(object):

    @pytest.fixture(scope='function')
    def setup_function(request):
        def teardown_function():
            print("teardown_function called.")

        request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作

        print('setup_function called.')

    @pytest.fixture(scope='module')
    def setup_module(request):
        def teardown_module():
            print("teardown_module called.")
            request.addfinalizer(teardown_module)

        print('setup_module called.')

    @allure.story("功能测试用例1")  # story定义用户场景；
    @allure.step("这个是第一个测试用例！！")
    @pytest.mark.website
    def test_1(setup_function):
        print('Test_1 called.')

    @allure.story("功能测试用例2")
    def test_2(setup_module):
        file=open(r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test.png","rb").read()
        allure.attach(body=file,name='AAAAAAAAAAAAAA',attachment_type=allure.attachment_type.PNG)
        allure.attach.file(r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\cpu.jpg",attachment_type=allure.attachment_type.JPG)
        print('Test_2 called.')

    @allure.story("功能测试用例3")
    @allure.testcase("http://www.baidu.com","测试用例地址")
    @allure.link("http://wwww.baidu.com",name="BUG链接")
    @allure.severity('blocker')
    def test_3(setup_module):
        allure.attach.file(r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test.png",attachment_type=allure.attachment_type.PNG)
        print('Test_3 called.')
        assert 2 == 1 + 5

    @pytest.mark.skip()
    @allure.description("描述，跳过用例测试！！")
    @allure.severity("normal")
    def test_4(setup_module):
        print('Test_3 called.')
        assert 2 == 1 + 1



if __name__ == '__main__':
    pytest.main('-vs')



