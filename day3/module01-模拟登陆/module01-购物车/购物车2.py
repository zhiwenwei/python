#coding:utf-8
#Author:Mr Zhi
import os,sys
user_file = open("user_list",'r+',encoding="utf-8") # 打开用户列表
user_list = user_file.read()
if "xkl" in user_list:
    print("yes")
def regis():
    username = input("username")
    if username not in user_list:
        print("改用户名可以注册")
        password =input("password")
        password2 =input("password again")
        if password == password2:
            name_info = '''
            恭喜注册成功！！！
            用户名：{user}
            密  码：{password}
            '''
            print(name_info.format(user=username,password=password2))
            user_list_r = username,password
            user_list_r_list = ','.join(user_list_r)
            user_file.write(str(user_list_r_list)+'\n')
            user_file.flush()
regis()

user_list_line = eval(user_list)
print(type(user_list_line))