#-*- coding:utf-8 -*-
#Author:Kevin
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #添加环境变量

from models import School
def create_school():#创建学校
    # try:
    name = input("请输入学校名字")
    addr = input("请输入学校地址：")
    school_name_list = [(obj.name,obj.addr) for obj in School.get_all_obj_list()]
    # if (name,addr) in school_name_list:
    #     raise Exception('\033[43;1m[%s] [%s]校区 已经存在,不可重复创建\033[0m' % (name, addr))
    obj = School(name,addr)
    # print(school_name_list)
    obj.save()
    # status =True
    data = "[%s] [%s]校区创建成功"%(obj.name,obj.addr)
    print(data)
    # except Exception as e:
    #     status = False
    #     error =str(e)
    #     data = ''
    # return {'status': status, 'error': error, 'data': data}
create_school()