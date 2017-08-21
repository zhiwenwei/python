#coding:utf-8
#Author:Mr Zhi
import time
def deco(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print("the func run time is %s" % (stop_time-start_time))
    return func
def test1():
    time.sleep(3)
    print("in the test1")
def test2():
    time.sleep(3)
    print("in the test2")
deco(test1),deco(test2) #改用调用函数方式
test1=deco(test1),test1() #这种方式必须使用retuan返回函数的内存地址
test2=deco(test2),test2()