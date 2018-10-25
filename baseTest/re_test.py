__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-

import  re

"""
    表示择一匹配的管道符号（|），也就是键盘上的竖线，表示一个“从多个模式中选择其一”的操作。
"""

# m = re.match('f...','fo#d.fdo')
# m = re.match('\d{3}.\d{3}.\d{3}.\d{3}','122.122.122.122')
# m = re.match('b[aie]r','barbir')
# m = re.search('bar','ffbarberffbir')
# print(m.group())
# print(m.groups())


# m = re.match('fo','fo#d.fdowqqqqqqqqqqqq')
m = re.search('fo','wwwwwwwwwfo#d.fdowqqqqqqqqqqqq')
m = re.match('\w+@(\w+\.)?\w+\.com','1eee@163.com')
if m is not None:
    print(m.group())


m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
if m is not None:
    print(m.group())
    print(m.groups())