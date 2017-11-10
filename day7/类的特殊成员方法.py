#-*- coding:utf-8 -*-
#Author:Kevin
'''__doc__表示类的描述信息,一般是三重号内的注释信息
__module__表示当前操作的对象在哪个模块
__class__表示当前操作的对象的类是什么
__init__构造方法，通过类创建对象时，自动触发执行
__del__析构方法，当对象在内存中释放时，自动触发执行
__dict__ 类的字典属性、名称空间
__base__ 类的第一个父类
'''
class Student(object):
    '''在类内部定义的属性属于类本身的,由操作系统只分配一块内存空间,大家公用这一块内存空间'''
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.count +=1
class Teacher(Student):
    def __init__(self,name,age,lesson):
        super(Teacher,self).__init__(name,age)
        self.lesson = lesson
        # print("My name is %s.I am %s years old I am your %s teacher"%(self.name,self.age,self.lesson))
    def t_info(self):
        print("My name is %s.I am %s years old I am your %s teacher" % (self.name, self.age, self.lesson))

student1 = Student("Kevin",24)
student2 = Student("Jay",28)
teacher1 = Teacher("alex",24,"English")
teacher1.t_info()
print("__doc__:",Student.__doc__)
print("__module__:",student1.__module__)
print("__class__:",student2.__class__)
print("__dict__:",student2.__dict__)
print("__bash__:",Teacher.__base__)