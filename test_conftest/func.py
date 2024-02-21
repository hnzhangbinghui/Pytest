import yaml

path=r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test_conftest\data.yaml"


# 得到yaml字段的值
def get_yaml(param):
    with open(path,'r') as f:
        d=yaml.safe_load(f)
        return d[param]

# # 得到一个参数值的字典列表
# print(get_yaml("test"))
# # 得到一个参数列表
print(get_yaml("test_login_data"))
t=[]
print(len(get_yaml("test_login_data")))
for i in range(len(get_yaml("test_login_data"))):
    print((get_yaml("test_login_data")[i]))
    t.append(get_yaml("test_login_data")[i])
print(t[0])


# 更正yaml文件的值
def update_yaml():
    with open(path,'r') as f:
        data=yaml.safe_load(f)
        # 更新yaml文件内容
        data['account']=['zbh','ab']
        # 将更新后的内容下入yaml文件
        with open(path,'w') as file:
            yaml.dump(data,file)


# 通过占位符更新yaml的值
from string import Template
path2=r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Pytest\test_conftest\zhanweifu.yaml"


def update_bianhua(x,y):
    with open(path2,'r',encoding='utf-8') as f:
        d=f.read()
        t=Template(d)
        c=t.safe_substitute({"zhanghao":x,"mima":y})
    return c

# zhanghao: ab
# mima: Ysstech123!@#


update_bianhua("ab","Ysstech123!@#")


def get_lastest_yaml(a):
    cfg=yaml.safe_load(a)
    return cfg



get_lastest_yaml(update_bianhua("ab","Ysstech123!@#"))

