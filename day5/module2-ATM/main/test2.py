#coding:utf-8
#Author:Mr Zhi
from log import get_logger
logger = get_logger()
user,passwd = "zww","123"
username = input("input your name:").strip()
password = input("input your passwd:").strip()
if username == user and password == passwd:
    print("welcome....")
    logger.debug(username)
else:
    logger.debug(password)