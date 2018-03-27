__author__ = 'Test-YLL'

# coding: utf-8
import shelve
DATA_FILE = 'guestbook.dat'
def save_data(name, comment, create_at):
    """�����ύ������
    """
# ͨ��shelveģ������ݿ��ļ�
    database = shelve.open(DATA_FILE)
    # ������ݿ���û��greeting_list�����½�һ����
    if 'greeting_list' not in database:
        greeting_list = []
    else:
# �����ݿ��ȡ����
        greeting_list = database['greeting_list']
    # ���ύ��������ӵ���ͷ
    greeting_list.insert(0, {
'name': name,
'comment': comment,
'create_at': create_at,
    })
    # �������ݿ�
    database['greeting_list'] = greeting_list
    # �ر����ݿ��ļ�
    database.close()
