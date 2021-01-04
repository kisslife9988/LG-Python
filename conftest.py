import pytest
from counter.Counter_demo import Counter
from conf.get_datas import get_param
from conf.get_file_path import data_path

# 获取计算器实例
@pytest.fixture(scope="class")
def get_calc():
    print('获取计算机实例')
    calc = Counter()
    return calc

#模块执行前/后的操作
@pytest.fixture(scope='module')
def start_print():
    print('\n--------开始计算--------')
    yield
    print('\n--------计算结束--------')


#获取测试用例需要的数据及别名
all_datas = get_param(data_path)
# print(all_datas)

#通过fixture方式获取加法的用例数据及别名信息
@pytest.fixture(params=all_datas['add_datas'],ids=all_datas['ids_add_datas'])
def get_add_datas(request):
    data = request.param
    print(f"\n测试数据：{data}")
    yield data


#通过fixture方式获取减法的用例数据及别名信息
@pytest.fixture(params=all_datas['minus_datas'],ids=all_datas['ids_minus_datas'])
def get_minus_datas(request):
    data = request.param
    print(f"\n测试数据：{data}")
    yield data

#通过fixture方式获取乘法的用例数据及别名信息
@pytest.fixture(params=all_datas['multiply_datas'],ids=all_datas['ids_multiply_datas'])
def get_multiply_datas(request):
    data = request.param
    print(f"\n测试数据：{data}")
    yield data


#通过fixture方式获取除法的用例数据及别名信息
@pytest.fixture(params=all_datas['divide_datas'],ids=all_datas['ids_divide_datas'])
def get_divide_datas(request):
    data = request.param
    print(f"\n测试数据：{data}")
    yield data
