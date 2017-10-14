#coding:utf-8
#Author:zhiwenwei
'''一：定义一个学生类。有下面的类属性： 
1 姓名 
2 年龄 
3 成绩（语文，数学，英语)[每课成绩的类型为整数] 
类方法： 
1 获取学生的姓名：get_name() 返回类型:str 
2 获取学生的年龄：get_age() 返回类型:int 
3 返回3门科目中最高的分数。get_course() 返回类型:int 
写好类以后，可以定义2个同学测试下: 
zm = Student('zhangming',20,[69,88,100]) 
返回结果： 
zhangming 
20 
100 '''
class Student(object):
    def __init__(self,name,age,sorce):
        self.name = name
        self.age = age
        self.sorce = sorce

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_sorce(self):
        return self.sorce
s = Student('zhangsan',22,[60,17,89])
print(s.get_name(),s.get_age(),s.get_sorce())

""" 
二：定义一个字典类：dictclass。完成下面的功能： 
dict = dictclass({你需要操作的字典对象}) 

1 删除某个key 

del_dict(key) 

2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found" 

get_dict(key) 

3 返回键组成的列表：返回类型;(list) 

get_key() 

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list) 
update_dict({要合并的字典}) 
"""
class Dictclass(object):
    def __init__(self,dict):
        self.dict = dict
    '''删除某个key'''
    def dict_del(self,key):
        if key in self.dict.keys():
            self.dict.pop(key)
            return self.dict
        else:
            print("no found")
    '''判断key'''
    def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            print("no found")
D = {'k1':123,'k2':'shabi','k3':12345}
s = Dictclass(D)
print(s.dict_del('k1'))
print(s.get_dict('k0'))
