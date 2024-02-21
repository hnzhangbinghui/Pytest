import pytest


class TestCase:

    # 通过装饰器@pytest.mark.dependency()标记当前用例为被依赖用例，被依赖用例需要优先关联用例执行
    @pytest.mark.dependency()
    def test_01(self):
        print("测试用例01，执行失败")
        # assert 1 == 1

    # 通过使用装饰器关联被依赖用例，通过depends参数指定用例名称关联用例
    @pytest.mark.dependency(depends=['test_01'])
    def test_02(self):
        print("测试用例02，跳过")

    # 标记被依赖用例时，可以通过name参数指定别名
    @pytest.mark.dependency(name="func_2")
    def test_03(self):
        print("测试用例03，执行成功！")

    # 使用depends参数指定定义的别名关联用例
    @pytest.mark.dependency(depends=['func_2'])
    def test_04(self):
        print("测试用例04，执行成功！")

    # depends参数可以关联多个测试用例，使用“,”分隔即可
    @pytest.mark.dependency(depends=['test_01', 'func_2'])
    def test_05(self):
        print("测试用例05，跳过")


if __name__ == '__main__':
    pytest.main(['-vs'])
