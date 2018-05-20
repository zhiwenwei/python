#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import redis
r = redis.Redis(host='192.168.10.128',port=6379)
r.set('name','xiaogang')
print(r.get('name'))