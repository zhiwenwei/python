#-*- coding:utf-8 -*-
#Author:Kevin
'''staticmethod静态方法'''
class Dog(object):
    name = "jdklas"
    def __init__(self,name):
        self.name = name
    @staticmethod
    def eat(): #静态方法:只是名义上归类管理，实际访问不了类或实例中的任何属性
        print("%s is eating"% self.name)

d = Dog("hashiqi")
d.eat()

'''类方法：classmethod'''
class Dog1(object):
    name = 'ha'
    def __init__(self,name):
        self.name = name
    @classmethod
    def eat(self):
        print("%s is eating"%self.name)
d1 = Dog1('erha')
d1.eat()
'''属性方法：property'''

