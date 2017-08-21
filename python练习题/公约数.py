#coding:utf-8
#Author:Mr Zhi
"""
给你两个正整数a,b,  输出它们公约数的个数。
例如：a = 24， b = 36
则输出：6
"""
#能够整除一个整数的整数称为其的约数（如5是10的约数）,如果一个数既是数A的约数，又是数B的约数，称为A,B的公约数
a = 12
b = 15
count = 0
for i in range(1,min(a,b)+1):
    if a % i ==0 and b % i ==0:
        count +=1
print(count)
