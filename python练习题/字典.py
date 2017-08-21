#coding:utf-8
#Author:Mr Zhi
#给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。

#例如：a={1:1,2:2,3:3}, 则输出：1,2,3
a={1:1,2:2,3:3}
print(sorted(map(str,a.keys())))
print(','.join(sorted(map(str,a.keys()))))
