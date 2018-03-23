__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-

# pip install requests

# 发送请求
import requests
# response = requests.get('http://httpbin.org/get')
# # 获取返回的html信息
# print(response.text)

# 进行带参数的get请求
# data = {'name': 'june', 'password': 123456}
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)

# 还可以添加请求头进行请求
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
# response = requests.get('http://httpbin.org/get', headers=headers )
# print(response.headers)
# print(response.text)

# 进行post请求
data = {'name': 'june', 'password': 123456}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.text)