__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-
import os

print("Hello Python interpreter!")
print("中文也没问题!")

print('翻倍'*3)
print('45+55')
print(45+55)

#注释
'''
多行

print("Hello World")
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


变量名只能包含以下字符：
•  小写字母（a~z）
•  大写字母（A~Z）
•  数字（0~9）
•  下划线（_）
名字不允许以数字开头。

'''

'''
列表
'''
# letters =[2,22,'2cd',5]
# print(letters[1])
# #append()和 extend()的区别
# letters.append('vvv')
# letters.extend(['mmm'])
# letters.extend('mmm')
# letters.insert(3,'55')
# print(letters)
# letters.remove('55')
# print(letters)
# del letters[0]
# print(letters)
# print(letters.pop(1))
# print(letters.pop(1))
# print(letters.pop(0))
# print(letters)
# letters.sort()#改变你提供的原始列表，而不是创建一个新的有序列表
# print(letters)
# letters.reverse()
# print(letters)

'''
集合
[] 能创建一个空列表
{} 会创建一个空字典
空集输出为 set()
'''
print(set())
s_test ={1,2,3,4}
s_test.add('a')
print(s_test)




"""
控制流
"""
# print('What is your name?')
# name = input()
# print('What is your age?')
# age = input()
#
# if name == 'Alice':
#     print('Hi, Alice.')
# elif int(age) < 12:
#     print('You are not Alice, kiddo.')
# else:
#     print('You are neither Alice nor a little kid.')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')

# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

# import random
# for i in range(5):
#     print(random.randint(1, 10))
#
# import sys
# sys.exit()

'''
函数
'''
# def hello(name):
#     print('Hello ' + name)
#
# hello('Alice')
# hello('Bob')

def printMyNameBig():
    print("  CCCC       A       RRRRR  TTTTTTT  EEEEEE  RRRRR  ")
    print(" C    C     A A      R    R    T     E       R    R ")
    print("C          A   A     R    R    T     EEEE    R    R ")
    print("C         AAAAAAA    RRRRR     T     E       RRRRR  ")
    print(" C    C  A       A   R    R    T     E       R    R ")
    print("  CCCC  A         A  R     R   T     EEEEEE  R     R")
    print()
for i in range(2):
    printMyNameBig();

'''类'''
class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

     #特殊方法是 __str__()，它会告诉 Python 打印（print）一个对象时具体显示什么内容。
    def __str__(self):
        msg = "Hi, I'm a " + self.name + " " + str(self.age) + " ball!"
        return msg

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

d = Dog('jack',10)
# d.sit()
print(d)

'''继承'''
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())


'''
文件处理
os.getcwd()取当前目录
os.path.dirname(os.getcwd())取当前目录上一级目录

'''
import re
def transformCodec(re_data):#ascii (gbk) 转 unicode
    try:
        re_data = re_data.decode('gbk')
    except Exception as error:
        print(error)
        print('delete illegal string,try again...')

        pos = re.findall(r'decodebytesinposition([\d]+)-([\d]+):illegal',str(error).replace(' ',''))
        if len(pos)==1:
            re_data = re_data[0:int(pos[0][0])]+re_data[int(pos[0][1]):]
            re_data = transformCodec(re_data)
            return re_data
    return re_data


# textFile = open(os.path.pardir +'\\readme.txt')
# textFile ='C:\\Users\\Test-YLL\\PycharmProjects\\python3\\test.txt'
# textFile =u'test.txt'
# print(textFile)
# # with open('test.txt') as file_object:
# with open(textFile) as file_object:
#     contents = file_object.read()
#     print(contents)

# print(os.getcwd())
# print(os.path.dirname(os.getcwd()))
# textFile =os.path.dirname(os.getcwd())+r'\readme.txt'
# print(textFile)
# with open(textFile,'rb') as file_object:
# # with open(textFile,'r', encoding='gbk') as file_object:
# #      contents = file_object.read()
#     contents = transformCodec( file_object.read()) #转码
#     print(contents)

'''
Python数据可视化：Matplotlib
pip install matplotlib
pip install pandas
pip install xlrd

'''
# a = 5
# matplotlib.lines
# from matplotlib.pyplot import plot
# plot(a, a**2)

# import matplotlib.pyplot as plt
# import pandas as pd
# # import seaborn as sns
# import numpy as np
#
# # 0、导入数据集
# df = pd.read_excel('first.xlsx', 'Sheet1')
#
# var = df.groupby('BMI').Sales.sum()
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlabel('BMI')
# ax.set_ylabel('Sum of Sales')
# ax.set_title('BMI wise Sum of Sales')
# var.plot(kind='line')
#
# plt.show()


