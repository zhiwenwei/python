#coding:utf-8
#Author:Mr Zhi
import logging,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取上级目录的绝对路径
log_dir = BASE_DIR + '/log/record.log'
def get_logger():
    fh = logging.FileHandler(log_dir) #创建一个文件流
    logger = logging.getLogger() #获得一个logger对象，默认是root
    logger.setLevel(logging.DEBUG)  #设置最低等级debug
    fm = logging.Formatter("%(asctime)s --- %(message)s")  #设置日志格式
    logger.addHandler(fh) #把文件流添加进来，流向写入到文件
    fh.setFormatter(fm) #把文件流添加写入格式
    return logger