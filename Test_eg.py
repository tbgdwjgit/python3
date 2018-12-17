__author__ = 'Test-YLL'

# coding:utf-8

# print('中方')

import urllib.request

import urllib.error

try:
    urllib.request.urlopen('http://blog.csdn.net')
except urllib.error.URLError as e:
# except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)