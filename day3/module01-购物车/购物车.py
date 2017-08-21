#coding:utf-8
#Author:Mr Zhi
file_open = open('购物车用户信息','r+',encoding="utf-8")  #购物车用户信息文件保存着用户名密码和余额
f = str(file_open.read())
for line in f:
     file_str = str(f)
file_open_dict = eval(file_str) #转换成字典(文件内容原先是字典)
username = input("输入用户名：")
password = input("输入密码:")
while True:
    if username in file_open_dict:  #判断用户名是否在购物车用户信息文件中
        if password in file_open_dict[username]:
            salary = int(file_open_dict[username][password])
            print('''\033[32;1m欢迎登录，当前余额为%s\033[0m''' % salary)
            break
        else:
            password = input("密码错误，请重新输入密码")
            continue
    else:
        password_salary = {} #定义密码，工资空字典
        salary_str = input("欢迎第一次登陆，请输入工资：")
        salary =float(salary_str) #输入的工资转成数字
        password_salary[password] = salary  #密码与数字对应
        file_open_dict[username] = password_salary  #用户名和密码工资对应
        file_open.seek(0)  #文件读取到开头
        file_open.write(str(file_open_dict)) #把用户名密码和工资写到文件中
        file_open.tell()   #返回当前位置
        break
product_list = [   #购物清单
    ['iphone6', 5000],
    ['bike', 800],
    ['python books', 200],
    ['bag', 300],
    ['macbook pro', 9000],
]
history_f = open('history','r+',encoding="utf-8")  #打开history文件
f2 = str(history_f.read())
for line in f2:
     file_str2 = str(f2)
history_line = eval(file_str2)
if username not in history_line:
    history_line[username] = []
shoppinglist = history_line[username]
shoppinglist_new = []
choice = input ("\033[35;1m是否需要查询历史购物记录（y/n）\033[0m") #询问是否查询历史记录
if choice == "y" or choice =="Y":
    print("---历史购物记录---")
    print(shoppinglist)
while True:
    print("---商品清单---")
    for index,item in enumerate(product_list): #对元组进行遍历并加上索引
        print(index,item) #输出商品
    choice = input("输入商品编码：")
    #choice = int(choice)
    if choice.isdigit():
        choice = int(choice)
        if choice < len(product_list) and choice >= 0:
            p_item = product_list[int(choice)] #把商品赋值给p_item
            print(p_item)
            if p_item[1] <= salary: #判断商品价格和工资的大小
                shoppinglist_new.append(p_item) #把商品加到元组
                salary -= p_item[1] #余额 = 工资 - 商品
                print("\033[37;1m买了 %s 还剩下 %s 元\033[0m" % (p_item, salary))
            else:
                print("你的余额不足")
        else:
            print("你选择的编码%无效" % choice)
    elif choice == "q" or choice =="Q":
        file_open_dict[username][password] = salary #工资给对应的用户密码位置
        file_open.seek(0)
        file_open.write(str(file_open_dict)) #把余额写到购物车用户信息文件中
        file_open.tell()
        print("----已购商品清单----")
        print(shoppinglist_new)  # 打印清单
        print("\033[31;1m你的余额：%s\033[0m" % salary)  # 打印余额
        shoppinglist.extend(shoppinglist_new)  # 本次购物记录追加到购物列表中
        history_line[username] = shoppinglist  # 购物列表和用户名对应
        history_f.seek(0) #移动文件读取指针到开头
        history_f.write(str(history_line))  # 购物记录写入文件
        history_f.tell() #返回文件的当前位置
        break
    else:
        print("你选择的编码%无效" % choice)