#coding:utf-8
#Author:zhiwenwei
class Garen:
    camp = "Demacia"
    def __init__(self,nickname,life_value=2000,aggre_value=100):
        self.nickname = nickname
        self.life_value = life_value
        self.aggre_value = aggre_value
    def attack(self,enemy):
        enemy.life_value = enemy.life_value - self.aggre_value
class Riven:
    camp = "Demacia"
    def __init__(self,nickname,life_value=999,agge_value=200):
        self.nickname = nickname
        self.life_value = life_value
        self.aggre_value = agge_value
    def attack(self,enemy):
        enemy.life_value = enemy.life_value - self.aggre_value
g = Garen("盖伦")
r = Riven("瑞文")
print("盖伦的生命值是%s"%g.life_value)
print("瑞文的生命值是%s"%r.life_value)
g.attack(r)
print("瑞文的生命值是%s"%r.life_value)