#coding:utf-8
#Author:zhiwenwei
class Dog(object):
    def __init__(self,name): #传参数，叫构造函数也叫构造方法==初始化方法
        self.NAME = name
    def sayhi(self):  #类的方法
        print("hello,i am a dog,my name is ",self.NAME)
    def eat(self,food):
        print("%s is eating %s"%(self.NAME,food))
#上面只是定义类，下面把类实例化
d = Dog("zhangsan")   #d相当于等于__init__(self,name)中的self，实例化后产生的对象叫实例
d2 = Dog("zhangsan2")
d.sayhi()
d2.sayhi()
d3 = Dog("bitch")
d .eat("shi")
