__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-

import json

# dumps将数据对象转变为json格式
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = json.dumps(data)
print(json)

# 与dumps相反，将json对象转变为字典对象返回





'''
python 原始类型向 json 类型的转化对照表：
Python	         JSON
dict	         object
list, tuple	   array
str, unicode	   string
int, long, float	number
True	          true
False	          false
None	          null

json 类型转换到 python 的类型对照表：
JSON	Python
object	dict
array	list
string	unicode
number (int)	int, long
number (real)	float
true	True
false	False
null	None
'''

'''
第三方库：Demjson
encode	将 Python 对象编码成 JSON 字符串
decode	将已编码的 JSON 字符串解码为 Python 对象
'''
import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = demjson.encode(data)
print(json)

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = demjson.decode(json)
print(text)