__author__ = 'Test-YLL'

# coding: utf-8
import shelve
'''
shelve是python的自带model。
shelve类似于一个存储持久化对象的持久化字典，即字典文件。
使用方法也类似于字典。
'''
DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """保存提交的数据
    """
# 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    # 如果数据库中没有greeting_list，就新建一个表
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # 从数据库获取数据
        greeting_list = database['greeting_list']
    # 将提交的数据添加到表头
    greeting_list.insert(0, {'name': name,'comment': comment,'create_at': create_at,})
    # 更新数据库
    database['greeting_list'] = greeting_list
    # 关闭数据库文件
    database.close()
