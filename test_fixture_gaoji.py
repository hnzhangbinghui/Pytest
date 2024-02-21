import pytest

@pytest.fixture()
# @pytest.fixture(autouse=True)
# @pytest.fixture(scope='class',autouse=True)
def before():
    print('\n----before test------')
#方法1：通过参数引用的形式；
class Test_A():
    def test_a(self,before):
        '''
        :param before: 传入被fixture标识的函数，已变量的形式；
        '''
        print('测试test_a')
        assert 1
#方法2：通过函数引用；
@pytest.mark.usefixtures('before')
class Test_B():
    def setup(self):
        print('setup----------')
    def test_b(self):
        print('test_b-----------')
        assert 1
    def teardown(self):
        print('\nteardown---------')

#方法3：默认设置为运行，需要设置为：@pytest.fixture(autouse=True)
#方法4：设置作用于为function,自动运行,每个方法都会运行一次；还可以设置为class，只运行一次；
class Test_C():
    def setup(self):
        print('setup----------')

    def test_c(self):
        print('test_c-----------')
        assert 1
    def test_d(self):
        print('test_d-----------')
        assert 1
    def teardown(self):
        print('\nteardown---------')

#5、利用fixture的固定返回值；
@pytest.fixture()
def need_data():
    return 2  #返回数字2

class Test_D():
    def test_e(self,need_data):
        print('test_e--------')
        assert need_data == 3  #拿到返回值做进一步断言；

#6、利用fixture的参数param；
@pytest.fixture(params=[1,2,3])
def need_list(request):       #传入参数request，系统封装参数；
    return request.param      #取列表中的单个值，默认的取值方式；

class Test_F():
    @pytest.mark.parametrize('v',[1,2,3])
    def test_f(self,need_list,v):
        print('传参的形式执行test_f')
        assert need_list == v  #断言need_data是否跟参数的值是否相等；


'''
1、根据特定的条件，不执行标识的测试函数.
 方法：skipif(condition, reason=None)
 参数：condition：跳过的条件，必传参数，reason：标注原因，必传参数
 使用方法：@pytest.mark.skipif(condition, reason="xxx")；
 2、关于skip，无条件跳过，被标记的类中所有方法测试用例都会被跳过；
    skipif，被标记的类，当条件为Ture时，会被跳过，否则不跳过；
3、标记测试函数为失败函数
 方法： xfail(condition=None, reason=None, raises=None, run=True, strict=False)
 常用参数：condition：预期失败的条件，必传参数，reason：失败的原因，必传参数
 使用方法：@pytest.mark.xfail(condition, reason="xx")'''
class Test_G():
    def setup_class(self):
        print('类模块的启动，只启动一次----开始启动-----')
    def teardown_class(self):
        print('\n------类模块的结束---------')
    def test1(self):
        print('---------test1----------')
        assert 1
    @pytest.mark.skipif(condition=2>1,reason='跳过该函数')
    def test2(self):
        print('\n-------跳过test2-----------')
        assert 1
    @pytest.mark.xfail(2>1,reason="标注为预期失败")
    def test3(self):
        print('-------标注为预期失败-------')
        assert 1
    @pytest.mark.skip()
    def test4(self):
        print('----无条件的全部跳过---------')


























# if __name__=='__main__':
#     pytest.main('-s -v test_fixture_gaoji')













