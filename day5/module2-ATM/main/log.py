#coding:utf-8
#Author:Mr Zhi
#很多程序都有记录日志的需求，并且日志中包含的信息即有正常的程序访问日志，还可能有错误、警告等信息输出，python的logging模块提供了标准的日志接口，
# 你可以通过它存储各种格式的日志，logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别，下面我们看一下怎么用。
import logging,os
# logging.basicConfig(filename='app.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
# logging.info('test info')
# logging.debug('test debug')
# logging.warning('test warning')
# logging.error('test error')
# logging.critical('test critical')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = BASE_DIR + '/log/record.log'
print(log_dir)
def get_logger():
    fh = logging.FileHandler(log_dir)
    logger = logging.getLogger() #获得一个logger对象，默认是root
    logger.setLevel(logging.DEBUG)
    fm = logging.Formatter("%(asctime)s --- %(message)s")
    logger.addHandler(fh)
    fh.setFormatter(fm)
    return logger
get_logger()