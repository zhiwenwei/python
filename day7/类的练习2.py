#coding:utf-8
#Author:zhiwenwei
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj1 = Student('XiaoMing',18)  #将XiaoMing和18分别封装到name和age属性中
obj2 = Student('zww',24)       #将zww和24分别封装到name和age属性中
print(obj1.name,obj1.age)      #直接调用封装的内容：对象.属性名

