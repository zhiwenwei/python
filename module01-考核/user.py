#coding:utf-8
#Author:Mr Zhi
"""  (1)用户输入帐号密码进行登陆
  (2)用户信息保存在文件内
  (3)用户密码输入错误三次后锁定用户"""
user = {"zww":"123",} #定义正确的用户名和密码
user_locked = open("user_locked",'r+',encoding="utf-8") #定义输错三次后被锁定的用户文件
user_locked_line = user_locked.read()
username = input("username:")
password = input("password:")
while True:
    if len(username) == 0 or len(password) ==0:#判断用户名密码为空
        print("你输入的用户名或密码为空")
    if username in user_locked_line:
        print("你的用户已经被锁定！")
        break
    if username in user.keys() and password == user[username].format(password = password):
        print("welcome to login...")
        break
    if username in user.keys() and username not in user_locked_line:
        count = 0
        while count <3:
            count +=1
            password = input("请重新输入密码：")
            if password == user[username].format(password = password):
                print("welcome")
                break
            elif count == 3:
                print("你的用户已经被锁定")
                user_locked.write(username+'\n')
                user_locked.flush()
                user_locked.close()
                break
            else:
                print("请重新输入密码，还有{count}".format(count = count))
                continue
