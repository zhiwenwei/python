#-*- coding:utf-8 -*-
#Author:Kevin
import os
import sys
import platform
'''定义数据库路径'''
if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
    database_path = os.path.join(BASE_DIR,"database")
    print(database_path)
else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
    database_path = os.path.join(BASE_DIR, "database")

school_db_file = os.path.join(database_path,"school")