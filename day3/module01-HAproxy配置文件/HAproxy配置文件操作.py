#coding:utf-8
#Author:Mr Zhi
"""
HAproxy配置文件操作：

1. 根据用户输入输出对应的backend下的server信息

2. 可添加backend 和sever信息

3. 可修改backend 和sever信息

4. 可删除backend 和sever信息

5. 操作配置文件前进行备份

6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作

配置文件 参考 http://www.cnblogs.com/alex3714/articles/5717620.html
"""
import shutil
def Menu(): #定于关于菜单函数
    menu = (
        """\033[35;1m
        1.增加
        2.删除
        3.修改
        4.查询
        \033[0m""")
    print(menu.strip('\n'))

def Backup_proxy(): #定于关于备份文件的函数
    shutil.copyfile("HAproxy.conf","HAproxy.conf.bak")

def Add_haproxy():  #定义关于增加加数据的函数
    domain = input('输入你要添加的域名:')
    domain_ip = input("输入你要添加的ip:")
    domain_weight = input("输入weight值:")
    domain_maxconn = input("输入maxconn值:")
    Backup_proxy()  # 写入数据前执行备份文件的函数
    with open("HAproxy.conf","a+",encoding="utf-8") as f: #打开文件追加模式
        f_w = "backend %s\n\t\t server %s %s weight %s maxconn %s" % (domain,domain_ip,domain_ip,domain_weight,domain_maxconn)
        f.write('\n' + f_w), f.flush() ##把数据写入文件
        print("\033[36;1m添加成功!\033[0m")

def Alter_haproxy(): #定义关于修改数据的函数
    domain_old1 = input("输入你要修改的域名:")
    print(type(domain_old1))
    domain_new1 = input("输入新域名:")
    ip_new1 = input("输入修改后的ip：")
    weight_new1 = input("输入修改后的weight值:")
    maxconn_new1 = input("输入修改后的maxconn值:")
    with open("HAproxy.conf", "r", encoding="utf-8") as f:
        lines = f.readlines()
        num = lines.index("backend %s\n" %domain_old1) #赋值域名对应的列表索引号
        lines[num] = "backend %s\n" %domain_new1 #根据索引号修改对应的backend
        lines[num + 1] = "\t\tserver %s %s weight %s maxconn %s\n" % (ip_new1,ip_new1,weight_new1,maxconn_new1) #根据索引号修改对应的server
        Backup_proxy()  # 写入数据前执行备份文件的函数
    with open("HAproxy.conf", "w", encoding="utf-8") as f_w:
        for line in lines:
            f_w.write(line) #把修改后的列表写入文件中
        print("\033[32;1m修改成功!\033[0m")

def Search_haproxy():  #定义关于查看数据的函数
    domain= input("输入你要查看的域名:")
    with open("HAproxy.conf", "r", encoding="utf-8") as f:
        lines = f.readlines()
        num = lines.index("backend %s\n" %domain) #赋值域名对应的列表索引号
        lines[num] = "backend %s\n" %domain #根据索引号修改对应的backend
        print(lines[num],lines[num + 1])

def Delete_haproxy(): #定义关于删除数据的函数
    domain = input("输入你要删除的域名节点:")
    with open("HAproxy.conf", "r", encoding="utf-8") as f:
        lines = f.readlines()
        num = lines.index("backend %s\n" %domain) #赋值域名对应的列表索引号
        lines.pop(num)
        lines.pop(num) #这里不用num + 1，因为上面已经删除了一个索引号
    Backup_proxy()  # 写入数据前执行备份文件的函数
    with open("HAproxy.conf", "w", encoding="utf-8") as f_w: #打开文件
        for line in lines:
            f_w.write(line)
        print("\033[37;1m删除成功!\033[0m")

while True:
    Menu()
    number = int(input("input number:"))
    if number == 1:
        Add_haproxy()
    elif number == 2:
        Delete_haproxy()
    elif number == 3:
        Alter_haproxy()
    elif number == 4:
        Search_haproxy()
    else:
        print("\033[31;1mInput is woring\033[0m")
        continue