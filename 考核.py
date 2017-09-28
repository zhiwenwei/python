# #coding:utf-8
# #Author:Mr Zhi
# #使用while循环实现输出1 - 2 + 3 - 4 + 5 ... - 100 的和
# #偶数和减去奇数和就可以得出答案sum =0
# for i in range(1,100,2):
#     sum += i * (i+1)
# print(sum)
# # #coding:utf-生成器8
# # # from json import dumps
# # # import json
# #()
# import random
# a = ''
# for i in range(6):
#     s = random.randint(0,9)
#     a += str(s)
# print(a)
# sum =0
# for i in range(1,100,2):
#     sum += i * (i+1)
# print(sum)
#将时间戳转化为localtime
#python3 起，filter 函数返回的对象从列表改为 filter object（迭代器）,filter(function or None, iterable) --> filter object
#获取数字100以内的奇数
def even_num(n):
    return n % 2 ==1
res = filter(even_num,(i for i in range(10)))
for i in res:
    print(i)
# 利用 filter、自定义函数 获取l1中元素大于33的所有元素 l1 = [11, 22, 33, 44, 55]
ll = [11, 22, 33, 44, 55]
def ll_fil(x):
    return x > 33
for i in filter(ll_fil,ll):
    print(i)
#利用 filter、lambda表达式 获取l1中元素小于33的所有元素 l1 = [11, 22, 33, 44, 55]
ll = [11, 22, 33, 44, 55]
res = filter(lambda x:x<33,ll)
for i in res:
    print(i)
g = lambda x:x**2
print(g(4))
r1 = eval("1 + 10 * 10")
r2 = exec("1 + 10 * 10")
print(r1, r2)
#写一个函数判断列表中是否有重复元素，如果有返回true，否则返回false
a = [1,2,3,4]
print([True,False][a==list(set(a))])
import json
l1 = ["alex", 123, "eric"]
l2 = ["alex", 123, 'eric']
s1 = """ ["alex", 123, "eric"] """
s2 = """ ["alex", 123, 'eric'] """
# json.loads(l1)
# json.loads(l2)
# json.loads(s1)
# json.loads(s2)
json.dumps(l1)
json.dumps(l2)
json.dumps(s1)
json.dumps(s2)
"""如有一下两个函数，请书写一个装饰器实现在不改变函数调用者的代码基础上，实现在函数执行前后分别打印"before" 和 "after"。
        def f1(arg):
            return arg + 1
        def f2(arg1, arg2):
            return arg1 + arg2"""
def before(func):
    def wrap(*args,**kwargs):
        if func.__name__ == "f1":
            print("before")
        else:
            print("alter")
        func(*args, **kwargs)
    return wrap
@before
def f1(arg):
    # print(arg+1)
    return arg + 1
@before
def f2(arg1, arg2):
    # print(arg1+arg2)
    return arg1 + arg2

f1(100)
f2(56,2)
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
str = json.dumps(data)
print(type(str),str)
json = json.loads(str)
print(type(json),json)
s1 = """ ["alex", 123, "eric"] """
s1_josn = json.loads(s1)
print(s1_josn)

