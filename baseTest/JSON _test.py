__author__ = 'Test-YLL'

#import json

# data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
# json = json.dumps(data)
# print(json)

#pip install mysqlclient==1.3.13

'''
MySQL-python：是封装了MySQL C驱动的Python驱动；mysql-connector-python：是MySQL官方的纯Python驱动。
pip install mysql-connector-python==8.0.12


'''

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
# 1
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
# values
# [(u'1', u'Michael')]
# 关闭Cursor和Connection:
cursor.close()
# True
conn.close()