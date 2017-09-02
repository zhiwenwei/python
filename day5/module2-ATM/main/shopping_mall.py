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
mall()