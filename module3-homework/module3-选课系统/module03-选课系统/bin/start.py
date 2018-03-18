#-*- coding:utf-8 -*-
#Author:Kevin
import sys,os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) #添加环境变量
from core import main

if __name__ == '__main__':
    obj = main.Manage_center()
    obj.run()