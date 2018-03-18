#!/usr/bin/env python
# _*_coding:utf-8_*_
#Author:ZhiWenwei
import os
import hashlib
import json
import re
import socketserver
import configparser
import subprocess
from conf import settings

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


class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            # print(self.client_address[0])
            if not self.data:
                print("Client closed.")
                break
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                if hasattr(self, "_%s" % data.get('action')):
                    func = getattr(self, "_%s" % data.get('action'))
                    func(data)
                    self.user_tmp_dir = self.get_abs_path()
                    # print("tmp_dir", self.user_tmp_dir)
                else:
                    print("Invalid cmd")
                    self.send_response(251)
            else:
                print("Invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code, data=None):
        '''
        向客户端返回数据
        '''
        response = {'status_code': status_code, 'status_msg': STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)

        user = self.authenticate(data.get("username"), data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print("Passed authentication", user)
            self.user = user
            self.user_home_dir = "{}/{}".format(settings.USER_HOME, self.user["Username"])
            self.send_response(254)

    def authenticate(self, username, password):
        '''
        验证用户合法性，合法就返回用户数据
        '''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("Passed auth.", username)
                config[username]["Username"] = username
                return config[username]

    def get_abs_path(self, *args, **kwargs):
        '''
        获取当前目录绝对路径
        '''
        try:
            if self.user_tmp_dir:
                abs_path = self.user_tmp_dir
        except Exception as e:
            abs_path = self.user_home_dir

        return abs_path

    def _cd(self, *args, **kwargs):
        '''
        切换目录
        '''
        data = args[0]
        if data.get('directory') is None:
            self.send_response(259)

        # 判断绝对路径和相对路径
        if data.get("directory").startswith("/"):
            directory_abs_path = "{}/{}".format(self.user_home_dir, data.get("directory"))
        else:
            directory_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("directory"))
        print("Directory abs path", directory_abs_path)
        if not os.path.exists(directory_abs_path):
            self.send_response(260)
        elif os.path.isfile(directory_abs_path):
            self.send_response(261)
        else:
            access_flag = os.access(directory_abs_path, os.R_OK|os.X_OK)
            if access_flag and directory_abs_path.startswith(self.user_home_dir):
                self.send_response(0)
                os.chdir(directory_abs_path)
                self.user_tmp_dir = os.getcwd()
            else:
                self.send_response(262)

    def _pwd(self, *args, **kwargs):
        '''
        显示当前目录的绝对路径（/表示ftp家目录）
        '''
        abs_path = self.get_abs_path()
        if abs_path:
            relative_path = re.sub(self.user_home_dir,"", abs_path + "/", count=1)
            self.request.sendall(relative_path.encode())
        else:
            self.send_response(263)


    def _get(self, *args, **kwargs):
        '''
        客户端下载文件
        '''
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
        # 判断绝对路径和相对路径
        if data.get("filename").startswith("/"):
            file_abs_path = "{}/{}".format(self.user_home_dir, data.get("filename"))
        else:
            file_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("filename"))
        # print("File abs path", file_abs_path)
        if os.path.isfile(file_abs_path):
            print("---- ready to send file ----")
            file_obj = open(file_abs_path, "rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257, data={'file_size': file_size})
            self.request.recv(1)  # 等待客户端确认

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.request.recv(1)  # 等待客户端确认
                    self.send_response(258, {'md5': md5_val})
                    print("Send file done.")
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("Send file done.")
        else:
            self.send_response(256)

    def _ls(self, *args, **kwargs):
        '''
        显示当前目录下的文件和目录
        '''
        data = args[0]
        # 判断绝对路径和相对路径
        if data.get("filename"):
            if data.get("filename").startswith("/"):
                file_abs_path = "{}/{}".format(self.user_home_dir, data.get("filename"))
            else:
                file_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("filename"))
        else:
            file_abs_path = self.user_tmp_dir

        if os.path.exists(file_abs_path):
            if os.path.isfile(file_abs_path):  # 如果是文件的情况下，进行路径，再ls，避免输出服务端绝对路径
                # old_dir = self.user_tmp_dir
                os.chdir(os.path.dirname(file_abs_path))
                file_abs_path = os.path.basename(file_abs_path)
            result = os.popen("ls -l {}".format(file_abs_path))
            result_content = result.read().encode()
            os.chdir(os.path.dirname(self.user_tmp_dir))
        else:
            result_content = STATUS_CODE[260].encode()
        result_lenth = len(result_content)
        self.send_response(264, data={'lenth_size': result_lenth})
        self.request.recv(1)  # 等待客户端确认
        self.request.sendall(result_content)

    def _put(self, *args, **kwargs):
        '''
        客户端上传文件       
        '''
        data = args[0]
        file_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("filename"))

        # print(self.user)

        self.send_response(266)
        file_size = json.loads(self.request.recv(1024).decode())
        if file_size:  # 客户端准备传输文件
            self.request.send(b'1')
            received_size = 0
            file_obj = open(file_abs_path, "wb")
            if data.get('md5'):
                md5_obj = hashlib.md5()
                while received_size < file_size["file_size"]:
                    data = self.request.recv(4096)
                    received_size += len(data)
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    print("---- file received ----")
                    file_obj.close()
                    self.request.send(b'1')  # 解决粘包
                    md5_val = md5_obj.hexdigest()
                    md5_from_client = json.loads(self.request.recv(1024).decode())
                    if md5_from_client['md5'] == md5_val:
                        self.send_response(267)
                    else:
                        self.send_response(268)
            else:
                while received_size < file_size["file_size"]:
                    data = self.request.recv(4096)
                    received_size += len(data)
                    file_obj.write(data)

    def _rm(self, *args, **kwargs):
        '''
        删除文件或者目录
        '''
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
        # 判断绝对路径和相对路径
        if data.get("filename").startswith("/"):
            file_abs_path = "{}/{}".format(self.user_home_dir, data.get("filename"))
        else:
            file_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("filename"))
        if os.path.isfile(file_abs_path):
            print("---- ready to remove file ----")
            result = subprocess.Popen(["rm","-f",file_abs_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            error_log = result.stderr.read()
            if error_log:  # 有提示输出时
                self.send_response(270, data={'error_log': error_log.decode()})
            else:
                self.send_response(0)
        else:
            self.send_response(271)

    def _rmdir(self, *args, **kwargs):
        '''
        删除文件或者目录
        '''
        data = args[0]
        if data.get('dirname') is None:
            self.send_response(255)
        # 判断绝对路径和相对路径
        if data.get("dirname").startswith("/"):
            dir_abs_path = "{}/{}".format(self.user_home_dir, data.get("dirname"))
        else:
            dir_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("dirname"))
        if os.path.isdir(dir_abs_path):
            print("---- ready to remove directory ----")
            result = subprocess.Popen(["rmdir",dir_abs_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            error_log = result.stderr.read()
            if error_log:  # 有提示输出时
                self.send_response(276, data={'error_log': error_log.decode()})
            else:
                self.send_response(0)
        else:
            self.send_response(277)

    def _mkdir(self, *args, **kwargs):
        '''
        创建目录
        '''
        data = args[0]
        if data.get('dirname') is None:
            self.send_response(272)
        # 判断绝对路径和相对路径
        if data.get("dirname").startswith("/"):
            dir_abs_path = "{}/{}".format(self.user_home_dir, data.get("dirname"))
        else:
            dir_abs_path = "{}/{}".format(self.user_tmp_dir, data.get("dirname"))
        if not os.path.exists(dir_abs_path):
            print("---- ready to create directory ----")
            result = subprocess.Popen(["mkdir","-p",dir_abs_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            error_log = result.stderr.read()
            if error_log:  # 有提示输出时
                self.send_response(273, data={'error_log': error_log.decode()})
            else:
                self.send_response(0)
        else:
            self.send_response(275)
