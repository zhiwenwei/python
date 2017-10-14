#coding:utf-8
#Author:zhiwenwei

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sex = "normal"
    def talk(self):
        print("person is talking...")
class BlackPerson(Person):
    def __init__(self,name,age,strength):#先继承再重构
        super(BlackPerson,self).__init__(name,age)
        self.strength = strength
        print(self.name,self.age,self.sex)
    def talk(self):
        print("blackperson is talking")
    def walk(self):   #如果与父类方法重复，用自己的
        print("person is walking")
b = BlackPerson("zww",10,"streng")
b.talk()
b.walk()