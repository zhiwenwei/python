#coding:utf-8
#Author:Mr Zhi
"""
模拟计算器开发：
实现加减乘除及拓号优先级解析
用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，
结果必须与真实的计算器所得出的结果一致
"""
# -*-coding:utf8-*-
import re
'''乘除运算函数'''
def multiply_divide(num):
    while re.search("-?\d+\.?\d*[\*\/]-?\d+\.?\d*",num): #当有*/运算时循环
        ret = re.search("-?\d+\.?\d*[\*\/]-?\d+\.?\d*",num).group() #获取包含*/算式
        if re.search("-?\d+\.?\d*\*-?\d+\.?\d*",ret): #是*的时候
            n1,n2 = re.split("\*",ret) #以*号拆分两边的数字
            multiply = float(n1)*float(n2)  #得到数字进行运算
            if re.search("-\d+\.?\d*\*-\d+\.?\d*",num): #两负相乘加上+
                print(num,"nimei1")
                num = re.sub("-?\d+\.?\d*\*-?\d+\.?\d*",("+"+str(multiply)),num,1) #替换刚算的公式
                print(num,"nimei")
                return multiply_divide(num) #继续递归
            else:
                num = re.sub("-?\d+\.?\d*\*-?\d+\.?\d*", str(multiply), num, 1) #一般正常情况下替换
                return multiply_divide(num)
        else: #是/的时候
            n1,n2 = re.split("\/",ret) #以/分割两边的数字
            shang = float(n1)/float(n2) #得到数字进行运算
            num = re.sub("-?\d+\.?\d*\/-?\d+\.?\d*",str(shang),num,1) #一般正常情况下替换
            return multiply_divide(num) #继续递归
    else: #没有*/的时候
        return num #返回算的结果
'''加减运算函数'''
def add_subtract(num):
    while re.search("-?\d+\.?\d*[\+\-]-?\d+\.?\d*",num): #当有+-运算时循环
        ret = re.search("-?\d+\.?\d*[\+\-]-?\d+\.?\d*",num).group() #获取包含+-*运算的算式
        if re.search("-?\d+\.?\d*\+-?\d+\.?\d*",ret): #是+的时候
            n1,n2 = re.split("\+",ret) #以+分割两边的数字
            he = float(n1)+float(n2) #得到数字进行运算
            num = re.sub("-?\d+\.?\d*\+-?\d+\.?\d*",str(he),num,1) #替换刚算的公式
            return add_subtract(num)
        else:
            n1, n2 = re.split("-", ret,1)  # 以-分割两边的数字
            if n1 == "": #n1分割为空时，说明-号在开头
                n1,n2 = re.split("-",n2) #重新分割上面n2的结果
                cha = -float(n1)-float(n2) #得到数字进行运算，注意前面得加上-号
            else : #不是-开头的时候
                cha = float(n1) - float(n2)  # 得到数字进行运算
            num = re.sub("-?\d+\.?\d*--?\d+\.?\d*",str(cha),num,1) #替换刚算的公式
            return add_subtract(num) #继续递归
    else: #没有+-的时候
        return num #返回算的结果
'''格式输出'''
def form(res,sums):
    res = re.sub("\(|\)", "", res) #去掉括号
    ret = re.sub("\([^()]+\)",res,sums,1) #把括号里的公式替换成结果
    ret = re.sub("\+\+|--", "+", ret) #统一运算符，++为+，--为+
    ret = re.sub("\+-|-\+", "-", ret) #统一运算符，+-为-，-+为-
    return ret #返回结果
'''运算规则'''
def calc(num):
    print(num)
    if re.search("\([^()]+\)",num): #有括号先算
        ret = re.search("\([^()]+\)", num).group() #获取括号里的公式
        res = add_subtract(multiply_divide(ret)) #在括号里先算乘除，后算加减
        return calc(form(res, num)) #将格式化后的结果传给calc函数递归
    else: #没有括号的时候
        res = add_subtract(multiply_divide(num)) #先算乘除，后算加减
        return res
'''用户交互模式'''
while True:
    input_str = input("\033[38;1m请输入您要计算的内容(q退出)>>>>:\033[0m")
    if input_str == "q":
        exit("已退出，欢迎下次使用")
    ret = calc(re.sub(" ","",input_str))
    print("最终结果:","\033[35;1m%s\033[0m"%(ret))
