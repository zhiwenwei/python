#coding:utf-8
#Author:Mr Zhi
#生成器：只有在调用时才会生成相应的数据,只记录当前位置，只有一个__next__()方法
#列表生成式：
l = [i * 2 for i in range(10)]
print(l)

#生成器：
c = (i*2 for i in range(100))
#print(c.__next__)  每次调用一个元素，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
for a in c:
    print(a)

#经过测试生成器和列表生成器，两者占用cpu和运行速度不差上下，但是生成器只占用4g内存的0.3%，列表生成式占2.4%

#迭代器：（list，tuple，dict，set，generator等）直接作用于for循环的对象统称为可迭代对象Iterable，可以使用isinstance()判断判断一个对象是否是Iterable对象
from collections import Iterable
print(isinstance({},Iterable))
print(isinstance('fdsffdsf',Iterable))
print(isinstance(100,Iterable))
#生成器都是Iterator对象，但list，tuple，str虽然是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象，因为python的Itertor表示的是一个数据流，可以被next
#小结：凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数都是Itertor