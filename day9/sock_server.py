#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import socket,os,time
server=socket.socket()
server.bind(('localhost',9999))
server.listen()
while True:
    conn,addr = server.accept()
    print("now conn",conn,addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令",data)
        cmd_res = os.popen(data.decode()).read() #接受和执行结果都是字符串
        if len(cmd_res) ==0:
            cmd_res="cmd has no output"
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))  #注意中文解码成bytes再len统计，否则出现误差
        #time.sleep(0.5) #此方法可以解决粘包问题，这种方法比较low
        client_ack = conn.recv(1024) #接受客户端的回复，解决粘包
        print("client_ack",client_ack.decode())
        conn.send(cmd_res.encode("utf-8"))
        print("send done")
server.close()