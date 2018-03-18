#coding:utf-8
#Author:Mr Zhi
#yesterday2文件内容必须有一个嵌套字典
# yesterday2_open = open("yesterday2",'r+',encoding="utf-8")
# yesterday2_open_read = yesterday2_open.read()
# print(yesterday2_open)
# print(yesterday2_open_read)
# yesterday2_open_read_to_list = eval(yesterday2_open_read)
# username = input("input your name:")
# password = input("input your password:")
# salary = input("input your salary:")
# password_salary = {} #定义一个空字典
# password_salary[password] = [salary]
# yesterday2_open_read_to_list[username] = password_salary
# #yesterday2_open.seek(0) #设置初始指针位置，否则分成多个字典
# yesterday2_open.write(str(yesterday2_open_read_to_list)) #写入到文件中
# yesterday2_open.close()


grade = {}
student_name = input("请输出学生名字：")
homework_name = input("请输入作业名字：")
grade_ = input("请输入这次作业分数：")
grade[student_name]= homework_name
grade[homework_name] = grade_


print(grade)
