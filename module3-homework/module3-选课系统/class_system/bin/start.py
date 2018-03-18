#-*- coding:utf-8 -*-
#Author:Kevin
import os
import sys
import platform
'''添加环境变量'''
if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
sys.path.insert(0,BASE_DIR)
print(BASE_DIR)
from core import main
from conf import settings
if __name__ == '__main__':
    obj = main.Manage_center()
    obj.run()
