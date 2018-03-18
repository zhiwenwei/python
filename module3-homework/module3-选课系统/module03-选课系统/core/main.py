#-*- coding:utf-8 -*-
#Author:Kevin
import os,sys
import pickle
import hashlib
import time
from conf import settings
'''创建基类（父类）'''
class Baseclass(object):
    def __init__(self):
        pass
    def uid(self):
        m = hashlib.md5()
        m.update(bytes(str(time.time()), encoding='utf-8'))
        return m.hexdigest()
    '''定义一个保存数据的方法'''
    def save(self,type,dict):  #type目录,dict内容
        filename = self.uid()
        dict['uid'] = filename
        abs_file = os.path.join(settings.BASE_DIR,type,filename) #拼接出文件的绝对路径
        with open(abs_file,'wb') as f:
            f.write(pickle.dumps(dict))
            if True:
                print("-----",type,"创建成功","-----")
                for key in dict:
                    print(key,dict[key])
    @staticmethod
    def get_all_db(self,type):
        all_data = []
        db_dir = os.path.join(settings.BASE_DIR,type)
        for i in os.listdir(db_dir): #序列目录下所有文件
            if os.path.isfile(os.path.join(db_dir,i)):
                db_file = os.path.join(db_dir,i)
                with open(db_file,"rb") as f:
                    file_dict = pickle.load(f) #如果目标文件含有__init__文件会报错
                    all_data.append(file_dict)
        return all_data
        #print(all_data)
'''学校类'''
class School(object):
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
'''教师类'''
class Teacher(object):
    def __init__(self,teacher_name,teacher_salary,teacher_school,teacher_class):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school
        self.teacher_class = []  #关联课程

'''班级类'''
class Classes(object):
    def __init__(self,classes_name,classes_course,classes_teacher):
        self.classes_name = classes_name
        self.classes_course = classes_course
        self.classes_teacher = classes_teacher

'''课程类'''
class Course(object):
    def __init__(self,course_name,course_period,course_price): #课程名，课程周期，课程价格
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price
'''学生类'''
class Student(object):
    def __init__(self,student_name,student_sex,student_class,student_school):
        self.student_name = student_name
        self.student_sex = student_sex
        self.student_class = student_class
        self.student_school = student_school


'''管理员'''
class Manage_admin(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)
        self.admin_view()
    def create_school(self): #创建学校
        school_dict = {}
        school_name = input("校名：").strip()
        school_addr = input("地址：").strip()
        school_name_list = []
        for obj in self.get_all_db(self,"school"):
            school_name_list.append((obj["校名"],obj["地址"]))
        if (school_name,school_addr) in school_name_list:
            print("校区已经存在")
        else:
            s1 = School(school_name,school_addr) #实例化
            school_dict["校名"] = s1.school_name
            school_dict["地址"] = s1.school_addr
            Baseclass.save(self,"school",school_dict) #永久保存数据到文件
    def create_teacher(self): #创建教师
        teacher_dict = {}
        school_name_list = []
        teacher_name_list =[]
        for obj in self.get_all_db(self,"teacher"):
            teacher_name_list.append((obj["姓名"]))
        for obj in self.get_all_db(self,"school"):
            school_name_list.append((obj["校名"]+obj["地址"]))
        teacher_name = input("教师姓名：")
        teacher_salary = input("教师工资：")
        print("已经存在的校区：", school_name_list)
        teacher_school = input("所属学校：")
        teacher_class = input("班级：")
        if teacher_school in school_name_list and teacher_name not in teacher_name_list: #判断是否名字或校名错误
            t1 = Teacher(teacher_name,teacher_salary,teacher_school,teacher_class) #实例化
            teacher_dict["姓名"] = t1.teacher_name
            teacher_dict["工资"] = t1.teacher_salary
            teacher_dict["所属学校"] = t1.teacher_school
            teacher_dict["班级"] = t1.teacher_class
            Baseclass.save(self,"teacher",teacher_dict)
        else:
            print("教师姓名重复或填入所属学校不存在")
    def create_classes(self):#创建班级
        classes_dict = {}
        classes_name_list = []
        for obj in self.get_all_db(self,"classes"):
            classes_name_list.append((obj["班级名"]))
        classes_name = input("班级名：")
        classes_course = input("关联课程：")
        classes_teacher = input("负责讲师：")
        if classes_name in classes_name_list:
            print("该班级已经存在")
        else:
            cs1 = Classes(classes_name,classes_course,classes_teacher) #实例化
            classes_dict["班级名"] = cs1.classes_name
            classes_dict["关联课程"] = cs1.classes_course
            classes_dict["负责讲师"] = cs1.classes_teacher
            Baseclass.save(self,"classes",classes_dict)
    def create_course(self):  #创建课程
        course_dict = {}
        course_name_list = []
        for obj in self.get_all_db(self,"course"):
            course_name_list.append((obj["课程名"]))
        course_name = input("课程名：")
        course_period = input("课程周期：")
        course_price = input("课程价格：")
        if course_name in course_name_list:
            print("该课程已经存在")
        else:
            c1 = Course(course_name,course_period,course_price) #实例化
            course_dict["课程名"] = c1.course_name
            course_dict["课程周期"] = c1.course_period
            course_dict["课程价格"] = c1.course_price
            Baseclass.save(self,"course",course_dict)
    def admin_view(self):
        while True:
            menu = '''
            欢迎来到管理员视图
            1.创建学校
            2.创建讲师
            3.创建班级
            4.创建课程
            '''
            menu_dict = {
                '1':self.create_school,
                '2':self.create_teacher,
                '3':self.create_classes,
                '4':self.create_course,
                'q':exit
            }
            print(menu)
            user_choice = input("请选择(f返回q退出):")
            if user_choice in menu_dict.keys():
                menu_dict[user_choice]()
            elif user_choice == 'f':
                break
            else:
                print("输入有误")

