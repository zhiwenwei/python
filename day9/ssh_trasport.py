# -*- coding: utf-8 -*-
import paramiko
transport = paramiko.Transport(('45.199.182.238',23424))
transport.connect(username='zww',password='123')
ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exec_command('df -h')
print(stdout.read().decode())
transport.close()
