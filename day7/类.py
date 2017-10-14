#coding:utf-8
#Author:zhiwenwei
class Dog(object):
    def __init__(self,name,age):  #传参数，叫构造函数也叫构造方法==初始化方法
        '''初始化属性name和age'''
        self.name = name
        self.age = age
    def sit(self):  #类的方法
        '''赋予小狗蹲下的能力'''
        print("[%s] is sitting now."%(self.name))
    def roll(self):
        '''赋予小狗打滚的能力'''
        print("[%s] rolling now!"%self.name)

my_dog = Dog('XiaoHei',3) #实例化，my_dog相当于等于__init__(self,name,age)中的self，实例化后产生的对象叫实例
your_dog = Dog("XiaoHuang",4)  #创建第二个实例
my_dog.sit()  #调用类的方法
my_dog.roll()
your_dog.sit()
print("My dog is called %s,it's %d years old"%(my_dog.name,my_dog.age))  #访问my_dog的属性name的值：my_dpg.name

'''1.方法__init__()
类中的函数称为方法，__init__()是一个特殊的方法(叫做初始化方法(或构造方法))，每当根据Dog类创建新实例时,
在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免 Python 默认方法与普通方法发生名称冲突.
我们将方法 __init__() 定义成了包含三个形参： self 、 name 和 age 。在这个方法的定义中，形参 self 必不可少，还必须位于其他形参的前面。为何必须在方法定义中包
含形参 self 呢？因为 Python 调用这个 __init__() 方法来创建 Dog 实例时，将自动传入实参 self 。每个与类相关联的方法调用都自动传递实参 self ，它是一个指向实例本身
的引用，让实例能够访问类中的属性和方法。我们创建 Dog 实例时， Python 将调用 Dog 类的方法 __init__() 。我们将通过实参向 Dog() 传递名字和年龄； self 会自动传递，
因此我们不需要传递它。每当我们根据 Dog 类创建实例时，都只需给最后两个形参（ name 和 age ）提供值。

2.self.name和self.age类似，像这样可通过实例访问的变量称为属性 
3.Dog 类还定义了另外两个方法： sit和roll由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参 self 。后面将创建的实例能
够访问这些方法。
'''