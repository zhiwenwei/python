#-*- coding:utf-8 -*-
#Author:Kevin
class SchoolMember(object):
    '''学校类'''
    mumbers = 0 #学校初始人数为零
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def info(self):
        pass
    def enroll(self):
        '''注册'''
        SchoolMember.mumbers +=1
        print("new %s is enrolled,now there are %s members"%(self.name,SchoolMember.mumbers))

class Teacher(SchoolMember):
    '''讲师类'''
    def __init__(self,name,age,sex,salary,course):
        SchoolMember.__init__(self,name,age,sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        '''讲课方法'''
        print("Teacher %s is teaching %s for class %s"%(self.name,self.course,'s12'))

    def msg(self):
        '''讲师个人信息方法'''
        msg = """
        name:%s
        age:%s
        sex:%s
        course:%s
        """%(self.name,self.age,self.sex,self.course)
        print(msg)

class Student(SchoolMember):
    def __init__(self,name,age,sex,grade,sid):
        #SchoolMember.__init__(self,name,age,sex) #经典类写法
        super(Student,self).__init__(name,age,sex)  #新式类写法
        self.grade = grade
        self.sid = sid
        self.enroll()

    def s_msg(self):
        msg = """
        name:%s
        age:%s
        sex:%s
        grade:%s
        """%(self.name,self.age,self.sex,'s1')
        print(msg)

t1 = Teacher('alex',24,'男',100000,'python')
s1 = Student('zww',24,'男','python s6',10001)
t1.msg()
# s1.s_msg()
t1.teaching()