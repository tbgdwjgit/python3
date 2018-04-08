__author__ = 'Test-YLL'

import logging
logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

import functionlib_test
#from  functionlib_test import TestFunctionLib

logging.debug('Start of program')

tfl = functionlib_test.TestFunctionLib('sdsd',100)
tfl =functionlib_test.TestFunctionLib('sdsd',100)
tfl.three_Number()
tfl.sqr_Number()
tfl.day_Year(1997,7,1)

logging.debug('End of program')

'''
小技巧
'''
l = [1,2,3,4]
print(l[10:])#[]
print(l[-3:])#[2,3,4]
print(l[-4:])#[1,2,3,4]
print(l[-5:])#[1,2,3,4]
print(l[-10:])#[1,2,3,4]