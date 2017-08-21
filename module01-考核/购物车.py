#coding:utf-8
#Author:Mr Zhi
product_list = [
    ('iphone',5000),
    ('bike',1500)
]
salary = input("请输入工资").strip()
if salary.isdigit():
    salary = int(salary)
shopping_list = []
print(product_list[1])
while True:
    for index,item in enumerate(product_list):
        print(index,item)
    choice = input("请选择产品编码:").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice < len(product_list) and choice >=0:
           p_item = product_list[choice]
           if salary >= p_item[1]:
               shopping_list.append(p_item)
               print("你的购物单:",shopping_list)
               salary -= p_item[1]
           else:
               print("你的余额不足")
        else:
            print("无效编码")