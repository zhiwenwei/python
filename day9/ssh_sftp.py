# -*- coding: utf-8 -*-

import paramiko
transport=paramiko.Transport(('45.199.182.238',23424))
transport.connect(username='zww',password='123')
sftp=paramiko.SFTPClient.from_transport(transport)
sftp.put('/root/a.log','/tmp/a.log')
sftp.get('/home/zww/abc.txt','/tmp/a.txt')
