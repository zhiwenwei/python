#coding:utf-8
#Author:Mr Zhi
"""
1.#
11. 有如下变量，请实现要求的功能
        tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

        a. 讲述元祖的特性
          元组也叫只读列表，跟列表差不多，它只有两个方法，一个是count，一个是index

        b. 请问tu变量中的第一个元素 “alex” 是否可被修改？
            元组不可直接被修改，需要转换成列表或字典

        c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
             k2是字典的键，对应的值是列表可修改：tu[1][2]['k2']='Seven'
        d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
            k3是字典的键，对应的值是列表不可修改
"""
total = 0
i = 0
while (i < 100):
    i +=1
    if i % 2==0:
        total -=i
    else:
        total +=i
print(total)