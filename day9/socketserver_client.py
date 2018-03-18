#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import socket
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))
    data = client.recv(10240)
    print("recv",data.decode())
client.close()
