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
    product_list = []
    product_list2 = []
    with open(shopping_data,'r',encoding='utf8') as f:
        for i in f:
            product_list.append(i.strip("\n").split(' ')) #拆分为列表并添加到product_list
    #print(product_list,len(product_list))
    def product_info():
        for index,item in enumerate(product_list):
            print(index +1,item[0],item[1])
        #product_info()
    while True:
        print("欢迎来到购物商城".center(30, '-'))
        product_info()
        choice_id = input("请输入商品编号：").strip()
        if choice_id.isdigit():
            choice_id = int(choice_id)
            if 0 <= choice_id <= len(product_list):

    else:
        print("没有对应的商品编号，请重新输入！")
mall()