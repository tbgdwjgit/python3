__author__ = 'Test-YLL'

# -*- coding:utf-8 -*-
import logging
logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
import math

class TestFunctionLib:

    def __init__(self, name, salary):
        '''初始化'''
        self.name = name
        self.salary = salary

#eg1:1,2,3组成多少个不重复的三位数？
    def three_Number(self):
        logging.debug('Start of program')
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if (i != k) and (k != j) and (i != j):
                        print(i,j,k)
        logging.debug('End of program')

#eg2:一个整数加100是一个平方数，再加268又是一个平放数
    def sqr_Number(self):
        for i in range(1000000):
            x = int( math.sqrt(i+100))
            y = int( math.sqrt(i+268))
            if (x*x==i+100)and(y*y==i+268):
                print(i)

#eg3:判断一天是这一年的第几天。
    def day_Year(self,y,m,d):
        months=(0,31,59,90,120,151,181,212,243,273,304,334)
        if 0 <= m <= 12:
            sum = months[m-1]
        else:
            print('data error')
        sum += d
        leap = 0
        if (y%400==0) or ((y%4==0) and (y%100!=0)) :
            leap=1
        if(leap == 1)and(month > 2):
            sum+=1
        print(' It is the %dth day.'%sum)

#eg4:输入数字由小到大排序







