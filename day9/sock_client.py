#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import socket
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input(">>>").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)#接受命令结果的长度
    print("命令结果大小",cmd_res_size)
    client.send("准备好接收，可以发了".encode('utf-8')) #给服务端发一条回复解决粘包问题
    received_size = 0
    received_data = b''
    while received_size != int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data) #接受到的可能小于1024，用len判断
        received_data += data
    else:
        print("cmd_res receive done",received_size)
        print(received_data.decode())
client.close()
