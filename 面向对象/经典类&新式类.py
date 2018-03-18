#-*- coding:utf-8 -*-
#Author:Kevin
class Schoolmember(object): #新式类
    pass
class Schoolmember:  #经典类
    pass


# SchoolMember.__init__(self,name,age,sex) #经典类写法
# super(Student, self).__init__(name, age, sex)  # 新式类写法
def create_teacher():
      teacher_dict = {}
      teacher_name = input("讲师姓名：")
      teacher_salary = input("讲师工资：")
      teacher_school = input("所属学校：")
      t1 = Teacher(teacher_name, teacher_salary, teacher_school)
      teacher_dict["姓名"] = t1.teacher_name
      teacher_dict["工资"] = t1.teacher_salary
      teacher_dict["所属学校"] = t1.teacher_school
      print(teacher_dict)

class Teacher(object):
     def __init__(self,teacher_name,teacher_salary,teacher_school):
         self.teacher_name = teacher_name
         self.teacher_salary = teacher_salary
         self.teacher_school = teacher_school
create_teacher()