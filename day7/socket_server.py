#coding:utf-8
#Author:zhiwenwei
#服务端
import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6969)) #绑定要监听的端口
server.listen()  #监听
conn,addr = server.accept() #conn是客户端连接过来而在服务器端生成的一个连接实例
data = conn.recv(1024)
print("接收到信息",data)
server.close()

