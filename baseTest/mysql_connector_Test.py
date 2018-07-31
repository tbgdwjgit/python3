__author__ = 'Test-YLL'

# -*- coding:utf-8 -*-
import mysql.connector


# mysql1.py
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'port': 3306,
    'database': 'test',
    'charset': 'utf8'
}

#查询
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))

cursor = cnn.cursor()

try:
    sql_query = 'select name,age from stu ;'
    cursor.execute(sql_query)
    for name, age in cursor:
        print (name, age)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()



#增加
def select2(sql_cmd, param):
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))

    cursor = conn.cursor()

    try:
        cursor.execute(sql_cmd, param)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
    finally:
        conn.commit()#执行INSERT等操作后要调用commit()提交事务；
        cursor.close()
        conn.close()

if __name__ ==  '__main__':
    sql_cmd = "insert into stu (name, age, sex) value (%s, %s, %s);"
    #param = ('yangguo', 28, 'male')
    param = ('test', 28, 'm')
    select2(sql_cmd=sql_cmd, param=param)

'''
MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。

安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。
在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：

MySQL-python：是封装了MySQL C驱动的Python驱动；mysql-connector-python：是MySQL官方的纯Python驱动。
pip install mysql-connector-python==8.0.12

'''



