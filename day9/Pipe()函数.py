#-*- coding:utf-8 -*-
#Author:ZhiWenwei
from multiprocessing import Process,Pipe
def f(conn):
     conn.send([9000,None,'I am fine!'])
if __name__ == '__main__':
    parent_conn,child_cpnn = Pipe()
    p = Process(target=f,args=(child_cpnn,))
    p.start()
    print(parent_conn.recv())
    p.join()