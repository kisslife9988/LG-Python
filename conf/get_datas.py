import yaml
#获取测试用例数据及别名信息并返回值
def get_param(path):
    with open(path) as f:
        param = yaml.safe_load(f) #获取F文件的所有数据信息并以字典格式进行返回
        print(param)
    return param
if __name__ == '__main__':
    get_param("../datas.yml")
