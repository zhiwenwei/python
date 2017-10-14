#coding:utf-8
#Author:zhiwenwei
class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
    def shot(self):
        print("shooting...")
    def got_shot(self):
        print("ah...,i got shot")
    def buy_gun(self,gun_name):
        print("just bought %s"%gun_name)
r1 = Role('alex','police','AK47') #生成一个角色
r2 = Role('jack','terrorist','B22') #生成一个角色
print(r1.buy_gun('B33fdsf'))
print(r1.weapon)
