#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import threading
import time
event = threading.Event()
def lighter():
    count = 1
    event.set() #先设置绿灯
    while True:
        if 5 < count <=10:#改成红灯
            event.clear() #清标志位
            print("\033[41;1mred light is on...\033[0m")
        elif count > 10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on...\033[0m")
        time.sleep(1)
        count +=1
def car(name):
    while True:
        if event.is_set(): #判断，True代表绿灯
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print(" [%s]sees red light,waiting..."%name)
            event.wait()
            print("\033[34;1m[%s]green light is on start going....\033[34;0m")
light = threading.Thread(target=lighter,)
light.start()
car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()