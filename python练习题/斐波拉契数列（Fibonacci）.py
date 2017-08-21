#coding:utf-8
#Author:Mr Zhi
#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("干点别的事")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("号的啊")
print(f.__next__())
print(f.__next__())
print(f.__next__())
