#coding:utf-8
#Author:zhiwenwei
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969)) #主动发起tcp服务器连接
res = input("输入你要发送的信息：").strip()
client.send(bytes(res,encoding='utf-8'))  #发送tcp消息
#data = client.recv(1024)  #接收
print("成功发送：",res)
client.close() #关闭服务器套接字



