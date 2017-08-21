#coding:utf-8
#Author:Mr Zhi
"""
import os,sys,time,re,prettytable,json
HAproxy配置文件操作：

1. 根据用户输入输出对应的backend下的server信息

2. 可添加backend 和sever信息

3. 可修改backend 和sever信息

4. 可删除backend 和sever信息

5. 操作配置文件前进行备份

6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作

配置文件 参考 http://www.cnblogs.com/alex3714/articles/5717620.html
"""

arg = {
    'backend': 'www.oldboy.org',
    'record': {
        'server': '100.1.7.9',
        'weight': 20,
        'maxconn': 30
    }
}
#print(arg["record"]["server"])
def menu():
    menu = (
        """
        1.增加节点
        2.删除节点
        3.修改节点
        4.查询节点
        """)
    print(menu.strip('\n'))
#content = input("请输入域名：")
#content1 = list(content)
# print(type(content))
# conf = open("HAproxy.conf","r",encoding="utf-8")
# conf_r = conf.read()
# conf_dict = eval(conf_r)
# for line in conf_dict:
#     if line.startswith("backend") and content["backend"] in line:
#         print(line.startswith("backend"))
#         print(content["backend"])

# def SearchConf():
#     content = eval("请输入域名：")
#domain = input('plz input backend:')
# def Search_haproxy():
#     haproxy_list = [] #定义文件内容列表
#     domain = input("plz input domain:")
#     with open("HAproxy.conf","r",encoding="utf-8") as f:
#         for (num,value) in enumerate(f.readlines()):
#             haproxy_list.append(value.strip()) #去除字符串的回车和空格并加到列表中
#     ha = haproxy_list[27:]
#     print(type(ha))
#     hah = str(ha)
#     print(hah.strip('\n'))
    # for line in f:
    #     if line.startswith("backend %s" %domain):
    #         print("yes")

# if domain in haproxy_list[27:]:
#     print("yes")
# else:
#     print("no")
def Add_haproxy():  #定义关于添加数据的函数
    #print(arg["backend"]["record"][1])
    backend = input('plz input backend:')
    backend_ip = input("plz input ip:")
    backend_weight = input("plz input weight:")
    backend_maxconn = input("plz input maxconn:")
    # arg["backend"] = [backend]
    # arg["record"][0] = [backend_ip]
    # arg["record"][1] = [backend_weight]
    # arg["record"][2] = [backend_maxconn]
    with open("HAproxy.conf","a+",encoding="utf-8") as f: #打开文件追加模式
        f_w = "backendd %s \n\t\t server %s %s weight %s maxconn %s" % (backend,backend_ip,backend_ip,backend_weight,backend_maxconn)
        #f.write('\n'+ f_w),f.flush(),f.close() #把数据写入文件后进行关闭操作
        f.write('\n' + f_w), f.flush() ##把数据写入文件
#Search_haproxy()
#Search_haproxy()

def delete_haproxy():
    domain = input("plz input domain:")
    with open("HAproxy.conf", "r+", encoding="utf-8") as f:
        f_read = f.readlines()
        print(f_read)
        print("backend %s" %domain)
        if "backend %s\n".format(backend=domain) in f_read:
            print("yes")
        else:
            print("no")
#delete_haproxy()


# import os
# os.system("copy HAproxy.conf HAproxy.conf.bak")  #文件备份
# import shutil
# domain = input("plz input domain:")
# with open('HAproxy.conf', 'r') as f:
#     with open('file.new', 'w') as g:
#         for line in f.readlines():
#             if "backend domain" in line:
#                 g.write(line)
# shutil.move('file.new', 'HAproxy.conf')
import re
def Alter_haproxy():
    domain_old = input("输入你要修改的域名:")
    domain_new = input("输入新域名:")
    ip_new = input("输入修改后的ip：")
    weight_new = input("输入修改后的weight:")
    maxconn_new = input("输入修改后的maxconn:")
    with open("HAproxy.conf", "r", encoding="utf-8") as f:
        lines = f.readlines()
        num = lines.index("backend %s\n" %domain_old) #赋值域名对应的列表索引号
        print(num)
        lines[num] = "backend %s\n" %domain_new #根据索引号修改对应的backend
        lines[num + 1] = "\t\tserver %s %s weight %s maxconn %s\n" % (ip_new,ip_new,weight_new,maxconn_new) #根据索引号修改对应的server
                # print(line)
                # if re.search('backend %s' %domain,line):
                #     line_sub = re.sub('backend %s' %domain,'zhiwenwei',line)
                #     data += line_sub
                #     print(data)
    with open("HAproxy.conf", "w", encoding="utf-8") as f_w: #打开文件
        for line in lines:
            # if "backend www.oldboy.org" in line:
            #     line = line.replace("backend %s" %domain_old,"backend www.%s.com" %domain_new)
            #     print(line)
            f_w.write(line) #把修改后的列表写入文件中
        print(lines)



#Alter_haproxy()
# with open("out_file", 'a+') as f:
#     f.write(''.join([line for line in open("in_file","a+").readlines() if 'nihao' not in line]))

def Search_haproxy():  #定义关于查看输的函数
    domain= input("输入你要查看的域名:")
    with open("HAproxy.conf", "r", encoding="utf-8") as f:
        lines = f.readlines()
        num = lines.index("backend %s\n" %domain) #赋值域名对应的列表索引号
        lines[num] = "backend %s\n" %domain #根据索引号修改对应的backend
        #lines[num + 1] = "\t\tserver %s %s weight %s maxconn %s\n" % (ip_new,ip_new,weight_new,maxconn_new) #根据索引号修改对应的server
        print(lines[num],lines[num + 1])


def Delete_haproxy(): #定义关于删除数据的函数
    domain = input("输入你要删除的域名节点:")
    with open("HAproxy.conf", "r", encoding="utf-8") as f:
        lines = f.readlines()
        num = lines.index("backend %s\n" %domain) #赋值域名对应的列表索引号
        lines.pop(num)
        lines.pop(num) #这里不用num + 1，因为上面已经删除了一个索引号
    with open("HAproxy.conf", "w", encoding="utf-8") as f_w: #打开文件
        for line in lines:
            # if "backend www.oldboy.org" in line:
            #     line = line.replace("backend %s" %domain_old,"backend www.%s.com" %domain_new)
            #     print(line)
            f_w.write(line) #
Delete_haproxy()