#-*- coding:utf-8 -*-
#Author:Kevin

class Dog(object):
    def __init__(self,name):   #传参数，叫构造函数也叫构造方法也叫类的初始化方法，其中self就是实例本身
        self.N = name
    def shiyan(self):  #类的方法
        print("i am a dog,my name is %s"%self.N)

d = Dog("xiaohei") #实例化，实例后的对象叫实例，其中d就是实例
d.shiyan()

