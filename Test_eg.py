__author__ = 'Test-YLL'

# coding:utf-8

# print('中方')

# import urllib.request
#
# import urllib.error
#
# try:
#     urllib.request.urlopen('http://blog.csdn.net')
# except urllib.error.URLError as e:
# # except urllib.error.HTTPError as e:
#     print(e.code)
#     print(e.reason)

# import re
#
# string ='hellomypythonhispythonourpythonend'
# # pattern = re.compile('.python.')
# # result = pattern.findall(string)
# pattern = 'python.'
# result1=re.sub(pattern,'php',string)
# result2=re.sub(pattern, 'php',string,2)
# print(result1)
# print(result2)

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))



