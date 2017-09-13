#coding:utf-8
#Author:zhiwenwei
import re
str = 'jklodsudinmreiruksdjhfjdfhjk'
a = re.findall('jk*',str)
print(a)
sear = re.search('j*',str).group()
print(sear)
sub_str = re.sub("jk","zhiwenwei",str)
print(sub_str)
# def calc(num):
#     print(num)
#     return num
# num = input(">>>")
# calc(num)
def jkl(sum):
    print(sum+12)
a = jkl(9)
print(a)