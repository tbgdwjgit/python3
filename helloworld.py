__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-
import sys

print('你好，世界！')
print('Hello world！')
print('hello	world')	#注意到	print	是一个函数
print('在某些情况下，会存在一个隐含的假设，允许你不使 \
用反斜杠。这一情况即逻辑行以括号开')

x	=	2
y	=	3
print(x	!=	y) #返回True

# number = int(input())
# while number > 0:
#     print('大于零')
#     # number = 0
#     break
# else:
#      print('小于等零')
#
# for i in range(number):
#     print(i)
# else:
#     print('结束')

print(max(21,3,13))

def	print_max(x,	y):
				'''Prints	the	maximum	of	two	numbers.打印两个数值中的最大数。
				The	two	values	must	be	integers.这两个数都应该是整数'''
				#	如果可能，将其转换至整数类型
				x	=	int(x)
				y	=	int(y)
				if	x	>	y:
								print(x,	'is	maximum')
				else:
								print(y,	'is	maximum')
print_max(3,	5)
print(print_max.__doc__)

print('010','12345678',sep='-')

print('name',sys.__name__)

print(dir(sys))















