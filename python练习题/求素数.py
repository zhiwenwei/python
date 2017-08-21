#coding:utf-8
#Author:Mr Zhi
#输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
#素数也叫质数，除了能被1和自己本身整数整除的数，0和1非质数也非合数，最小素数是2

i =1
l = []
while (i < 100):
    i +=1
    for a in range(2,i):
        if i % a == 0:
            break
    else:
        l.append(i)
print(' '.join(map(str,l)))
