#coding:utf-8
#Author:zhiwenwei
import os,json
base_dir = os.path.dirname(os.path.dirname(__file__))
user_dir = base_dir + '/db/user_data'
'''管理员用户认证装饰器'''
def auth(auth_type):
    def wrapper(func):
        if auth_type == "admin_auth":
            def admin_login():
                res = func
                username = input("请输入管理员账户：").strip()
                passwd = input("请输入管理员密码：").strip()
                with open(user_dir, 'r+', encoding='utf-8') as f:
                    _user_data = json.loads(f.read())
                    if username in _user_data.keys() and passwd == int(_user_data[username]):
                        print("用户%s登陆成功"%(username))
                        return res
                    else:
                        print("用户名或密码有误")
            return admin_login
        return wrapper
