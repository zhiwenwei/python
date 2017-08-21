#coding:utf-8
#Author:Mr Zhi
#使用while循环实现输出1 - 2 + 3 - 4 + 5 ... - 100 的和
#偶数和减去奇数和就可以得出答案
i = 0
l1 = [] #所有偶数加到这个列表
l2 = [] #所有奇数加到这个列表
while (i < 100):
    i += 1
    if i % 2 == 0:
        l1.append(i)
    if i % 2 == 1:
        l2.append(i)
sum1 = 0
sum2 = 0
for b in l1:
    sum1 += b
print(sum)
for c in l2:
    sum2 += c
sum = sum1 - sum2 #偶数和减去奇数和
print(sum)