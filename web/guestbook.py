__author__ = 'Test-YLL'

# coding: utf-8
import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    '''保存提交的数据'''
    # 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    # 如果数据库中没有greeting_list，就新建一个表
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # 从数据库获取数据
        greeting_list = database['greeting_list']
    # 将提交的数据添加到表头
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })
    # 更新数据库
    database['greeting_list'] = greeting_list
    # 关闭数据库文件
    database.close()


'''写入读取'''
import datetime

# save_data('test', 'test comment',datetime.datetime(2018, 3, 28, 10, 0, 0))

# db = shelve.open(DATA_FILE)  #打开文件
# print(db['greeting_list'])  #向从字典中获取键的方式一样读取内容
# db.close()  #关闭文件