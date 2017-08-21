#coding:utf-8
#Author:Mr Zhi
#实现不同目录间模块相互调用
import os,sys
print(__file__)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR) #把路径添加到环境变量中
from conf import settings #调用conf目录下的settings
settings.logging() #引用settings的函数logging