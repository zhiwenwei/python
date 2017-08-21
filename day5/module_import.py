#coding:utf-8
#Author:Mr Zhi
# import zww
# print(zww.name)
# zww.say_hello()
# zww.test1()
# import sys
# print(sys.path)


#导入不同目录的模块
import sys,os
print(sys.path)
print(os.path.abspath(__file__))  #获取当前文件绝对路径
print(os.path.dirname(__file__))  #获取当前文件所在目录
print(os.path.dirname(os.path.abspath(__file__)))
a = os.path.dirname(os.path.abspath(__file__))
sys.path.append(a)  #把当前目录加入到python的搜索模块的路径（list）集
from zww import test1 as f
f()

from  zww import test1
test1()

import package_test

