#-*- coding:utf-8 -*-
#Author:ZhiWenwei
from multiprocessing import Process,Queue
def f(q):
    q.put([10000,None,'hello!!!!'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()