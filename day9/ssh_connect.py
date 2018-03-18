# -*- coding: utf-8 -*-
#!/usr/bin/python3
#用于连接远程服务器并执行命令
import paramiko
#创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='45.199.182.238',port=23424,username='zww',password='123')
#执行命令并获取命令输出结果
stdin,stdout,stderr=ssh.exec_command('df -h')
res=stdout.read()
print(res.decode())
#关闭连接
ssh.close()


