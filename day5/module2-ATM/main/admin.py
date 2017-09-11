#coding:utf-8
#Author:zhiwenwei
import os,json
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''数据库文件的绝对路径'''
creditcard_data = base_dir + '/db/creditcard_data'
user_dir = base_dir + '/db/user_data'

'''管理员用户认证装饰器'''
def auth_admin(func):
    def wrapper(*args,**kwargs):
        while True:
            check = input("是否确认认证用户？y确认q退出认证")
            if check == "y":
                print("管理员用户认证".center(60,'-'))
                username = input("请输入管理员账户：").strip()
                passwd = input("请输入管理员密码：").strip()
                with open(user_dir, 'r', encoding='utf-8') as f:
                    _user_data = json.loads(f.read())
                    if username in _user_data.keys() and int(passwd) == int(_user_data[username]):
                        print("用户%s认证成功"%(username))
                    else:
                        print("用户名或密码有误")
                        continue
            else:
                print("已退出管理用户认证")
                break
            func(*args,**kwargs)
    return wrapper

'''申请信用卡'''
@auth_admin
def apply():
    while True:
        print("申请信用卡".center(40,'-'))
        with open(creditcard_data,'r+',encoding='utf-8') as f:
            _credictcard_data = json.loads(f.read())
            credictcard_id = input("请输入你要申请的信用卡号(八位数字)：")
            if credictcard_id.isdigit() and len(credictcard_id) == 8:
                if credictcard_id not in _credictcard_data.keys():
                    apply_user = input("请输入信用卡申请人：").strip()
                    apply_passwd = input("请输入信用卡密码(六位数)：").strip()
                    if len(apply_user) > 0:
                        if apply_passwd.isdigit() and len(apply_passwd) == 6:
                            _credictcard_data[credictcard_id] = {"limitcash": 7500, "password":int(apply_passwd), "personinfo": apply_user,"locked": "False",
                                                                 "deflimit": 15000, "credictcard": int(credictcard_id), "limit": 15000, "totalbill": 0}
                            dict = json.dumps(_credictcard_data)
                            f.seek(0)
                            f.truncate(0)
                            f.write(dict)
                            f.flush()
                            print("申请信用卡成功！\n卡号：%s\t持卡人：%s\n额度：15000\t取现额度：7500"%(credictcard_id,apply_user))
                            break
                        else:
                            print("输入密码有误！")
                            continue
                    else:
                        print("申请人不能为空")
                else:
                    print("改信用卡已存在")
                    continue
            else:
                print("输入信用卡有误!")
'''修改信用卡密码'''
@auth_admin
def alter_pw():
    while True:
        print("修改信用卡密码".center(40,'-'))
        with open(creditcard_data,'r+',encoding='-utf8') as f:
            _creditcard_data = json.loads(f.read())
            creditcard_id = input("请输入你要修改的信用卡：").strip()
            if creditcard_id.isdigit() and len(creditcard_id) ==8:
                if creditcard_id in _creditcard_data.keys():
                    passwd = _creditcard_data[creditcard_id]["password"]
                    _passwd = input("请输入信用卡原密码：").strip()
                    if int(_passwd) == passwd:
                        passwd_new = input("请输入你要设置的信用卡密码：").strip()
                        _creditcard_data[creditcard_id]["password"] = int(passwd_new)
                        dict = json.dumps(_creditcard_data)
                        f.seek(0)
                        f.truncate(0)
                        f.write(dict)
                        f.flush()
                        print("密码修改成功！")
                        break
                    else:
                        print("你输入的原密码有误！")
                else:
                    print("你输入的信用卡不存在")
            else:
                print("你输入的信用卡有误")
'''添加管理员账户'''
@auth_admin
def alter_admin():
    while True:
        print("添加管理员账户".center(50,'-'))
        username = input("请设置管理员账户名：").strip()
        passwd = input("请设置账户密码：").strip()
        with open(user_dir,'r+',encoding='utf-8') as f:
            user_data = json.loads(f.read())
            if username not in user_data.keys():
                if len(username) >= 0 and len(passwd) >= 0:
                    user_data[username] = passwd
                    user_data = json.dumps(user_data)
                    f.seek(0)
                    f.truncate(0)
                    f.write(user_data)
                    f.flush()
                    print("成功添加[%s]管理员"%(username))
                    break
                else:
                    print("账户或密码不能为空")
            else:
                print("该管理账户名[%s]已存在！请换一个用户名！"%(username))
                continue