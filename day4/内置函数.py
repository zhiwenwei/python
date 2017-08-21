#coding:utf-8
#Author:Mr Zhi
#all(iterable)  如果迭代的所有元素都是True(或者迭代是空的)，返回True
print(all([0,-5,45]))
print(all([1,-5,45,'df','问']))

#any(iterable) 如果迭代的任意元素为真则返回True
print(any([0,12,-3]))
print(any([0]))

#bytearray(str,encoding="utf-8") #返回一个新的字节数组
a = bytearray('abcd',encoding="utf-8")
print(a[0],type(a))

#bytes(source,encoding) 返回一个新的字节对象
a=bytes('在',encoding="utf-8")
print(a,type(a))

#callable(object) 判断可否被调用
def test():
    pass
print(callable(test))

#chr(i) 返回字符串，表示Unicode代码点是整数i的字符。这是ord()的逆。
print(chr(98),ord('b'))

#dir() 查某个变量，字典，函数等操作用法以及属性
x = {'k1':'zww'}
print(dir(x))
import sys
print(dir(sys))

#divmod  将两个(非复数)数作为参数，并返回一对由它们的商和余数组成的数字。使用混合操作数类型，可以应用二进制算术运算符的规则。对于整数，结果与(a//b，a%b)相同
print(divmod(17,2))

#enumerate(iterable,start=0)返回一个枚举对象。迭代必须是一个序列，一个迭代器，或者其他支持迭代的对象。由枚举()返回的迭代器的next()方法返回一个包含计数(从开始到0)的元组，以及从遍历迭代中获得的值。
l1 = ['apple','bike','books','a']
print(list(enumerate(l1)),enumerate(l1))

#filter(function,iterable)  filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
print(list(filter(lambda n:n>3,range(10))))

#eval() 将字符串str当成有效的表达式来求值并返回计算结果
#可以把list，tuple，dict和string相互转换
a  = "[3,'aaaa',{'k1':'dsd'}]"
print(eval(a),type(eval(a)))  #字符串装换成列表
b = "{'k1':'zww','k2':'zhiwenwei'}" #字符串转换成字典
print(eval(b),type(eval(b)))
c = "('dsd',1234,[1,34,'zww'])" #字符串转换成元组
print(eval(c),type(eval(c)))

# hex(x) 将一个整数数字转换为前缀为“0x”的小写十六进制字符串
print(hex(255),hex(3))

#oct() 将一个整数转换为一个八进制字符串

#round(number，ndigits) 以四舍五入返回一个数，在小数点后返回n位数
print(round(35),round(35.54444444),round(34.567,2))\


#字典items()方法：语法：dict.items()函数以列表返回可遍历的（键，值）的元组数组


#sorted() 排序
k = {34:534,1:45,0:4,-100:56,4:1}
print(sorted(k)) #排序key
print(sorted(k.items())) #以列表形式返回排序key的可遍历的（键，值）
print(sorted(k.items(),key=lambda x:x[1])) #以value排序

#zip(*iterable) 创建一个迭代器，它从每个迭代器中聚合元素
a = [21323,2,3,21313213]
b = (9000,99,111,4,54,565,7777)
for i in zip(a,b):
    print(i)

#__import__(module) 相当import module




