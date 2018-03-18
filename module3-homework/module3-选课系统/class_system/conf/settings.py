#-*- coding:utf-8 -*-
#Author:Kevin
import os
import sys
import platform
'''定义数据库路径'''
if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
    database_path = os.path.join(BASE_DIR,"database")
else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
    database_path = os.path.join(BASE_DIR, "database")

school_db_file = os.path.join(database_path,"school")
STUDENTDB_PATH=r'F:\python文件\选课系统\db\student'
TEACHERDB_PATH=r'F:\python文件\选课系统\db\teacher'
COURSE_PATH=r'F:\python文件\选课系统\db\course'
SCHOOL_PATH=r'F:\python文件\选课系统\db\school'
CLASS_PATH=r'F:\python文件\选课系统\db\class'
