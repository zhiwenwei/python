# -*- coding: utf-8 -*-
import paramiko
private_key= paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
transport=paramiko.Transport(('45.199.182.238',23424))
transport.connect(username='zww',pkey=private_key)
ssh=paramiko.SSHClient()
ssh._transport=transport
stdin,stdout,stderr=ssh.exec_command('df -h')
print(stdout.read().decode())
transport.close()
