#coding:utf-8
#Author:Mr Zhi
"""
抓不住爱情的我 总是眼睁睁看它溜走 ...现在来练习一下发现爱的能力，给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。
例如：a = "OurWorldIsFullOfLOVE"
则输出：LOVE
"""
a = "OurWorldIsFullOfLOV"
if 'LOVE' in a.upper():  #小写a.lower()
    print("LOVE")
else:
    print("SINGLE")