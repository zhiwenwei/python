#coding:utf-8
#Author:zhiwenwei
class Dog(object):
    def __init__(self,name):
        self.name = name
    @staticmethod  #把eat变为静态方法
    def eat():
        print(" is eating")
d = Dog("XiaoHei")
d.eat()