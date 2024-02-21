import unittest  # 导入unittest模块

def number_sum(a, b):
    return a + b

"""
setUp():每个测试case运行之前运行
tearDown():每个测试case运行完之后执行
setUpClass():必须使用@classmethod 装饰器,  所有case运行之前只运行一次
tearDownClass():必须使用@classmethod装饰器, 所有case运行完之后只运行一次

"""

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    # def setUp(self):
    #     print("setUp")

    def test_sum_int(self):
        print('1111')
        self.assertEqual(number_sum(1, 2), 3)
        self.assertEqual(number_sum(100, 300), 400)

    def test_sum_number(self):
        print('222')
        self.assertEqual(number_sum(1.1, 2.2), 3.3,msg='数值不相等，断言失败')
    #
    # def tearDown(self):
    #     print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()