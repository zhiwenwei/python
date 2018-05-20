#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import os,sys
base_dir = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
sys.path.insert(0,base_dir)
from ceshi1 import zhiww1
zhiww1.test1()
print(zhiww1.port)