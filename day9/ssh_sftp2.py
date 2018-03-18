# -*- coding: utf-8 -*-

import paramiko
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
transport = paramiko.Transport(('45.199.182.238', 23424))
transport.connect(username='zww', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/po.sh', '/tmp/abc.py')
# 将remove_path 下载到本地 local_path
sftp.get('/tmp/a.log', '/root/a.log')
transport.close()
