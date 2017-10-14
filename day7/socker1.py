#coding:utf-8
#Author:zhiwenwei
import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen()
while True:
    conn,addr = sk.accept()
    conn.sendall(bytes("欢迎光临",encoding='utf-8'))
    size = conn.recv(1024)
    size_str = str(size,encoding='utf-8')
    file_size = int(size_str)
    conn.sendall(bytes("开始传送",encoding='utf-8'))
    has_size = 0
    f = open("a.txt","wb")
    while True:
        if file_size == has_size:
            break
        data = conn.recv(1024)
        f.write(data)
        has_size += file_size
    f.close()

