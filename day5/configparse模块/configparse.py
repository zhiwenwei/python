#coding:utf-8
#Author:Mr Zhi
#configparse用于生成和修改常见配置文档，当前模块名称在python 3.x版本中变更为configparse

#生成配置文件
import configparser
config = configparser.ConfigParser()
config.read()
config['hostname'] = {'port':'22','socket':'/tmp/mysql.sock'}
config['hostname2'] = {'quick':'','max':'16m'}
with open('my.cnf', 'a') as configfile:
   config.write(configfile)