#coding:utf-8
#Author:zhiwenwei
# coding=utf-8

''''' 
习题一： 
1.1用time模块获取当前的时间戳. 
1.2用datetime获取当前的日期，例如:2013-03-29 
1.3用datetime返回一个月前的日期，比如今天是2013-3-29一个月前的话2013-02-27 
'''

import time

print
'当前时间戳:', time.time()

import datetime

print
'当前日期：', datetime.date.today()

print
datetime.date.today() - datetime.timedelta(days=30)

''''' 
习题二： 
1 用os模块的方法完成ping www.baidu.com操作。 
2 定义一个函数kouzhang(dirpwd),用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件 
不重复的扩展名，如果有两个'.py'的扩张名，则返回一个'.py' 
'''
import os

# os.system('ping www.baidu.com')

kz = []


def kuozhan(dirpwd):
    if not os.path.exists(dirpwd):
        return dirpwd, 'is not found!'
    for i in os.listdir(dirpwd):
        kz.append(os.path.splitext(dirpwd + i)[-1])
    print
    list(set(kz))


kuozhan('C:\Users\Administrator\Desktop\py\scripts\scripts')

''''' 
习题三： 
定义一个函数xulie(dirname,info)参数:dirname-路径名，info-需要序列化的数据，功能： 
将info数据序列化存储到dirname路径下随机的文件里 
'''
import pickle, random


def xulie(dirname, info):
    if not os.path.exists(dirname):
        return 'Not found!'
    a = pickle.dumps(info)
    filename = ''
    for i in range(10):
        filename = filename + random.choice('abcedfghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890')
    filepath = os.path.join(dirname, filename)
    f = open(filepath, 'a+')
    f.write(a)
    f.close()


a = [1, 2, 3, 4, 5, 6, 7]
xulie('C:\Users\Administrator\Desktop', a)