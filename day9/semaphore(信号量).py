#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import threading,time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread:%s"%n)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)
    for i in range(1,5):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("---all threads done")
    print(num)