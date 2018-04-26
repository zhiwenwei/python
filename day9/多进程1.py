#-*- coding:utf-8 -*-
#Author:ZhiWenwei
# from multiprocessing import Process
import multiprocessing
import threading
import time,os
def func_f(name):
    time.sleep(2)
    print('hello',name,os.getpid())

def thread_run():
    print("the id thread",threading.get_ident())
if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=func_f,args=('zww %s'%i,)) #启动十个进程
        p.start()
    t = threading.Thread(target=thread_run,) #线程
    t.start()
    #p.join()
