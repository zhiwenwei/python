#coding:utf-8
#Author:Mr Zhi
file_o = open("menu",'r',encoding="utf-8") #打开三级菜单文件
menu= eval(file_o.read())  #把打开后的文件内容转换成字典(文件内容原本是字典)
def out():     #频繁使用的代码定义个函数
    file_o.close()  #关闭打开的文件
    exit()  #退出程序
for i in menu: #遍历菜单menu字典
    print(i)  #输出字典菜单
while True:   #开始while循环
    choice = input("输入地区(按q退出，b返回上层)：") #输入地区
    if choice == "q": #判断输入chice值是否为q
        out()   #执行函数
    if choice == "b": #判断输入chice值是否为b
        print("已是第一层")
        continue
    if choice not in menu or len(choice) == 0 and choice != "b": #判断输入choice值在菜单文件中或输入choice不等于b
        print("你输入有误，请重新输入3")
    if choice in menu:  #p判断输入choice是否在menu中
        for i in menu[choice]: #遍历menu[choice]
            print(i)
        choice2 = input("输入省区(按q退出，b返回上层)：")  #输入结果
        if choice2 not in menu[choice] and choice2 != "b":#判断输入choice2 不在字典中和不等于b
            print("你输入有误，请重新输入2")
        if choice2 in menu[choice]: #判断
            for i2 in menu[choice][choice2]:  #遍历字典
                print(i2)
            print("最后一层菜单，下面没有了2")
        if choice2 == "q": #判断
            out()
        if choice2 == "b":#判断
            continue #继续循环

