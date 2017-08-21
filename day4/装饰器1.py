#coding:utf-8
#Author:Mr Zhi
import time
def fun1():
    time.sleep(3)
    print("in the fun1")
def fun2(dan):
    start_time = time.time()
    dan() #run fun1
    stop_timre = time.time()
    print("fun1 run time... %s" % (stop_timre-start_time))
fun2(fun1) #测试fun1函数运行时间
#y源代码fun1的调用方式被改不符合装饰器定义

def test(func):
    print(func)
    return func
fun1 = test(fun1)
fun1()