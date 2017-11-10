#coding:utf-8
#Author:zhiwenwei
class Student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.count += 1
# if __name__ == '__main__':
Student1 = Student('CaiYongping',19)
print(Student1.__dict__)
print(Student.count)
Student2 = Student('ZhouYouxian',17)
print(Student2.__class__)
print(Student.count)