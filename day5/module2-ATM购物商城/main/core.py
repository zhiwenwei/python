#coding:utf-8
#Author:zhiwenwei
import os,sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# core_path = base_dir + 'main'
# sys.path.insert(0,core_path)
from admin import *
from credictcard import *
from shopping_mall import *
'''主页面列表'''
def core_list():
    list = ["  ATM  ",
            "购物商城",
            "后台管理",
            "退出程序"]
    index = 0
    for i in list:
        print(index+1,i)
        index +=1

'''ATM页面列表'''
def atm_list():
    list = ["信用卡信息",
            "信用卡转账",
            "信用卡取现",
            "信用卡还款",
            ]
    index = 0
    for i in list:
        print(index+1,i)
        index += 1
'''后台管理列表'''
def admin_list():
    list = [" 申请信用卡 ",
            "添加管理员账户",
            "修改信用卡密码"
            ]
    index = 0
    for i in list:
        print(index +1,i)
        index += 1
'''购物商城列表'''
def shopping_list():
    list = ["购物商城",
            "购物结算",
            "清空购物车",
            "查看购物车"
            ]
    index = 0
    for i in list:
        print(index+1,i)
        index += 1

'''主函数'''
def core():
    print("欢迎来到购物商城ATM系统".center(30,'-'))
    while True:
        core_list()
        choice = input("请选择ID：").strip()
        if choice == "q":
            print("已退出，欢迎下次使用！".center(40,'-'))
            exit()
        if choice.isdigit():
            choice = int(choice)
            if  1 <= choice <= 4:
                while True:
                    if choice == 1:
                        print("欢迎来到信用中心".center(40,'-'))
                        atm_list()
                        atm_choice = input("请选择ATM操作id：").strip()
                        if atm_choice == "q":break
                        if atm_choice == "exit":exit("已退出程序，欢迎下次使用！")
                        if atm_choice.isdigit():
                            atm_choice = int(atm_choice)
                            if 1 <= atm_choice <= 4:
                                while True:
                                    if atm_choice == 1:
                                        creditcard_info()
                                        break
                                    elif atm_choice == 2:
                                        transfer()
                                        break
                                    elif atm_choice == 3:
                                        takecash()
                                        break
                                    elif atm_choice == 4:
                                        repayment()
                                        break
                            else:
                                print("请输入正确的id")
                    elif choice ==2:
                        print("欢迎来到购物商城".center(40,'-'))
                        shopping_list()
                        shop_choice = input("请选择id：").strip()
                        if shop_choice == "q":break
                        if shop_choice == "exit":exit("已退出程序，欢迎下次使用！")
                        if shop_choice.isdigit():
                            shop_choice = int(shop_choice)
                            if 1 <= shop_choice <= 4:
                                while True:
                                    if shop_choice == 1:
                                        mall()
                                        break
                                    elif shop_choice == 2:
                                        shopping_pay()
                                        break
                                    elif shop_choice == 3:
                                        del_shoppingcar()
                                        break
                                    elif shop_choice == 4:
                                        search_shopppingcar()
                                        break
                            else:
                                print("请输入正确的id")
                        else:
                            print("请输入正确的id")
                    elif choice == 3:
                        print("欢迎来到管理后台中心".center(50,'-'))
                        admin_list()
                        admin_choice = input("请选择id(q返回exit退出)").strip()
                        if admin_choice == "q":break
                        if admin_choice == "exit":exit("已退出程序，欢迎下次使用！")
                        if admin_choice.isdigit():
                            admin_choice = int(admin_choice)
                            if 1 <= admin_choice <= 3:
                                while True:
                                    if admin_choice == 1:
                                        apply()
                                        break
                                    elif admin_choice == 2:
                                        alter_admin()
                                        break
                                    elif admin_choice == 3:
                                        alter_pw()
                                        break
                            else:
                                print("请输入正确的id")
                    elif choice == 4:
                        exit("已退出程序，欢迎下次使用！")
            else:
                print("请输入正确的id")
        else:
            print("你输入有误！")