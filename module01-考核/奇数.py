
# #Author:Mr Zhi
# l = []
# i = 1
# for i in range(1,101):
#     if (i % 2) == 1:
#         l.append(i)
# print(l)

# i = 0
# sum = 0
# while (i < 100):
#     i +=1
#     sum += i
# print(sum)
import  sys
n = "老男孩"
print(sys.getdefaultencoding())
n1 = n.encode("utf-8")
print(n1)
n1 = n.encode("utf-8")
n2 = n1.decode("utf-8")
print(n2.encode("gbk"))
print(sys.getdefaultencoding())
#求0-100的和
sum = 0
for i in range(101):sum += i
print(sum)
#求100以内偶数之和
sum = 0
l = []
for i in range(2,101):
    if i % 2 == 0:
        sum +=i
        l.append(i)
print(sum,l)

