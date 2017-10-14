#coding:utf-8
#Author:zhiwenwei
'''编写表示汽车的类'''
class Car(object):
    def __init__(self,name,model,year):
        '''初始化描述汽车的属性'''
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 0  #给属性指定默认值
    def describe_car(self):
        '''返回汽车的信息'''
        print("%s %s %d"%(self.name,self.model,self.year))
    def odometer_read(self):
        '''打印汽车里程信息'''
        print("this car has " + str(self.odometer) + " miles on it")
my_car = Car("Audi","a4",2016)
my_car.describe_car()
my_car.odometer_read()
my_car.odometer = 100 #直接修改属性的值
my_car.odometer_read()