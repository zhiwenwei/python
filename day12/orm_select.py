#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("mysql+pymysql://zww:123@192.168.10.144/zdb",
                       encoding='utf-8')
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
Base = declarative_base()  # 生成orm基类
class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
Base.metadata.create_all(engine)  # 创建表结构
#查询
my_user = Session.query(User).filter(User,User.id==1).all()
print(my_user)
#修改
