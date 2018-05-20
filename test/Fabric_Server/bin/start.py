#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import os
import sys
import platform
# import configparser
# import paramiko
'''定义配置文件的路径'''
if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(sys.argv[0])).split("/")[:-1])
sys.path.insert(0,BASE_DIR) #添加到环境变量
from core import main
def interaction():
    a = main.Fabric_host()
    print('请选择'.center(40,'#'))
    option = input(
        '''1.执行命令\n2.上传文件\n3.下载文件\n4.增加远程主机\n5.退出程序\ncmd>>>:'''
    ).strip()

    while True:
        if option == '1':
            a.connect_cmd()
        elif option == '2':
            a.connect_upload()
        elif option == '3':
            a.connect_download()
        elif option == '4':
            a.add_host()
        elif option == '5':
            exit()
        else:
            print("输入有误")

if __name__ == '__main__':
    interaction()