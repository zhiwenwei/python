#coding:utf-8
#Author:Mr Zhi
import os
print(__file__) #返回相对路径
print(os.path.abspath(__file__)) #返回绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #返回当前文件所在目录名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #返回上一级目录名
