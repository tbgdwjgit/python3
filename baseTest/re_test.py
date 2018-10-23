__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-

import  re

"""
    表示择一匹配的管道符号（|），也就是键盘上的竖线，表示一个“从多个模式中选择其一”的操作。
"""

# m = re.match('f...','fo#d.fdo')
# m = re.match('\d{3}.\d{3}.\d{3}.\d{3}','122.122.122.122')
m = re.match('b[aie]r','barbir')
print(m.group())






