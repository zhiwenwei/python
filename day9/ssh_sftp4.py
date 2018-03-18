# -*- coding: utf-8 -*-
import paramiko, sys, os, socket, select, getpass
from paramiko.py3compat import u
tran = paramiko.Transport(('45.199.182.238', 23424,))
tran.start_client()
tran.auth_password('zww', '123')
# 打开一个通道
chan = tran.open_session()
# 获取一个终端
chan.get_pty()
# 激活器
chan.invoke_shell()
while True:
    readable, writeable, error = select.select([chan, sys.stdin, ],[],[],1)
    if chan in readable:
        try:
            x = u(chan.recv(1024))
            if len(x) == 0:
                print('\r\n*** EOF\r\n')
                break
            sys.stdout.write(x)   # 写入缓冲区
            sys.stdout.flush()    # 刷新，将缓冲区内容显示出来
        except socket.timeout:
            pass
    if sys.stdin in readable:
        inp = sys.stdin.readline()
        chan.sendall(inp)
chan.close()
tran.close()

