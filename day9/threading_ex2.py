#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import threading
import time
class MyThread(threading.Thread): #继承父类threading.Thread
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num = num

    def run(self):#把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("running on number:%s" %self.num)
        time.sleep(3)
if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    # t1.join() #=wait()
    t2.start()
