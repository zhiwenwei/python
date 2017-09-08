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
        choice_id = input("请输入商品编号（q返回）：").strip()
        if choice_id.isdigit():
            choice_id = int(choice_id)
            if 0 <= choice_id <= len(product_list):
                product_item = product_list[choice_id-1] #获取选择的商店
                print("商品 %s 加入购物车，价格 %s " % (product_item[0],product_item[1]))
                product_list2.append(product_item)
                '''购物信息记录到日志模块'''
                shopping_info = ["购物",str(product_item[0]),"价格",product_item[1]]
                shopping_info = "---".join(shopping_info)
                logger.debug(shopping_info)
            else:
                print("没有对应的商品编号，请重新输入！")
        elif choice_id == 'q':
            with open(shopping_car,'r+',encoding='utf-8') as f:
                list = json.loads(f.read())
                list.extend(product_list2)
                f.seek(0)
                #f.truncate(0)
                list = json.dumps(list)
                f.write(list)
                f.flush()
                break
                # f.flush()
        else:
            print("没有对应的商品编号，请重新输入！")
#mall()
'''清空购物车'''
def del_shoppingcar():
    while True:
        choice = input("是否清空购物车？('y'确认'q'退出)：").strip()
        if choice == 'q':break
        if choice == 'y':
            with open(shopping_car,"r+",encoding='utf-8') as f:
                res = json.loads(f.read())
                print(type(res))
                if res != []:
                    f.seek(0)
                    f.truncate(0)  #截断后面所有的字符也就是清空
                    list = json.dumps([])
                    f.write(list)
                    f.flush()
                    print("购物车已经清空！")
                else:
                    print("你还没有消费，购物车为空！")
        else:
            print("你输入指令有误！")
            break
def shopping_pay():
    while True:
        print("购物结算".center(50,'-'))
        with open(shopping_car,'r+',encoding='utf-8') as f:
            data = json.loads(f.read())
            if data != []:
                print("\t商品\t价格")
                for index,item in enumerate(data):
                    print(index +1,item[0],item[1])
                money = sum([int(i[1]) for i in data])
            else:
                print("你还没消费，快去花钱吧！")
                break
        choice = input("商品总额：%s (y)确认支付,(q)返回：" %(money))
        if choice == 'q':break
        if choice == 'y':
            creditcard_id = input("请输入结算的信用卡账号：").strip()
            with open(creditcard_data,'r+',encoding='utf-8') as f2:
                _creditcard_data  = json.loads(f2.read())
                if creditcard_id in _creditcard_data.keys():
                    passwd = input("请输入信用卡 %s 支付密码：" % (_creditcard_data[creditcard_id]["credictcard"])).strip()
                    if int(passwd) == _creditcard_data[creditcard_id]["password"]:
                        limit = _creditcard_data[creditcard_id]["limit"]
                        limitcash = _creditcard_data[creditcard_id]["limitcash"]
                        if _creditcard_data[creditcard_id]["limit"] >= money:
                            _creditcard_data[creditcard_id]["limit"] -= money
                            _creditcard_data[creditcard_id]["limitcash"] -= money
                            _creditcard_data[creditcard_id]["totalbill"] += money #账单
                            '''写入日志'''
                            shopping_info = [creditcard_id,"信用卡商城结账",str(money)+"¥"]
                            shopping_info = '--'.join(shopping_info)
                            logger.debug(shopping_info)
                            '''写入数据'''
                            dict = json.dumps(_creditcard_data)
                            f2.seek(0)
                            f2.truncate(0)
                            f2.write(dict)
                            print("支付成功：%s¥"%(money))
                            break
                        else:
                            print("当前信用卡额度%s不足支付！"%(limit))
                    else:
                        print("密码有误，请重新输入！")
                else:
                    print("你输入的信用卡不存在！")
