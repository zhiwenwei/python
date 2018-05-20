#-*- coding: utf-8 -*-
#AuthorZhiWenwei
from urllib import request
import gevent
import time
from gevent import monkey
monkey.patch_all()#把当前程序所有的io操作做上单独标记
def f(url):
    print('get:%s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("url.html","wb")
    f.write(data)
    f.close()
    print('%d bytes received from %s'%(len(data),data))

urls = ['http://www.cnblogs.com/wenwei-blog/p/8890436.html',
       'https://www.google.la/',
       'https://www.python.org',
        'https://github.com/',
        'http://edu.51cto.com/',
       ]
time_start = time.time()
for url in urls:
    f(url)
print("同步cost",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,'http://www.cnblogs.com/wenwei-blog/p/8890436.html'),
    gevent.spawn(f,'https://www.google.la/'),
    gevent.spawn(f,'https://www.python.org'),
    gevent.spawn(f,'https://github.com/'),
    gevent.spawn(f,'http://edu.51cto.com/'),
 ])
print("异步cost",time.time() - async_time_start)
