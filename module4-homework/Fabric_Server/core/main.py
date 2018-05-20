#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import os
import sys
import platform
import configparser
import paramiko
# '''定义配置文件的路径'''
# if platform.system() == "Windows":
#     BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
# else:
#     BASE_DIR = "/".join(os.path.abspath(os.path.dirname(sys.argv[0])).split("/")[:-1])
# sys.path.insert(0,BASE_DIR) #添加到环境变量
from conf import settings
class Fabric_host(object):
    def __init__(self): #主机名
        self.server_file = settings.server_file  #主机信息文件
        self.config_info = configparser.ConfigParser()  # 读数据对象
        #self.config_info.read(self.server_file)  # 读取文件
        self.name_list = [] #定义一个列表
    '''读取主机信息'''
    def host_info(self):
        self.config_info.read(self.server_file) #读取文件
        for i in range(len(self.config_info.sections())):
            self.name_list.append(self.config_info.sections()[i])
        else:
            print('主机列表:'.center(30,'#'))
            for i in self.name_list:
                print(('[%s]'%i).center(30,' '))
        self.config_info.clear()
    '''增加远程主机'''
    def add_host(self):
        print('增加主机'.center(30,'#'))
        hostname = input("请输入远程主机名:").strip()
        ip = input("请输入远程主机%s的ip："%hostname).strip()
        user = input("请输入主机%s用户名:"%hostname).strip()
        passwd = input("请输入用户%s的登录密码:"%user).strip()
        port = input("请输入主机%s的ssh端口:"%hostname).strip()
        self.config_info[hostname] = {'ip':ip,'user':user,'passwd':passwd,'port':port}
        with open(self.server_file,'a') as configfile:
            self.config_info.write(configfile)
        self.config_info.clear()
        print("主机%s添加成功！"%hostname)
    '''远程连接主机并执行命令'''
    def connect_cmd(self):
        self.host_info()
        host_name = input("请输入你要连接的主机:").strip()
        self.config_info.read(self.server_file)
        #print(self.config_info[host_name]['port'])
        ip = self.config_info[host_name]['ip']
        user = self.config_info[host_name]['user']
        passwd = self.config_info[host_name]['passwd']
        port = self.config_info[host_name]['port']
        ssh = paramiko.SSHClient()  #创建ssh对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())# 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=ip, port=port, username=user, password=passwd) #连接主机
        '''获取远程主机名'''
        stdin, stdout, stderr = ssh.exec_command('hostname -s')#执行命令并获取命令输出结果
        res = stdout.read()
        cmd = "%s@%s"%(user,res.strip().decode())
        print("Successful connecting to %s:%s"%(ip,port),"\n输入q端口远程连接")
        while True:
            _cmd = input("%s:" %cmd)
            if _cmd == "q":
                break
            stdin,stdout,stderr = ssh.exec_command(_cmd)
            res = stdout.read()
            print(res.decode())
        ssh.close() #关闭连接
    '''远程连接主机并进行传输文件（上传/下载）'''
    def connect_upload(self):
        self.host_info()
        host_name = input("请输入你要连接的主机:").strip()
        self.config_info.read(self.server_file)
        ip = self.config_info[host_name]['ip']
        user = self.config_info[host_name]['user']
        passwd = self.config_info[host_name]['passwd']
        port = self.config_info[host_name]['port']
        #使用sftp上传文件
        ssh = paramiko.SSHClient()  #创建ssh对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())# 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=ip, port=port, username=user, password=passwd) #连接主机
        tran = ssh.get_transport()#获取transport实例
        sftp = paramiko.SFTPClient.from_transport(tran)
        remotepath = '/tmp/'
        filename = input("请输入上传的文件名:").strip()
        localpath = settings.upload_dir
        sftp.put(os.path.join(localpath,filename),remotepath + filename)
        print(os.path.join(remotepath,filename))
        tran.close()
        print("上传成功")

    def connect_download(self):
        self.host_info()
        host_name = input("请输入你要连接的主机:").strip()
        self.config_info.read(self.server_file)
        ip = self.config_info[host_name]['ip']
        user = self.config_info[host_name]['user']
        passwd = self.config_info[host_name]['passwd']
        port = self.config_info[host_name]['port']
        transport = paramiko.Transport((ip,int(port)))#建立一个加密管道
        transport.connect(username=user, password=passwd) #建立连接
        sftp = paramiko.SFTPClient.from_transport(transport) ##建立一个sftp客户端对象，通过ssh transport操作远程文件
        local_path = settings.download_dir
        #server_path = input("请输入你要下载文件路径：")
        # server_path = '/tmp/'
        # local_path = input("请输入本地存放目录:")
        server_path = input("请输入你要下载文件路径：")
        filename = server_path.split('/')[-1] #获取文件名
        sftp.get(server_path,os.path.join(local_path,str(filename)))




