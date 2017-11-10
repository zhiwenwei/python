#-*- coding:utf-8 -*-
#Author:Kevin
import shelve
f = shelve.open("shelve_test.db")
f.update({'k1':'v1','k2':'v2'})
f['k3'] = "v3"
for i in f.keys():
    print(i)
f.close()