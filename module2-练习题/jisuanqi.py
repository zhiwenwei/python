#coding:utf-8
#Author:zhiwenwei
import re

# 去掉重复运算,和处理特列+－符号
def del_double(str):
  str = str.replace("++", "+")
  str = str.replace("--", "-")
  str = str.replace("+-","-")
  str = str.replace("- -","-")
  str = str.replace("+ +","+")
  return str
def shengchu(str):
  calc = re.split("[*/]",str)   #用＊/分割公式
  OP = re.findall("[*/]",str)  #找出所有＊和／号
  ret = None
  for index,i in enumerate(calc):
    if ret:
      if OP[index-1] == "*":
        ret *= float(i)
      elif OP[index-1] == "/":
        ret /= float(i)
    else:
      ret = float(i)
  return ret

def jiajian(str):
  calc = re.split("[+-]",str)   #用＊/分割公式
  OP = re.findall("[+-]",str)  #找出所有＊和／号
  ret = None
  for index,i in enumerate(calc):
    if ret:
      if OP[index-1] == "+":
        ret += float(i)
      elif OP[index-1] == "-":
        ret -= float(i)
    else:
      ret = float(i)
  return ret
def calc(str):
    res = jiajian(shengchu(str))
    return res
while True:
    input_str=input(">>>:")
    input_str = del_double(input_str)
    result = calc(input_str)
    print(result)