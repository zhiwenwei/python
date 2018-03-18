#!/usr/bin/env python
# _*_coding:utf-8_*_
#Author:ZhiWenwei
import socket
import os
import json
import optparse
import sys
import hashlib

STATUS_CODE = {
    0: "success",
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename doesn't provided",
    256: "File doesn't exist on server",
    257: "Ready to send file",
    258: "Md5 verification",
    259: "Directory doesn't provided",
    260: "No such file or directory",
    261: "Not a directory",
    262: "Permission denied",
    263: "Print working directory error",
    264: "Ready to send data",
    265: "Put: overwrite",
    266: "Ready to receive file",
    267: "The file is consistent",
    268: "The file is not consistent",
    270: "Remove file error",
    271: "It is not a file",
    272: "Filename doesn't provided",
    273: "Create directory error",
    275: "File or directory exists",
    276: "Remove directory error",
    277: "Directory not exists",

}


class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp ip address")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-p", "--password", dest="password", help="password")
        self.options, self.args = parser.parse_args()
        self.verify_args(self.options, self.args)
        self.make_connection()

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server, self.options.port))

    def verify_args(self, options, args):
        '''
        校验参数合法性
        '''
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            exit("Err: username and password must be provided together.")

        if options.server and options.port:
            if options.port > 0 and options.port < 65535:
                return True
            else:
                exit("Err: host port must be in 0-65535")

    def authenticate(self):
        if self.options.username:
            result = self.get_auth_result(self.options.username, self.options.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username: ").strip()
                password = input("password: ").strip()
                result = self.get_auth_result(username, password)
        return result

    def get_auth_result(self, user, password):
        data = {'action': 'auth',
                'username': user,
                'password': password
                }
        self.sock.send(json.dumps(data).encode())
        response = self.get_response()
        if response.get('status_code') == 254:
            print("Passed authentication!")
            self.user = user
            return True
        else:
            print(response.get("status_msg"))

    def get_response(self):
        '''
        得到服务器端回复结果
        '''
        data = self.sock.recv(1024)
        if data:
            data = json.loads(data.decode())
        else:
            data = "No data"
        return data

    def interactive(self):
        if self.authenticate():
            print("---- start interactive with you ----")
            while True:
                choice = input("[%s]: " % self.user).strip()
                if len(choice) == 0: continue
                cmd_list = choice.split()
                if hasattr(self, "_{}".format(cmd_list[0])):
                    func = getattr(self, "_{}".format(cmd_list[0]))
                    func(cmd_list)
                else:
                    print("Invalid cmd.")

    def __md5_required(self, cmd_list):
        '''
        检测命令是否需要进行md5验证
        '''
        if '--md5' in cmd_list:
            return True

    def show_progress(self, total):
        '''
        显示进度条
        '''
        received_size = 0
        current_percent = 0
        show_count = 5  # 中间显示进度百分比次数
        while received_size < total:
            received_pecent = int((received_size / total) * 100)
            remainder = received_pecent % (100 / show_count)
            if received_pecent > current_percent:
                print("#", end="", flush=True)
                if remainder == 0:
                    print("[{:2}%]".format(received_pecent))
            current_percent = int((received_size / total) * 100)
            new_size = yield
            received_size += new_size

    def get_abs_path(self, *args, **kwargs):
        '''
        获取当前目录绝对路径
        '''
        abs_path = os.getcwd()
        return abs_path


    def _get(self, cmd_list):
        if len(cmd_list) == 1:  # 需要接文件名
            print("No filename follows.")
            return

        data_header = {
            'action': 'get',
            'filename': cmd_list[1]
        }

        if self.__md5_required(cmd_list):
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        if response["status_code"] == 257:  # 接收传输文件信息
            self.sock.send(b'1')
            base_filename = cmd_list[1].split('/')[-1]
            received_size = 0
            file_obj = open(base_filename, "wb")
            if self.__md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response['file_size'])  # generator
                progress.__next__()
                while received_size < response["file_size"]:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print("#[100%]")
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    print("---- file received ----")
                    file_obj.close()
                    self.sock.send(b'1')
                    md5_val = md5_obj.hexdigest()
                    md5_from_server = self.get_response()
                    if md5_from_server['status_code'] == 258:
                        if md5_from_server['md5'] == md5_val:
                            print("[%s] %s!" % (base_filename, STATUS_CODE[267]))
                        else:
                            print("[%s] %s!" % (base_filename, STATUS_CODE[268]))
            else:
                progress = self.show_progress(response['file_size'])  # generator
                progress.__next__()
                while received_size < response["file_size"]:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    file_obj.write(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print("#[100%]")

                else:
                    print("---- file received ----")
                    file_obj.close()
        else:
            print(response['status_msg'])

    def _cd(self, cmd_list):
        '''
        切换目录
        '''
        if len(cmd_list) == 1:
            print(STATUS_CODE[259])
            return

        data_header = {
            'action': 'cd',
            'directory': cmd_list[1]
        }

        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print(response['status_msg'])

    def _pwd(self, cmd_list):
        '''
        获取当前目录路径
        '''
        data_header = {
            'action': 'pwd',
        }
        self.sock.send(json.dumps(data_header).encode())
        buffer = self.sock.recv(4096)
        if buffer:
            print(buffer.decode("utf-8"))

    def _ls(self, cmd_list):
        '''
        获取当前目录下的目录和文件
        '''
        if len(cmd_list) == 1:
            filename = ""
        else:
            filename = cmd_list[1]

        data_header = {
            'action': 'ls',
            'filename': filename
        }
        self.sock.send(json.dumps(data_header).encode())

        response = self.get_response()
        if response["status_code"] == 264:  # 传输数据
            self.sock.send(b'1')

        received_msg = b""
        received_size = 0
        while received_size < response["lenth_size"]:
            received_data = self.sock.recv(1024)
            received_msg += received_data
            received_size += len(received_data)

        print(str(received_msg, encoding='utf-8'))

        return True

    def _put(self, cmd_list):
        '''
        客户端上传文件
        '''
        if len(cmd_list) == 1:  # 需要接文件名
            print("No filename follows.")
            return

        # 判断上传文件绝对路径或相对路径
        abs_path = self.get_abs_path()
        if cmd_list[1].startswith("/"):
            file_abs_path = cmd_list[1]
        else:
            file_abs_path = "{}/{}".format(abs_path, cmd_list[1])
        print("File abs path", file_abs_path)

        # 文件不存在时
        if not os.path.isfile(file_abs_path):
            print(STATUS_CODE[260])
            return

        # 提取文件名
        base_filename = cmd_list[1].split('/')[-1]

        data_header = {
            'action': 'put',
            'filename': base_filename
        }

        # 是否md5验证
        if self.__md5_required(cmd_list):
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()

        if response["status_code"] == 266:  # 服务端准备接收文件
            print("---- ready to send file ----")
            file_obj = open(file_abs_path, "rb")
            file_size = os.path.getsize(file_abs_path)
            self.sock.send(json.dumps({'file_size': file_size}).encode())
            self.sock.recv(1)  # 等待客户端确认

            if data_header.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.sock.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    self.sock.recv(1)  # 解决粘包
                    print(STATUS_CODE[258])
                    md5_val = md5_obj.hexdigest()
                    self.sock.send(json.dumps({'md5': md5_val}).encode())
                    md5_response = self.get_response()
                    if md5_response['status_code'] == 267:
                        print("[%s] %s!" % (base_filename, STATUS_CODE[267]))
                    else:
                        print("[%s] %s!" % (base_filename, STATUS_CODE[268]))
                    print("Send file done.")
            else:
                for line in file_obj:
                    self.sock.send(line)
                else:
                    file_obj.close()
                    print("Send file done.")
        else:
            print(STATUS_CODE[256])

    def _rm(self, cmd_list):
        '''
        删除文件
        '''
        if len(cmd_list) == 1:  # 需要接文件名
            print("No filename follows.")
            return

        data_header = {
            'action': 'rm',
            'filename': cmd_list[1]
        }
        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        if response["status_code"] == 270:  # 接收到了错误日志，打印出来
            print("[{}] {}".format(response['status_msg'], response['error_log']))
        else:
            print(response['status_msg'])

    def _rmdir(self, cmd_list):
        '''
        删除目录
        '''
        if len(cmd_list) == 1:  # 需要接文件名
            print("No dirname follows.")
            return

        data_header = {
            'action': 'rmdir',
            'dirname': cmd_list[1]
        }
        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        if response["status_code"] == 276:  # 接收到了错误日志，打印出来
            print("[{}] {}".format(response['status_msg'], response['error_log']))
        else:
            print(response['status_msg'])

    def _mkdir(self, cmd_list):
        '''
        创建目录
        '''
        if len(cmd_list) == 1:  # 需要接目录名
            print("No directory name follows.")
            return

        data_header = {
            'action': 'mkdir',
            'dirname': cmd_list[1]
        }
        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        if response["status_code"] == 273:  # 接收到了错误日志，打印出来
            print("[{}] {}".format(response['status_msg'], response['error_log']))
        else:
            print(response['status_msg'])

    def _help(self, cmd_list):
        '''
        打印帮助信息
        '''
        print('''
        (commands)
        cd <dir>         ls <dir|file>        get <file>
        mkdir <dir>      put <file>           pwd
        rm <file>        rmdir <dir>      
        ''')

    def _quit(self, cmd_list):
        '''
        退出客户端
        '''
        print(cmd_list)
        if cmd_list[0] == "quit":
            exit("---- Bye ----")

if __name__ == "__main__":
    ftp = FTPClient()
    ftp.interactive()
