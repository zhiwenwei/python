#coding:utf-8
#Author:Mr Zhi
#configparse用于生成和修改常见配置文档，当前模块名称在python 3.x版本中变更为configparse

#生成配置文件
import configparser
config = configparser.ConfigParser()
config['client'] = {'port':'3306','socket':'/tmp/mysql.sock'}
config['mysqldump'] = {'quick':'','max':'16m'}
with open('my.cnf', 'w') as configfile:
   config.write(configfile)