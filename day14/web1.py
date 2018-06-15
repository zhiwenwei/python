#-*- coding: utf-8 -*-
#AuthorZhiWenwei
#对于所有的Web应用，本质上其实就是一个socket服务端，用户的浏览器其实就是一个socket客户端。
import socket
def handle_request(client):
    buf = client.recv(1024)
    f = open("body1.html","rb")
    data = f.read()
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding="utf8"))
    client.send(data)
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
if __name__ == '__main__':
    main()