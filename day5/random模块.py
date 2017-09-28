#coding:utf-8
#Author:Mr Zhi
"""
random模块生成随机数
"""
import random
print(random.random())#生成0到1的随机浮点数

print(random.uniform(100,200)) #生成指定范围内的随机浮点数

print(random.randint(100,105)) #生成指定范围内的整数

print(random.randrange(0,100,2)) #从指定范围内，按指定基础递增的集合中，获取一个随机数

#五位纯数字验证码
a = ''
for i in range(5):
    current = random.randint(1,9)
    a += str(current)
print(a)

"""
通过查找ASCII码表可以知道：
大写字母ASCII值范围：65~90
小写字母ASCII值范围：97~122
"""
#数字和字母组合验证码
tmp = ''
for i in range(6):
    current2 = random.randrange(0,6)
    if current2 == i:
        b = chr(random.randint(97,122))
    else:
        b = random.randrange(0,9)
    tmp += str(b)
print(tmp)