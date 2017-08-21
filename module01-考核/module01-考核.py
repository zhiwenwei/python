
#1. Python脚本的头部 #!/usr/bin/env python 作用？和#!/usr/bin/python有什么区别
   调用环境变量的python解析器；#!/usr/bin/python是调用/usr/bin/python解析器，如果安装的python没有指定在改目录下就不能成功调用，也就是说是死的，
   #!/usr/bin/env python比较灵活，不管你安装python在哪个目录下，只要python在环境变量中就可以！
2. 简述字节、位、比特的关系？
     位只有两种形式0和1，而字节是有8个位组成的。可以表示256个状态。
      1字节(b)=8比特(bit)
      位 = 比特

3.简述ascii、unicode、utf - 8、gbk，gb2312的关系？
   ascii是最早的一套计算机编码系统，最多只能表示255个符号；
   unicode是解决传统的编码局限而产生的一套可以足够编码全世界语言的统一码/万国码
    utf-8是全国使用的编码，是对Unicode编码的压缩和优化
    gbk是中国规定的汉字编码，gbk是gb2312的扩展版本
    gb2312是中国规定的汉字编码

4.变量名命名规范
  大小写字母，单词之间用_分割 

5. 简述全局变量和局部变量
   定义在函数内的变量就是局部变量，定义在函数外的变量就是全局变量，global语句声明局部变量是全局变量
6.有如下字符串：n = "老男孩",将字符串转换成utf-8的字节,再将转换的字节重新转换为gbk的字符串
    python3字符串转换成utf-8的字节：print(n.encode("utf-8")) 
8. 写代码：
    使用while循环实现输出 1-100 内的所有奇数
9将列表['alex', 'eric', 'rain'] 中的每一个元素使用 "_" 连接为一个字符串
    a = ['alex', 'eric', 'rain']
    print('_'.join(a))

10. 字典key都可以是什么类型？列表不可变   bcd
        A.列表    B.字典   C.字符串  D.数字
        11.利用 filter、自定义函数 获取l1中元素大于33的所有元素 l1 = [11, 22, 33, 44, 55]
"""
# i = 1
# while  0 < i <= 101:
#     if i % 2 != 1:
#         print(i)
#
#将n转换成utf-8的字节,再将转换的字节重新转换为gbk的字符串
# import sys
# print(sys.getdefaultencoding())
# n = "中文"
# n_utf8 = n.encode("utf-8")   #python3默认是unicode编码，直接encode编码成utf-8就可以
# print(n_utf8,type(n_utf8))
# n_gbk = n_utf8.decode("utf-8").encode("gbk").decode("gbk") #解码成unicode再编码成gbk最后解码成gbk的字符串
# print(n_gbk,type(n_gbk))
import sys
print(sys.getdefaultencoding())
n = "我爱python"
bytes_utf8 = n.encode("utf-8")  #python3默认是unicode编码，直接把n字符串编码成utf-8字节
str_utf8 = bytes_utf8.decode("utf-8") #把utf8字节转换成字符串
str_gbk = bytes_utf8.decode("utf-8").encode("gbk").decode("gbk")
print(bytes_utf8,str_utf8,str_gbk)