#coding:utf-8
#Author:zhiwenwei
import json
l1 = ["alex", 123, "eric"]
l2 = ["alex", 123, 'eric']
s1 = """ ["alex", 123, "eric"] """
s2 = """ ["alex", 123, 'eric'] """
print(json.dumps(l1))
print(json.dumps(l2))
print(json.loads(s1))
print(json.loads(s2))