#coding:utf-8
#Author:Mr Zhi
import time
user,passwd = 'zww','zww123'
def auth(auth_type):
    def outer_wrapper(func):
        print("auth func:",auth_type)
        def wrappp(*args,**kwargs):
            username = input("username:").strip()
            password = input("password:").strip()
            if user == username and passwd == password:
                print("\033[35;1mUser has passwd authentication\033[0m")
                res = func(*args,**kwargs)
                print("----alter -----")
                return res
            else:
                exit("\033[32;1mInvalid username or password!\033[0m")
        return wrappp
    return outer_wrapper
@auth(auth_type="local")
def index():
    print("welcome to index page")
#     return "from index"
# @auth(auth_type="local") #home = auth
# def home():
#     print("welcome to home page")
# @auth(auth_type="local")
def bbs():
    print("welcome to bbs page")
# @auth(auth_type="local")
index()
