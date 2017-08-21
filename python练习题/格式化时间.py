#coding:utf-8
#Author:Mr Zhi
t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}

#%s是字符串，%d是digit整数，%f是浮点数，%02d是表示输出不小于两位数，不足两位前面填充0，%04d是表示四位
print("%04d-%02d-%02d %02d:%02d:%02d" %(int(t['year']),int(t['month']),int(t['day']),int(t['hour']),int(t['minute']),int(t['second'])))