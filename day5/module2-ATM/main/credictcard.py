#coding:utf-8
#Author:支文伟
"""信用卡中心"""
import os
import json
from log import get_logger #导入日志模块
'''获取数据文件的绝对路径'''
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取当前目录的上级目录绝对路径
creditcard_path = base_dir + '/db/creditcard_data'
user_path = base_dir + '/db/user_data'
recordlog_path = base_dir + '/log/record.log'
logger = get_logger() #日志实例化对象
'''个人信用卡信息'''
def creditcard_info():
    while True:
        with open(creditcard_path,'r',encoding='utf8') as f:
            creditcard_data = json.loads(f.read())
            choice = input("请输入你要查询的信用卡卡号(8位数字)(退出输入q)：").strip()
            if choice in creditcard_data.keys():
                print("我的信用卡信息：".center(50,'-'))
                print("持卡人：[ %s ]\n卡号：[ %s ]\n额度：[ %s ]\n可用额度：[ %s ]\n提现额度：[ %s ]"
                      % (creditcard_data[choice]["personinfo"],choice,creditcard_data[choice]["deflimit"],
                         creditcard_data[choice]["limit"],creditcard_data[choice]["limitcash"]))
            elif choice == "q":
                    break
            else:
                print("你输入的信用卡不存在！")
'''信用卡转账'''
def transfer():
    while  True:
        print("信用卡转账".center(50, '-'))
        with open(creditcard_path,'r+',encoding='utf8') as f:
            creditcard_data = json.loads(f.read())
            choice = input("请输入你的信用卡账号('q'返回):").strip()
            if choice == 'q':
                break
            if choice in creditcard_data.keys():
                now_limit = creditcard_data[choice]["limit"]
                transfer_card = input("请输入你要转账的账户：").strip()
                if transfer_card.isdigit() and transfer_card in creditcard_data.keys() and len(transfer_card) == 8:
                    transfer_money = input("请输入转账金额：").strip()
                    if transfer_money.isdigit():
                        transfer_money = int(transfer_money)
                        creditcard_passwd = input("请输入信用卡密码:").strip()
                        creditcard_passwd = int(creditcard_passwd)
                        if creditcard_passwd == creditcard_data[choice]["password"]:
                            if transfer_money <= int(now_limit):
                                creditcard_data[choice]["limit"] -= transfer_money
                                creditcard_data[choice]["limitcash"] -= transfer_money
                                creditcard_data[transfer_card]["limit"] += transfer_money
                                creditcard_data[transfer_card]["limitcash"] += transfer_money
                                print("转账成功".center(50,'-'))
                                print("转账金额：[ %s ]\n信用卡可用额度：[ %s ]" % (transfer_money,creditcard_data[choice]["limit"]))
                                '''转账信息记录到日志'''
                                transfer_info = ["信用卡转账",str(choice),str(transfer_money)]
                                transfer_info = '---'.join(transfer_info)
                                logger.debug(transfer_info)
                                f.seek(0)
                                #f.truncate(0)
                                creditcard_data_dumps = json.dumps(creditcard_data)
                                f.write(creditcard_data_dumps)
                            else:
                                print("转账额度不能大于信用额度")
                        else:
                            print("输入密码有误")
                    else:
                        print("请输入数字格式的金额！")
                else:
                    print("你输入的账户不存在")
            else:
                print("你输入的信用卡账号不存在！")
'''信用卡取现'''
def takecash():
    while True:
        print("信用卡取现".center(50,'-'))
        with open(creditcard_path,'r+',encoding='utf-8') as f:
            creditcard_data = json.loads(f.read())
            creditcard = input("请输入你的信用卡账号(q返回)：").strip()
            if creditcard == 'q':break
            if creditcard in creditcard_data.keys():
                limit = creditcard_data[creditcard]["limit"]
                limitcash = creditcard_data[creditcard]["limitcash"]
                totalbill = creditcard_data[creditcard]["totalbill"]
                print("信用卡额度：[ %d ]\n信用卡账单：[ %d ]\n单信用卡可取现额度：[ %d ]" %(limit,totalbill,limitcash,))
                cash = input("请输入你要取现的额度,手续费%5：").strip()
                if cash.isdigit() and 0 < int(cash) <= limitcash:
                    passwd = input("请输入信用卡:%s的密码：" %(creditcard)).strip()
                    if int(passwd) == creditcard_data[creditcard]["password"]:
                        cash = int(cash)
                        fee = cash * 0.05  # 手续费
                        total_cash = cash + fee
                        totalbill += cash
                        creditcard_data[creditcard]["limitcash"] -= total_cash
                        creditcard_data[creditcard]["limit"] -= total_cash
                        creditcard_data[creditcard]["totalbill"] = totalbill
                        print("成功取现：[%d]\n收取手续费:[%d]" %(cash,fee))
                        '''取现信息记录到日志'''
                        takecash_info = ["信用卡取现",creditcard,str(cash)]
                        takecash_info = '---'.join(takecash_info)
                        logger.debug(takecash_info)
                        '''永久保存数据库'''
                        f.seek(0)
                        creditcard_data = json.dumps(creditcard_data)
                        f.write(creditcard_data)
                        f.flush()
                    else:
                        print("信用卡密码有误！")
                else:
                    print("你输入额度含有非数字或超过可取现额度")
            else:
                print("你输入的信用卡账号不存在")
'''信用卡还款'''
def repayment():
    while True:
        print("信用卡还款".center(50,'-'))
        creditcard = input("请输入信用卡账号：").strip()
        with open(creditcard_path,'r+',encoding='utf8') as f:
            creditcard_data = json.loads(f.read())
            print(creditcard_data)
            if creditcard in creditcard_data.keys():
                totalbill = creditcard_data[creditcard]["totalbill"]
                print("你的信用卡[%s]总账单:[%d]"%(creditcard,totalbill))
                repayments = input("请输入你要还款的额度：").strip()
                if repayments.isdigit() and 0 < int(repayments) <= totalbill:
                    passwd = input("请输入信用卡:[%s]的密码："%(creditcard)).strip()
                    if int(passwd) == creditcard_data[creditcard]["password"]:
                        repayments = int(repayments)
                        creditcard_data[creditcard]["totalbill"] -= repayments
                        creditcard_data[creditcard]["limit"] += repayments
                        creditcard_data[creditcard]["limitcash"] += repayments
                        totalbill -= repayments
                        '''记录还款信息到日志'''
                        repayment_info = ["信用卡还款",creditcard,str(repayments)]
                        repayment_info = '---'.join(repayment_info)
                        logger.debug(repayment_info)
                        '''写到文件'''
                        f.seek(0)
                        creditcard_data = json.dumps(creditcard_data)
                        f.write(creditcard_data)
                        f.flush()
                        print("成功还款：[%d]\n剩下总账单：[%d]"%(repayments,totalbill))
                    else:
                        print("你输入的密码有误")
                else:
                    print("你输入的额度非数字或超过还款额度！")
            else:
                print("你输入的信用卡账号不存在！")

repayment()
# takecash()