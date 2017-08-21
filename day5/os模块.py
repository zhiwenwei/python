#coding:utf-8
#Author:Mr Zhi
import os
print(os.getcwd()) #获取当前工作目录
print(os.listdir()) #列出当前所有的目录和文件
os.remove() #删除文件
os.stat() #获得文件或目录属性
os.chmod() #修改文件权限和时间戳
os.mkdir() #创建目录
os.rmdir()  #删除目录
os.removedirs() #删除多个目录
os.system() #运行shell命令
os.path.split() #返回一个路径的目录和文件名
os.path.isfile() && os.path.isdir() #判断一个路径是文件或目录
os.path.exists() #判断一个路径是否存在
os.curdir #返回当前目录('.')
os.chdir() #切换目录
os.path.getsize() #获得文件大小，如果是目录返回4096字节
os.path.abspath() #获得绝对路径
os.path.isabs()  #判断是否绝对路径
os.path.join(path,name) #连接目录与文件名或目录
os.path.basename() #返回文件名
os.path.dirname()  #返回目录
os.popen()
