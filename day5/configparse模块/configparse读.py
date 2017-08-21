#coding:utf-8
#Author:Mr Zhi
import configparser
config = configparser.ConfigParser()
print(config.read('my.cnf'))
print(config.sections()) #读取选项
print(config['client']['port'])