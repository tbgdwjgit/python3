__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-

# pip install requests

# 发送请求
import requests
response = requests.get('http://httpbin.org/get')
# 获取返回的html信息
print(response.text)


# 进行带参数的get请求
data = {'name': 'june', 'password': 123456}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)