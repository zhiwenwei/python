#-*- coding:utf-8 -*-
#Author:ZhiWenwei
import socketserver
class MyTCPHandle(socketserver.BaseRequestHandler):
    def handle(self): #接受处理客户端的请求
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote".format(self.client_address[0]))
                print(self.data)
                # if not self.data: #客户端断了
                #     print(self.client_address,"断开了")
                #     break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break

if __name__ == "__main__":
    HOST,PORT = "localhost",9999
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandle)
    server.serve_forever()
