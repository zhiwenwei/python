#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import os
import sys
import platform
'''定义配置文件的路径'''
if platform.system() == "Windows":
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
else:
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(sys.argv[0])).split("/")[:-1])
sys.path.insert(0,BASE_DIR) #增加环境变量
conf_path = os.path.join(BASE_DIR,"conf") #配置文件的目录
server_file = os.path.join(conf_path,"server") #主机名和密码端口保存文件路径
download_dir = os.path.join(BASE_DIR,"db","download") #下载文件保存目录
upload_dir = os.path.join(BASE_DIR,"db","upload")   #上传文件的目录
print(os.listdir(upload_dir))
print(BASE_DIR,download_dir)




