__author__ = 'Test-YLL'

'''
日志
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
可以将 basicConfig() 的 level 参数设置为 logging.ERROR，这将只显示 ERROR和 CRITICAL 消息，跳过 DEBUG、INFO 和 WARNING 消息。
logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable() 将禁用它之后的所有消息，只要向 logging.disable() 传入一个日志级别，它就会禁止该级别和更低级别的所有日志消息。
所以，如果想要禁用所有日志，只要在程序中添加 logging. disable(logging.CRITICAL)。

logging.debug('Start of program')
logging.info('测试')

将日志记录到文件
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
'''

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