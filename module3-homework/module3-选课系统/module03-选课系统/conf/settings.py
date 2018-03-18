#-*- coding:utf-8 -*-
#Author:Kevin
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'db') #获取上一级的绝对目录
ADMIN_DB = os.path.join(BASE_DIR,'admin')
SCHOOL_DB = os.path.join(BASE_DIR,'school')
CLASSES_DB = os.path.join(BASE_DIR,'classes')
COURSE_DB = os.path.join(BASE_DIR,'course')
TEACHER_DB = os.path.join(BASE_DIR,'teacher')
STUDENT_DB = os.path.join(BASE_DIR,'student')
COURSE_TO_TEACHER = os.path.join(BASE_DIR,'course_to_teacher')




