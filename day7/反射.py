#coding:utf-8
#Author:zhiwenwei
'''
反射
    hasattr（obj,name_str）  判断一个对象obj里是否有对应的name_str字符串的方法,返回一个布尔值
    getattr(obj,name_str)     根据字符串去获取obj对象里的对应的方法的内存地址
    setattr(obj,'y',z)
    delattr
'''


class Foo(object):
    def __init__(self):
        self.name = 'zhangsan'
    def func(self):
        return 'func'
obj = Foo()
print(hasattr(obj,'func1'))   #检查是否有成员
print(getattr(obj,'name'))    #获取成员
setattr(obj,'age',18)         #设置成员
print(obj.age)
delattr(obj,'name')  #删除成员
print(obj.name)