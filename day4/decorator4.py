#coding:utf-8
#Author:Mr Zhi
#coding:utf-8
#Author:Mr Zhi
import time
def timer(func): #嵌套函数，
    def deco(*args,**kwargs): #传递多个参数
        start_time=time.time()
        func(*args,**kwargs) #run test1
        stop_time=time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return deco
@timer
def test2(name,age):
    time.sleep(1)
    print("in the test2",name,age)
test2("zyx","two")