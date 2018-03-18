#-*- coding:utf-8 -*-
#Author:Kevin
class Baseclass(object):
    def foo1(self):
        print("helo",self)
    @staticmethod
    def get_list(cls):
        print("hello2",cls)

s = Baseclass()
s.foo1()
Baseclass.get_list("bit")