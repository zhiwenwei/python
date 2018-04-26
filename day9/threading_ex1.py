#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import threading
import time
def run(n):  #定义每个线程要运行的函数
    print("task",n)
    time.sleep(3)
    print("task done",n)
start_time = time.time()
#多线程并发：速度快
# t1 = threading.Thread(target=run,args=("t1",)) #生成一个线程实例
# t2 = threading.Thread(target=run,args=("t2",))  #生成另一个线程实例
# t1.start() #启动线程
# t2.start() #启动另一个线程
# #单线程：速度慢
# run("t1")
# run("t2")

#主线程和子线程是并行的，不是串行，两者互不影响
t_list = []
for i in range(50):
    t = threading.Thread(target=run, args=("%s"%i,))
    t.start()
    t_list.append(t)
    # t1.join() #=wait(),相当于变成串行
for i in t_list:
    t.join()
print("---all threads has finished---")
print("cost",time.time() - start_time)