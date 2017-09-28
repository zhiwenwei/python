#coding:utf-8
#Author:zhiwenwei
'''写代码实现：1*2+3*4+5*6+7*8...+99*100这个结果的和：使用循环或函数
'''
sum=0
for i in range(1,100,2):
    sum += i*(i+1)
print(sum)
''' 如有一下两个函数，请书写一个装饰器实现在不改变函数调用者的代码基础上，实现在函数执行前后分别打印"before" 和 "after"。

        def f1(arg):
            return arg + 1

        def f2(arg1, arg2):
            return arg1 + arg2
'''
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
    return arg + 1
@before
def f2(arg1, arg2):
    return arg1 + arg2
f1(100)
f2(56,2)

#书写代码，创建6位的随机验证码（含数字和字母）
import random
a = ''
for i in range(6):
    curr = random.randrange(0,6)
    if curr == i:
        e = chr(random.randint(97,122))
    else:
        e = random.randrange(0,9)
    a += str(e)
print(a)
