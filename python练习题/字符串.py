#coding:utf-8
#Author:Mr Zhi#
"""给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。

例如：a=‘xyzwd’

则输出:xzd"""
a = 'xyzwd'
l = []
for i in range(len(a)):
    if i % 2 ==0:
        l.append(a[i])
print(''.join(l))