'''学员管理'''
class Manage_student(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)
        self.student_view()
    def student_regist(self):  #学员注册
        student_dict = {}
        student_name_list = []
        student_school_list = []
        for obj in self.get_all_db(self,"student"):
            student_name_list.append((obj["姓名"]))
        for obj in self.get_all_db(self, "school"):
            student_school_list.append((obj["校名"] + obj["地址"]))
        student_name = input("注册姓名：")
        student_sex = input("性别：")
        student_class = input("班级：")
        print("已经存在校区：",student_school_list,student_name_list)
        student_school = input("学校：")
        if student_name not in student_name_list and student_school in student_school_list:
            s1 = Student(student_name,student_sex,student_class,student_school)#实例化
            student_dict["姓名"] = student_name
            student_dict["性别"] = student_sex
            student_dict["班级"] = student_class
            student_dict["学校"] = student_school
            Baseclass.save(self,"student",student_dict)
        else:
            print("该姓名已经注册或校区名字有误")
    '''查看校区'''
    def show_school(self):
        school_list =[]
        for obj in self.get_all_db(self,"school"):
            school_list.append((obj["校名"] + obj["地址"]))
        for i in school_list:
            print(i)

    def student_view(self):
        '''学生视图'''
        while True:
            menu = '''
            欢迎来到学生视图
            1.学员注册
            2.查看学校
            3.返回
            '''
            print(menu)
            user_choice = input("请输入你的选择：")
            menu_dict ={
                '1':self.student_regist,
                '2':self.show_school
            }
            if user_choice in menu_dict.keys():
                menu_dict[user_choice]()
            elif user_choice == "3":
                break
            else:
                print("你输入有误")

class Manage_teacher(Baseclass):
    def __init__(self):
        Baseclass.__init__(self)
        self.teacher_view()
    def show_class(self): #查看班级学生名单
        class_student_list = []
        for obj in self.get_all_db(self,"classes"):
            class_student_list.append((obj["班级名"],obj["关联课程"],obj["负责讲师"]))
        for i in class_student_list:
            print("班级名:",i[0],"关联课程：",i[1],"负责讲师：",i[2])

    def teacher_view(self):
        while True:
            menu = '''
            欢迎来到讲师视图
            1.查看班级
            2.返回
            '''
            menu_dict = {
                '1':self.show_class,
            }
            print(menu)
            user_choice = input("请选择：")
            if user_choice in menu_dict.keys():
                menu_dict[user_choice]()
            elif user_choice == '2':
                break
            else:
                print("你输入有误")

class Manage_center(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            print("\n欢迎进入选课系统\n"
                  "1 学生视图\n"
                  "2 教师视图\n"
                  "3 学校视图\n"
                  "q 退出学员管理系统\n")
            user_choice = input("\033[34;0m请输入您要登录的视图:\033[0m")
            if user_choice == '1':
                Manage_student()
            elif user_choice == '2':
                Manage_teacher()
            elif user_choice == '3':
                Manage_admin()
            elif user_choice == 'q':
                print("\033[34;1m感谢使用学员管理系统,退出\033[0m")
                break
            else:
                print("\033[31;1m请输入正确的选项\033[0m")
