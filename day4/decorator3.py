#coding:utf-8
#Author:Mr Zhi
#嵌套函数
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()
#foo()
import time
def timer(func): #嵌套函数，
    def deco():
        start_time=time.time()
        func() #run test1
        stop_time=time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return deco
        #return func
@timer #等于test1=timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")
    #return test1
@timer
def test2():
    time.sleep(1)
    print("in the test2")
#print(timer(test1))
#test1=timer(test1)
test1()
test2()