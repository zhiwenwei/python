#coding:utf-8
#Author:Mr Zhi
def foo(): #嵌套函数
    print("in the foo")
    def bar():
        print("in the bar")
    bar() #应用函数
foo()

#高阶函数
def test1(f):
    print("in the test1")
def func():
    print("in the func")
test1(func())
