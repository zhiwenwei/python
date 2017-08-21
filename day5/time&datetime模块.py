#coding:utf-8
#Author:Mr Zhi
import time
"""
time模块时间表示的格式主要有三种：
a.timestamp时间戳，时间戳表示的是从1970-1-1日00:00:00按秒计算的偏移量
b.struct_time时间组，共有九个元素
c.format time格式化时间，已格式化的结构使时间更具可读性，包括自定义格式和固定格式
"""
#主要time生成方法和time格式转换方法实例：
import time
#生成时间戳timestamp
print(time.time())
print(time.mktime(time.localtime()))

#生成struct_time本地时间
print(time.localtime())
print(time.localtime(time.time()))

#格林威治时间
print(time.gmtime())
print(time.gmtime(time.time()))

#生成format time
print(time.strftime("%Y-%m-%d %X")) # %X本地相应时间
print(time.strftime("%y-%m-%d %X",time.localtime()))

#生成固定格式的时间表示格式
print(time.asctime(time.localtime()))
print(time.ctime(time.time()))

"""
datetime模块重新封装了time模块，相当于date和time的结合
"""
import datetime
print(datetime.datetime.now()) #获取当前时间
print(datetime.datetime.now() + datetime.timedelta(3)) #获取三天后的时间
print(datetime.datetime.now() + datetime.timedelta(hours=-3)) #获取下个小时以前的时间
print(datetime.datetime.now() + datetime.timedelta(minutes=30,hours=3)) #获取三个半小时后的时间
