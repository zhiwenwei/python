#coding:utf-8
#Author:Mr Zhi
"""购物车程序：

1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表

2、允许用户根据商品编号购买商品

3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒 

4、可随时退出，退出时，打印已购买商品和余额

5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买

7、允许查询之前的消费记录"""
product_list = [
    ('iphone6', 5000),
    ('bike', 800),
    ('python books', 200),
    ('bag', 300),
    ('macbook pro', 9000),
]
User_info_file = open("User_info",'r',encoding="utf-8")     #打开用户信息文件,用来验证用户和密码是否正确
shopping_record_file = open('shopping_record',"r+",encoding="utf-8")#打开购物记录文件，验证用户是否第一次登陆
shopping_record_line = record_file.read()  #读取购物记录文件
User_info_line = eval(User_info_file.read()) #转换成字典

username = input("请输入你的用户名：")
password = input("请输入你的密码：")
if username in User_info_line.keys() and password == User_info_line["{user}".format(user=username)] and username not in shopping_record_line():
    salary = input("请输入你的工资：")
    if salary.isdigit():
        salary = int(salary)
    while True:
            for index,item in enumerate(product_list):
                print(index,item)
            choice = input("你要买什么？>>>")
            if choice.isdigit():
                choice = int(choice)
                if choice < len(product_list) and choice >=0:
                    p_item = product_list[choice]
                    print(p_item)
                    print(type(p_item))
                    if p_item[1] <= salary:
                        shopping_list.append(p_item)
                        salary -= p_item[1]
                        print("买了 %s 还剩下 %s 元" % (p_item,salary))
                    else:
                        print("你的余额不足")
                else:
                    print("你选择的编码%无效" %choice)
            elif choice == "q":
                record_file.write('你的账户{user}余额:'.format(user=username)+str(salary)+'\n') #把账户和余额写入购物清单
                record_file.write('你的购物单:'.format(user=username) + str(shopping_list) + '\n') #把购物单写入购物清单
                print("------shopping list-----")
                print(shopping_record_line)
                record_file.close()
                exit()
            elif username in shopping_record_line:
                continue
            else:
                print("你的输入无效")
else:
    print("用户或密码出错")






