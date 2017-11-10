#-*- coding:utf-8 -*-
#Author:Kevin
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def tell(self):
        print("%s-%s-%s"%(self.year,self.month,self.day))
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(People):
    def __init__(self,name,age,sex,year,month,day):
        People.__init__(self,name,age)
        self.sex = sex
        self.birth = Date(year,month,day)
student = Student('Kevin',25,'man',2017,10,17)
print("%s"%student.birth)
student.birth.tell()