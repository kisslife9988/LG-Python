import pytest

class TestCaseDemo:

    #加法运算的测试
    @pytest.mark.run(order=0)
    def test_case_add(self,start_print,get_calc,get_add_datas):
        result = get_calc.add(get_add_datas[0],get_add_datas[1])
        if isinstance(result,float):
            result = round(result,2)
        assert result == get_add_datas[2]

    #除法运算的测试
    @pytest.mark.run(order=3)
    def test_case_divide(self,get_calc,get_divide_datas):
        result = get_calc.divide(get_divide_datas[0],get_divide_datas[1])
        assert result == get_divide_datas[2]

    #减法运算的测试
    @pytest.mark.run(order=1)
    def test_case_minus(self,get_calc,get_minus_datas):
        result = get_calc.minus(get_minus_datas[0],get_minus_datas[1])
        assert result == get_minus_datas[2]
    #乘法运算的测试
    @pytest.mark.run(order=2)
    def test_case_multiply(self,get_calc,get_multiply_datas):
        result = get_calc.multiply(get_multiply_datas[0],get_multiply_datas[1])
        assert result == get_multiply_datas[2]


