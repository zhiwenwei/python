#coding:utf-8
#Author:ZhiWenwei
import os
import time
import shutil
staff_table_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'/db/staff_table'  #获取员工信息文件绝对路径
print(staff_table_path)
backup_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/backup/'  #备份路径
'''定义一个能备份文件的装饰器，在修改原文件前先进行备份'''
def bakcup(func):
    def bk(*args,**kwargs):
        shutil.copy(staff_table_path,backup_dir + 'staff_table' + time.strftime("%Y-%m-%d %H-%M-%S"))
        func(*args,**kwargs)
    return bk
'''查询员工信息'''
def search():
    user_search = input("请输入查询语句：").strip()
    user_search_list = user_search.split(' ') #拆分为列表
    search_info = [] #搜索结果放此列表
    with open(staff_table_path,'r',encoding='utf-8') as f:
        for line in f:
            user_info = line.strip().split(',') #循环出员工信息并拆分为列表
            conditional = '%s %s %s' %(user_info[2],user_search_list[6],user_search_list[7]) #将条件字符串写入变量
            if user_search_list[6] == '=': #判断是等号就替换
                conditional =conditional.replace('=','==')
            if user_search_list[5] == 'age' and user_info[0].isdigit() and eval(conditional):#判断年龄和员工账户
                print(type(conditional))
                search_info.append([user_info[1],user_info[2]])
            elif user_search_list[5] == 'dept'and user_info[4] in user_search_list[7]: #判断员工职位条件
                search_info.append(user_info)
            elif user_search_list[5] == 'enroll_date' and user_info[5][0:4] in user_search_list[7]: #判断日期
                search_info.append(user_info)
        if not search_info:
            print("\033[36;1m没有找到你要搜索的员工！\033[0m\n")
        else:
            print("\033[35;1m找到以下员工信息！\033[0m\n")
            for i in search_info:
                print(' | '.join(i))
            print("\n\033[35;1m一共找到 %d 条信息\033[0m" % len(search_info))
    return search_info
'''添加员工信息'''
@bakcup
def add():
    user_add = input("请输入添加员工信息的语句：").strip()
    add_list = user_add.split(',') #拆分为列表
    phone = [] #电话列表
    with open(staff_table_path,'r+',encoding='utf-8') as f:
        user_id = 0 #员工id初始变量值
        for line in f:
            user_info = line.strip().split(',') #拆分为列表
            phone.append(user_info[3])
            if user_info[0].isdigit() and user_id < int(user_info[0]):#判断员工id
                user_id = int(user_info[0]) #这里取文件最后一个员工的id号，如果没有则user_id为0
        if add_list[2] not in phone: #判断电话是否唯一
            f.write('\n' + str(user_id + 1) + ',' + ','.join(add_list))
            print("\033[35;1m员工 %s 的信息已经添加成功！\033[0m\n" % add_list[0])
        else:
            print("\033[35;1m你要添加员工的phone已经存在！\033[0m\n")
'''删除员工信息'''
@bakcup
def delete():
    user_del = input("请输入你要删除的员工id号：").strip()
    flag = False
    with open(staff_table_path,'r',encoding='utf-8') as f,\
            open(staff_table_path + '_new','w',encoding='utf-8') as f2:
        for line in f:
            line = line.split(',')
            if line[0] == user_del:
                username = line[1] #定义删除的员工名，给后面输出提示
                line = ''
            elif line[0].isdigit() and int(user_del) < int(line[0]): #删除的员工后面的id减1
                line[0] = str(int(line[0]) - 1)
                flag = True
            f2.write(','.join(line)) #把列表里面的各个元素以逗号分开后连接成整个元素并写到文件中
    if flag == True:
        os.remove(staff_table_path)
        os.rename(staff_table_path + '_new',staff_table_path)
        print("\033[35;1m员工 %s 对应的id %s 已经删除\033[0m" %(username,user_del) )
    else:
        print("\033[36;1m你查找的员工信息不存在\033[0m")
'''修改员工信息'''
@bakcup
def alter():
    user_alter = input("请输入你要修改的员工信息语句：").strip()
    altre_list = user_alter.split(' ')
    flag = False
    user_list = []
    with open(staff_table_path, 'r', encoding='utf-8') as f, \
            open(staff_table_path + '_new', 'w', encoding='utf-8') as f2:
        for line in f:
            user_info = line.strip().split(',')
            if user_info[4] in altre_list[9]:
                user_info[4] = altre_list[5].strip('"')
                user_list.append(user_info)
                flag = True
            print(user_info[4])
            f2.write(','.join(user_info) + '\n') #把列表里面的各个元素以逗号分开后连接成整个元素并写到文件中
    if flag == True:
        os.remove(staff_table_path)
        os.rename(staff_table_path + '_new',staff_table_path)
        print("\033[35;1m员工信息已经修改\n %s\033[0m" %user_list)
    else:
        print("你输入修改员工信息语句无效")
while True:
    print("""\t \033[31;1m1.查询员工信息
    2.添加员工信息
    3.修改员工信息
    4.删除员工信息
    5.退出\033[0m""")
    main_dict = {'1':search,'2':add,'3':alter,'4':delete}
    user_choose = input("\033[39;1m请输入你要操作的选项号：\033[0m").strip()
    if user_choose in main_dict.keys():
        main_dict[user_choose]() #执行输入号码对应的函数
    elif user_choose == '5':
        exit("\033[35;1m已退出程序，欢迎下次使用\033[0m")
    else:
        print("\033[36;1m输入格式无效\033[0m")


