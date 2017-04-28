#!/usr/bin env python3
# -*- coding: utf-8 -*-
'''
程序：购物车程序
需求：
     1.启动程序后，让用户输入工资，然后打印呢商品列表
     2.允许用户根据商品编号购买商品
     3.用户选择商品后，检测余额是否足够，够就直接扣款，不够就提醒
     4.可随时退出，退出时，打印购买的商品和余额
'''
import sys,os
product_list = [
    ('iphone7',6000),
    ('book',150),
    ('bike', 1000),
    ('bag', 300),
]
shopping_list = []
with open('shopping_file.txt','w',encoding='utf-8') as f:
    for i in str(product_list):
        f.write(i)
    f.close()
salary = input("input you salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("要买什么？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("买了 %s ,余额 %s" % (p_item,salary))
                else:
                    print("你的余额 %s ,买个毛线" %salary)
            else:
                print("你输入的编号 %s 无效" %user_choice)
        elif user_choice == 'q':
            print("---------shoppong list------------")
            for p in shopping_list:
                print(p)
            exit()
        else:
            print("invalid option")


