# -*- coding: utf-8 -*-

import paramiko
class SSHConnection(object):
    def __init__(self,host='45.199.182.238',port=23424,username='zww',password='123'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.__k=None
    def run(self):
        self.connect() #连接远程服务器
        self.upload('/root/test.txt','/home/zww/a.txt')#上传本地文件到远端服务器
        self.cmd('df -h')
        self.close() #关闭连接
    def connect(self):
        transport=paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.password)
        self.__transport=transport
    def close(self):
        self.__transport.close()
    def upload(self,local_path,ssh_path):
        sftp=paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path,ssh_path)
    def cmd(self,command):
        ssh=paramiko.SSHClient()
        ssh._transport=self.__transport
        stdin,stdout,stderr=ssh.exec_command(command)
        print(stdout.read().decode())

obj=SSHConnection()
obj.run()

