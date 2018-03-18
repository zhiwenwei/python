程序名称：简单FTP
作者：支文伟

2.需求
 用户登陆
 上传/下载文件
 不同用户家目录不同
 查看当前目录下文件
 充分使用面向对象知识

3.本次作业实现的需求：都实现了作业的基本要求

4.程序运行环境:pycharm 2017.1.2     python解释器版本：Python3.5

5.程序结构
Easy_FTP/
├── client
│   ├── ftp_client.py         #客户端执行程序
│   └── __init__.py
├── README
└── server
    ├── bin
    │   ├── ftp_server.py   #服务端执行程序
    │   └── __init__.py
    ├── conf
    │   ├── accounts.cfg   #用户和密码配置文件
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   └── settings.cpython-35.pyc
    │   └── settings.py
    ├── core
    │   ├── ftp_server.py   #服务端主要程序
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── main.py      #服务端主要程序
    │   ├── main.pyc
    │   └── __pycache__
    │       ├── ftp_server.cpython-35.pyc
    │       ├── __init__.cpython-35.pyc
    │       └── main.cpython-35.pyc
    ├── home             #用户家目录
    │   ├── __init__.py
    │   ├── jack
    │   │   └── __init__.py
    │   └── zww
    │       ├── dingwei.pdf
    │       ├── -p
    │       └── test
    └── __init__.py

7.运行测试:

    运行客户端：python3 Easy_FTP/server/bin/ftp_server.py start
    运行服务端：python3 Easy_FTP/client/ftp_client.py -uzww -p123 -slocalhost -P9999
    详情请看pnd图片
