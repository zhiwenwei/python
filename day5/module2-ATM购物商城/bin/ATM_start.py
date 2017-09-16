#coding:utf-8
#Author:支文伟
'''执行ATM程序'''
import os,sys
core_path  = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/main'
sys.path.append(core_path)  #把该路径加到环境变量
from core import *
if __name__ == '__main__':
    core()
