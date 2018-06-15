#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import pymysql
#创建连接
conn = pymysql.connect(host='192.168.10.144',port=3306,user='zww',passwd='123',db='zdb')
#创建游标
cursor = conn.cursor()
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from student1")
print(cursor.fetchall()) #获取结果

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()