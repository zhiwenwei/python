#coding:utf-8
#Author:Mr Zhi
count = 0       #为累计密码输入次数，赋值初始值
User_info_file = open("User_info",'r',encoding="utf-8")     #打开用户信息文件
Locked_user_file = open("Locked_user",'r+',encoding="utf-8")    #打开锁定用户文件
User_info_line = eval(User_info_file.read())    #把用户信息文件内容转换为字典
Locked_user_line = Locked_user_file.read()  #读取锁定的用户文件
def close_file():   #经常重复的代码，定义一个函数
    Locked_user_file.close()    #关闭文件
    User_info_file.close()      #关闭文件
    exit()      #结束程序
while True:     #开始循环
     username = input("请输入你的用户名:")  #输入用户名
     password = input("请输入你的密码:")   #输入密码
     if len(username) == 0 or len(password) == 0: #判断用户名或密码是否为空
         print("你输入用户名或者密码为空！")  #提示用户名或密码为空
         close_file()  #执行自定义函数结束程序
     if username in User_info_line.keys() and username not in Locked_user_line: #判断用户名是否在用户信息文件和锁定用户文件中
         if password == User_info_line["{user}".format(user=username)]:  #判断输入的密码是否对应用户的密码
             print("欢迎 {user} 成功登陆....".format(user=username))  #打印出登陆的信息
             close_file()    #执行自定义函数
         while count < 3:    #循环三次
            count += 1       #累加次数
            password = input("密码错误，你剩下{num}次输入密码的机会：".format(num = 4 - count))  #重新输入密码并提示剩下次数
            if len(password) == 0: #判断密码是否为空
                print("密码不能为空") #提示密码不能为空
                count -= 1   #不累加输入次数
            if password == User_info_line.values():     #判断密码是否正确
                print("欢迎 {user} 用户成功登陆....".format(user=username))     #输出登陆成功信息
                close_file()    #执行自定义函数
            if count == 3:      #判断累计的次数是否三次
                Locked_user_file.write(username+'\n')   #把用户名追加到锁定用户文件中
                print("超过次数，你的用户{user}被锁定".format(user=username))   #输出锁定用户的提示
                close_file()    #执行自定义函数
     elif username in Locked_user_line:     #判断用户名是否在锁定用户文件中
         print("你的用户{user}已经被锁定".format(user=username))     #输出锁定用户的提示
         close_file()   #执行自定义函数
     else:
         print("用户名不存在！")   #输出用户不存在的提示
         close_file()    #执行自定义函数




