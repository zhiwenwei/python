#-*- coding:utf-8 -*-
#Author:ZhiWenwei

class Dog():
    def __init__(self):   #构造函数，初始化作用，该类被实例化的时候回执行
        pass
    def __del__(self):  #析构函数,自动触行释放内存空间
        print("析构函数主要是用来释放内存空间的")
d = Dog()
#画图说明类和对象在内存中的关系。（提示：对象中存有类的指针）
class A():
    def __init__(self):
        pass
    def run(self):
        print("run")

a = A()
print(id(A()))
print(id(a))