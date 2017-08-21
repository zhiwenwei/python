#coding:utf-8
#Author:Mr Zhi
#排列组合,将4个数字可能组成的所有互不相同且无重复数字的排列组合列出。
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k) and (i != j) and (j != k ):
                print(i,j,k)
import fileinput
