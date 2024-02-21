import pytest
def return_test_data():
    return [(1,2),(4,8)]


class TestCase():
    def setup_class(self):
        print('---测试前准备开始---')
    def teardown_class(self):
        print('-------测试结束收尾-----------')
    #单个参数测试
    @pytest.mark.parametrize('a',[3,6,7,8,9])
    def test_a(self,a):
        print("获得测试数据是：%d" %a)
        assert a%3==0
    #多个参数测试,参数的值也可以从函数中获取；
    # @pytest.mark.parametrize("a,b",[(1,2),(4,8)])
    @pytest.mark.parametrize("a,b",return_test_data())
    def test_b(self,a,b):
        print('依次获得a，b的值分别是：%d %d' %(a,b))
        assert a+b==3
if __name__=='__main__':
    pytest.main("-s -v test_params.py")









