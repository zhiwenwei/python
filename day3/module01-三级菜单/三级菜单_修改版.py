#coding:utf-8
#Author:Mr Zhi
menu_f = open("menu",'r',encoding="utf-8")
menu = eval(menu_f.read())
l = []
while True:
    for key in menu:  #遍历字典
        print(key)     #打印出键值，也就是父字典
    choice = input("input your choice:").strip()  #
    if choice == "q": #判断退出
        menu = l[-1]  #赋值menu菜单等于列表的最后一个列表元素，把一个字典加到列表中
        l.pop()  #清空列表
    if len(choice) == 0 or choice not in menu: continue #判断不输入或者输入不在字典中时继续运行程序
    l.append(menu)  #把字典加到列表
    menu = menu[choice]  #重新复制选择的字典名称