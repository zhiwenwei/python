#coding:utf-8
#Author:Mr Zhi
# 5 写代码计算1*2+3*4+5*6+7*8...+99*100
#规律：100以内从1开始相邻的一个奇数和一个偶数乘机之和，可以迭代出100以内奇数i再得出偶数i+1，再进行积的累加
sum =0 #定义sum初始值为0
for i in range(1,100,2): #迭代100以内的奇数
    sum += i*(i+1) #累加i * (i+1)，也就是第一次是sum = 0 + 1*(1+1),第二次sum = 2 + 3(3+1)，以此类推
print(sum) #打印出sum值

# 4 写代码实现99乘法表（格式化输出）
#规律：第一行有一列的积，第二行有两列的积...第九行有九列的积,行数是行数以内数字相乘，比如第五行就是每列以5开头分别乘一个5以内的数字
for i in range(1,10):#迭代1到10内的整数
    for j in range(1,i+1):#迭代行数内的数字作为第二个因数
        print("%d*%d=%2d" % (i,j,i*j),end=' ') #end=' '意思是末尾不换行，在最后值后面加一个空格,%2d宽度是2，不满二位左边补一个空格，这样可以统一对齐！
    print(" ")#每次迭代玩j之后print一个空格隔开每行
