#coding:utf-8
#Author:zhiwenwei
class SchoolMember(object):
    member = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()
    def enroll(self):
        '''注册'''
        print("just enrolled a new school member %s"%self.name)
        SchoolMember.member +=1
    def tell(self):
        print("----info:%s-----"%self.name)
        for k,v in self.__dict__.items():
            print('\t',k,v)

    def __del__(self): #析构函数
        print("开除了%s"%self.name)
        SchoolMember.member -= 1
class Teacher(SchoolMember):
    '''教师类'''
    def __init__(self,name,age,sex,salary,course):
        # SchoolMember.__init__(self,name,age,sex)  #经典类写法
        super(Teacher,self).__init__(name,age,sex)  #新式类写法
        '''
        class Person(object): #新式类，统一使用新式类
        class Person  #经典类
        '''
        self.salary = salary
        self.course = course
    def teacher(self):
        print("Teacher %s is teaching %s"%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,cource,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.cource = cource
        self.tuition = tuition
        self.amount =0
    def pay_tuition(self,amount):
        print("student %s has just paied %s"%(self.name,self.amount))
        SchoolMember.amount += amount
t1 = Teacher("alex",24,"F",3000,"python")
s1 = Student("zww",24,"f","python",100000)
s2 = Student("zhangsan",24,"f","go",100000333)
# print(SchoolMember.member)
# print(s2.__dict__)
# del s2
s1.tell()