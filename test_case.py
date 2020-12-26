import pytest
from counter.Counter_demo import Counter
from conf import get_datas

#获取测试用例需要的数据及别名
all_datas = get_datas.get_param("datas.yml")
print(type(all_datas))
#获取加法运算的用例及别名
add_params = all_datas['add_datas']
ids_add_params = all_datas['ids_add_datas']
#获取减法运算的用例及别名
minus_params = all_datas['minus_datas']
ids_minus_params = all_datas['ids_minus_datas']
#获取乘法运算的用例及别名
multiply_params = all_datas['multiply_datas']
ids_multiply_params = all_datas['ids_multiply_datas']
#获取除法运算的用户及别名
divide_params = all_datas['divide_datas']
ids_divide_params = all_datas['ids_divide_datas']


class TestCaseDemo:
    #类方法运行之前输出内容
    def setup_class(self):
        self.t = Counter()
        print('\n----------计算器方法测试：start！----------')

    # 类方法运行之前输出内容
    def teardown_class(self):
        print('\n----------计算器方法测试：end！----------')

    #每个用例开始执行之前输出内容
    def setup(self):
        print('\n----------测试用例开始执行----------')
    def teardown(self):
        print('\n----------测试用例执行结束！----------')

    #加法运算的测试
    @pytest.mark.parametrize('a,b,expect',add_params,ids=ids_add_params)
    def test_add(self,a,b,expect):
        result = self.t.add(a,b)
        assert result == expect
    #减法运算的测试
    @pytest.mark.parametrize('a,b,expect',minus_params,ids=ids_minus_params)
    def test_case_minus(self,a,b,expect):
        result = self.t.minus(a,b)
        assert result == expect
    #乘法运算的测试
    @pytest.mark.parametrize('a,b,expect',multiply_params,ids=ids_multiply_params)
    def test_case_multiply(self,a,b,expect):
        result = self.t.multiply(a,b)
        assert result == expect
    #除法运算的测试
    @pytest.mark.parametrize('a,b,expect',divide_params,ids=ids_divide_params)
    def test_case_divide(self,a,b,expect):
        result = self.t.divide(a,b)
        assert result == expect

