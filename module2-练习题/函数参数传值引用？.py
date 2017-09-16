#coding:utf-8
#Author:zhiwenwei
from ctypes import *
import os.path
import sys
def test(c):
    print("test before")
    print(id(c))
    c +=2
    print(c)
    print("test after +")
    print(id(c))
    return c
# def printit(t):
#     for i in range(len(t)):
#         print(t[i])
# if __name__ == "__main__":
#     a = 2
#     print("test1")
#     print(id(a))
#     n= test(a)
#     print("test2")
#     print(a)
#     print(id(a))
# def test1(l1):
#     l1 = [12,89]
#     return l1
# def test2():
#     l2 = [123,897]
#     print(test1(l2))
#     print(l2)
# test2()
# def test3(val):
#     val.append(100)
#     # val = ['x','y','z']
#     print(id(val))
#     return val
# l = [1,10]
# print(test3(l))
# l.append(1000)
# print(l)
# print(id(l))
# def test(c):
#     c.append("hello world")
#     print(c,id(c))
#     return
# list = [1,2]
# test(list)
# print(list,id(list))

# def test2(str):
#     str = "i am test!!!"
#     print(str,id(str))
#     return
# str = "hello word"
# test2(str)
# print(str,id(str))

def test2(p):
    p = "i in test2"
    print(p,id(p))
str = "hello word"
test2(str)
print(str,id(str))

