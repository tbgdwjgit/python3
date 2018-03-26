__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-

print("Hello Python interpreter!")
print("中文也没问题!")

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

'''

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
def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')


'''类'''
class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# d = Dog('jack',10)
# d.sit()

'''继承'''
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


'''

'''


