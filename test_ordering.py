import pytest

'''
pytest-ordering，pytest在执行时，默认是按照文件中用例的先后顺序执行，如果要修改用例的执行顺序时，修改代码是不利于维护。
可以使用pytest-ordering，可以快速实现用例执行顺序的设置。
安装：pip install pytest-ordering；
使用：通过给用例添加装饰器@pytest.mark.run(order=执行顺序)，设置用例的执行顺序。在执行时，
使用装饰器@pytest.mark.run的用例会优先没有装饰器的用例执行。都设置了执行顺序的用例则按照order参数设置的大小升序执行；
'''

class TestCase():
    @pytest.mark.run(order=4)
    def test_01(self):
        print('测试用例1')

    @pytest.mark.run(order=3)
    def test_02(self):
        print('测试用例2')
    #使用装饰器设置执行顺序为2；
    @pytest.mark.run(order=2)
    def test_03(self):
        print('测试用例3')

    @pytest.mark.run(order=1)
    def test_04(self):
        print('测试用例04')
if __name__=='__main__':
    pytest.main('-vs' 'test_ordering.py')










