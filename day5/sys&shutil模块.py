#coding:utf-8
#Author:Mr Zhi
import sys
print(sys.version)  #获取python解析器版本信息
print(sys.argv) #获取程序本身路径
print(sys.path)  #返回模块的搜索路径，初始化使用pythonpath环境变量的值
print(sys.platform) #返回操作平台的名称

#shutil高级的文件，文件夹，压缩包处理模块
import shutil
shutil.copyfileobj(open('a.txt.py','r'),open('a.py1','w'))  #将文件内容拷贝到另一个文件中
shutil.copyfile('a.py1','a2.py') #拷贝文件
shutil.copymode('a2.py','a.txt.py') #仅拷贝权限。原文件内容，组，用户均不变
shutil.copystat('a3.py','a4.py') #拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copy('a3.py','a4.py') #拷贝文件和权限
shutil.copy2('a3.py','a4.py') #拷贝文件和状态信息
shutil.copytree('a1','a2') #shutil.ignore_patterns(*patterns)递归去拷贝文件（拷贝目录）
shutil.rmtree('a2','a1') #递归删除目录
shutil.move('D:/软件/pycharm/day5/a.py1','D:/软件/pycharm')  #递归的去移动文件
#shutil.make_archive(压缩保存路径，压缩包种类，压缩目标路径)；压缩包种类，“zip”, “tar”, “bztar”，“gztar”
shutil.make_archive('D:/软件/shutil.make_ar','zip','D:/软件/pycharm/day5')
#def _make_tarball(base_name, base_dir, compress="gzip", verbose=0, dry_run=0,owner=None, group=None, logger=None):默认是tar.gz包压缩目录
shutil._make_tarball('D:/软件/shutil.make_ar','D:/软件/pycharm/day5')
#shutil._make_zipfile(base_name, base_dir, verbose=0, dry_run=0, logger=None):默认zip包压缩目录
shutil._make_zipfile('D:/软件/shutil.make_ar','D:/软件/pycharm/day5')

#shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的，详细：
import zipfile
# zip包解压
z = zipfile.ZipFile('D:/软件/shutil.make_ar.zip')  #指定解压包
z.extractall() #解压到指定路径，默认是解压到程序当前路径
z.close()

#压缩zip包
z = zipfile.ZipFile('D:/软件/shutil_shiyan.zip','w') #打开并指定压缩包保存路径(一定得是zip后缀)
z.write('D:/a.txt')  #添加文件或目录到压缩包
z.write('C:/shutil.make_ar.zip')  #添加文件或目录到压缩包
z.write('C:/b') #添加文件或目录到压缩包
z.close()

#tar.gz包解压
import tarfile
gz = tarfile.open('D:/软件/shutil.make_ar.tar.gz') #指定解压包
gz.extractall('D:/软件/py_shiyan') #指定保存路径
gz.close()
#tar.gz包压缩
tar = tarfile.open('D:/软件/shiyan.tar.gz','w') #指定压缩包保存路径
tar.add('D:/a.txt') #添加文件或目录到压缩包
tar.add('C:/shutil.make_ar.zip') #添加文件或目录到压缩包
tar.add('C:/b') #添加文件或目录到压缩包
tar.close()

