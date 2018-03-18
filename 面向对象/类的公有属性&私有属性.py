#-*- coding:utf-8 -*-
#Author:Kevin
'''
在类里面定义的属性叫做公有属性
'''

class Dog(object):
    kind = "哈士奇" #类的公有属性
    def __init__(self,name):
        self.N = name
        self.__heart = 'normal'
    def sayhi(self):
        #self.__heart = 'Die'
        print('i am a dog,my name is ',self.N,self.__heart)
    # def shiyan(self):  #对外部提供访问私有属性接口
    #     return self.__heart

d = Dog('xiaohei')
print(d.kind)
d.kind = "秋田"  #修改类的公有属性
print(d.kind)
d.sayhi()
print(d._Dog__heart) #强制访问私有属性
# print(d.shiyan())
'''
类的私有属性：
'''
