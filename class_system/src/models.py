#-*- coding:utf-8 -*-
#Author:Kevin
import time
import pickle
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #添加环境变量
from conf import settings
from src import identifier
'''定义父类，关于读写数据模块'''
class BaseModel:
    def save(self):
        file_path = os.path.join(self.db_path,str(self.nid))
        pickle.dump(self,open(file_path,'wb'))

    @staticmethod
    def get_all_obj_list(cls): #普通的方法，第一个参数需要是self，它表示一个具体的实例本身。对于类方法的参数cls表示这个类本身.
        ret = []
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path,filename)
            ret.append(pickle.load(open(file_path,'rb')))

'''学校类'''
class School(BaseModel):
    db_path = settings.SCHOOL_DB
    def __init__(self,name,addr):
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.__income = 0



