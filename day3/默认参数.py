
def stu_register(name,age,course,country="china"):
    print("---注册学生信息")
    print("姓名：",name)
    print("年龄：",age)
    print("国籍",country)
    print("课程：",course)

stu_register("支文伟",25,"英文")
#非固定参数
def stu_register2(name,age,*sex):
    print(name,age,*sex)
stu_register2("zww",22)
#局部变量
name1 = "zww"
def change_name(name):
    print("before change",name1)
    global names
    names = "支文伟是个有前途的人"
    print("after change",name)
change_name("shabi")
print(name)