# #coding:utf-8
# #Author:Mr Zhi
# #使用while循环实现输出1 - 2 + 3 - 4 + 5 ... - 100 的和
# #偶数和减去奇数和就可以得出答案
# #coding:utf-8
# # from json import dumps
# # import json
# # data = {'name':'JieSen','height':175,'weight':'68KG'}
# # #dumps到字串
# # json_str = json.dumps(data)
# # print('dumps到字符串:',json_str,'类型:',type(json_str))
# # #loads回来
# # json_dict = json.loads(json_str)
# # print('loads回来:',json_dict,'类型:',type(json_dict))
# # import datetime,json
# # print(json.dumps(str(datetime.datetime.now())))
import datetime
def func_name(is_show=True):#定义一个带有参数的装饰函数
    def wrap(func):#包装函数，接受一个函数对象作为参数
        def inner_wrap(*args,**kwargs):
            if is_show:
                print("Function name:%s"%(func.__name__))
            return func(*args,**kwargs)
        return inner_wrap
    return wrap
@func_name(True)      #等于 func_time = func_name(func_time)
def func_time1():
    print(datetime.datetime.now())
@func_name(False)
def func_time2():
    print(datetime.datetime.now())
func_time1()
func_time2()
#
# 总结
# 1.定义一个装饰器函数，此函数会接受函数对象作为输入参数，以确保能执行其功能
# 2.在装饰器函数内定义一个和目标函数参数列表一致的包装函数，返回值（包装函数），同时添加欲追加的工作量（甚至彻底替换掉目标函数）
# 3.装饰器函数返回值设置为包装函数
# 4.把目标函数对象传递给装饰器函数去执行，返回值（包装函数）赋值到目标函数名上，最后以目标函数之名调用包装函数
# from datetime import datetime as dt
# def log(is_show=True):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             if is_show:
#                 print('['+str(dt.now())+']'+func.__name__)
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return wrapper
# # 默认显示日志
# @log(True)
# def func1():
#     print("func1")
# # 默认不显示日志
# @log(False)
# def func2():
#     print("func2")
# func2()
# func1()
'''带参数的装饰器'''
