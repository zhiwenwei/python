#coding:utf-8
#Author:zhiwenwei
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s"%(self.name,self.score))


zhangsan = Student('zhangsan',90)
lisi = Student('lisi',50)
zhangsan.print_score()
lisi.print_score()