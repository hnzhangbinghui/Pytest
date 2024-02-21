from __future__ import print_function
import pytest

# @pytest.fixture(scope='class')
# def resource_a_setup(request):
#     print('\nresources_a_setup()')
#
#     def resource_a_teardown():
#         print('\nresources_a_teardown()')
#
#     request.addfinalizer(resource_a_teardown)
# # 调用fixture的三种方法；
# # 1、函数或类里面方法直接传fixture的函数参数名称；
# def test_1(resource_a_setup):
#     print('test_1()')
#
#
# def test_2():
#     print('\ntest_2()')
#
#
# def test_3(resource_a_setup):
#     print('\ntest_3()')


# 2、使用装饰器@pytest.mark.usefixtures()，修饰需要运行的用例；
# 3、叠加usefixtures，如果一个方法或者一个class用例想要同时调用多个fixture，可以
#    使用@pytest.mark.usefixture()进行叠加，注意叠加顺序先执行放低层，后执行的放上层；

# @pytest.fixture()
# def test1():
#     print('\n开始执行function1')
# @pytest.fixture()
# def test2():
#     print('\n开始执行function2')
#
# @pytest.mark.usefixtures('test2')
# @pytest.mark.usefixtures('test1')
# def test_a():
#     print('--------用例a执行------------')
#
# @pytest.mark.usefixtures('test2')
# @pytest.mark.usefixtures('test1')
# class TestClass():
#     def test_b(self):
#         print("-------用例b执行------------")
#
#     def test_c(self):
#         print('--------用例c执行-------------')

'''
usefixtures和fixture的区别；
如果fixture有返回值，那么usefixture就无法获取到返回值，这个是装饰器usefixture与用例传fixture参数的区别；
当fixture需要用到return出来的参数时，只能将参数名称直接当参数传入，不需要用到return出来的参数时，二者一样；
'''
# 4、fixture自动使用autouse=True
# 当用例很多时，每次传这个参数，比较麻烦，fixture里面有个参数autouse，默认是False没开启，可以设置为True开启自动
#   使用fixture功能，这样用例就不用每次都去传参了；


import pytest


@pytest.fixture(scope='module', autouse=True)
def test1():
    print('\n开始执行module')


@pytest.fixture(scope='class', autouse=True)
def test2():
    print('\n开始执行classs')


@pytest.fixture(scope='function', autouse=True)
def test3():
    print('\n开始执行function')


def test_a():
    print('-------用例a开始执行---------------')


def test_b():
    print('---------用例b开始执行--------------')


class TestCase():
    def test_c(self):
        print('&&&&&&&&&用例c开始执行&&&&&&&&&&&')

    def test_d(self):
        print('*********用例d开始执行************')
if __name__=='__main__':
    pytest.main(['-s,-v','test_child.py'])




