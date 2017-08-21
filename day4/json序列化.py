#coding:utf-8
#Author:Mr Zhi

"""
什么叫序列化？
序列化就是把一个对象的形态改变一下，使他能够存放在文件中，或者在网络上传输，序列化也叫持久化，是把对象存储到永久介质中，这样就不会因为掉电而丢失

"""
import json
data = [{'k1':1,'k2':2,'k3':3}]
js = json.dumps(data)
print(js,type(js))
data2 = {'k1':1,'k2':2,'k3':3}
js2 = json.dumps(data2)
print(js2,type(js2))

# f = open('json.txt','w',encoding='utf-8')
# info = {'name':'zww','age':'25'}
# f.write(json.dumps(info)) #把数据写进去
# f.close()


#dump功能：将数据通过特殊的形式转换为所有程序语言都认识的字符串，并写入文件
with open('json.txt','w') as f:
    json.dump(data,f)
data = {'name':'JieSen','height':175,'weight':'68KG'}
#dumps到字符串
json_str = json.dumps(data)
print('dumps到字符串:'json_str,'类型:'type(json_str))
#loads回来
json_dict = json.loads(json_str)
print('loads回来:'json_dict,'类型:'type(json_dict))
