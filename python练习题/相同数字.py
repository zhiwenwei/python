#coding:utf-8
#Author:Mr Zhi
"""
给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
"""
l = [1,45,56,654,6544,2,45]
if len(set(l)) < len(l):
    print("yes")
else:
    print("no")