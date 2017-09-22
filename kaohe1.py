#coding:utf-8
#Author:Mr Zhi
import copy
# a = "i love python"
# b = a
# a1 = copy.copy(a)
# a2 = copy.deepcopy(b)
# print(id(a))
# print(id(b))
# print(id(a1))
# print(id(a2))

# D = {'k1':'v1','k2':123,'k3':["str1",469]}
# D2 = copy.copy(D)  #浅拷贝，额外创建第一层（变量名id改变，对象id不变，还是引用旧对象）
# print(id(D))
# print(id(D2))
# print(id(D["k1"]))
# print(id(D2["k1"]))
# D = {'k1':'v1','k2':123,'k3':["str1",469]}
# D["k3"][0] = "gaibian"
# D["k1"] = "value"
# D2 = copy.deepcopy(D)
# print(id(D))
# print(id(D2))
# print(id(D["k3"]))
# print(id(D2["k3"]))
# print(id(D["k2"]))
# print(id(D2["k2"]))
# print(D)
# print(D2)
# dict = {"cpu":[100],"mem":[200],"disk":[300]}
# new_dict = copy.deepcopy(dict)
# new_dict["cpu"][0] = 90
# print(new_dict)
# print(dict)
# import sys
# sys.path.append("D:\\软件\\python\\day5")
# print(sys.path)
import re
re.match().group()