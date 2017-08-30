#coding:utf-8
#Author:支文伟
import os,json
from log import get_logger
logger = get_logger() #日志模块实例化对象
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''数据库文件的绝对路径'''
shopping_data = base_dir + '/db/shopping_data'
shopping_car = base_dir + '/db/shopping_car'
creditcard_data = base_dir + '/db/creditcard_data'

'''购物商城'''
def mall():
    print("欢迎来到购物商城".center(30,'-'))
    product_list = []
    with open(shopping_data,'r',encoding='utf8') as f:
        for i in f:
            product_list.append(i.strip("\n").split(' ')) #拆分为列表并添加到product_list
    print(product_list)
mall()