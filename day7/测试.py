#coding:utf-8
#Author:zhiwenwei
def person(name,age,sex,job):
    data = {'name':name,'age':age,'sex':sex}
    return data
d = person('zww','f','12','it')
print(d['name'])