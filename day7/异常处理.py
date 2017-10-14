#coding:utf-8
#Author:zhiwenwei
name = ['djk',123]


class LiziException(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise LiziException('我的异常')
except LiziException as e:
    print(e)
