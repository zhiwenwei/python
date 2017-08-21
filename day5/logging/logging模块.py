#coding:utf-8
#Author:Mr Zhi
#很多程序都有记录日志的需求，并且日志中包含的信息即有正常的程序访问日志，还可能有错误、警告等信息输出，python的logging模块提供了标准的日志接口，
# 你可以通过它存储各种格式的日志，logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别，下面我们看一下怎么用。
import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
logging.info('test info')
logging.debug('test debug')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')

