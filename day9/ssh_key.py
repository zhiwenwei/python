# -*- coding: utf-8 -*-
#使用ssh-keygen命令创建秘钥对，公钥添加到目标主机对应用户的authorized_keys文件(远程添加公钥：ssh-copy-id '-p23424 zww@45.199.182.238')
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='45.199.182.238',port=23424,username='zww',pkey=private_key)
stdin,stdout,stderr=ssh.exec_command('df -h')
print(stdout.read().decode())
ssh.close()
