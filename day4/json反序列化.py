#coding:utf-8
#Author:Mr Zhi
#反序列化就是把数据加载回来
import json
f = open("json.txt",'r')
data = json.loads(f.read())  #加载数据
print(data['name'])