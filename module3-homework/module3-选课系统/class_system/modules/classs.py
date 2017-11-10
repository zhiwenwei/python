#-*- coding:utf-8 -*-
#Author:Kevin
class Class(object):
    '''班级类，包含名称课程学生'''
    def __init__(self,class_name,course_obj):
        self.class_name = class_name
        self.class_course = course_obj
        self.class_student = {} #学生字典