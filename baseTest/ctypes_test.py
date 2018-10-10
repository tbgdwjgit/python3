__author__ = 'Test-YLL'

# coding:utf-8

'''
使用python中的ctypes模块可以很方便的调用windows的dll（也包括linux下的so等文件）
'''
import ctypes
from ctypes import *

#cdecl调用约定
# dll = CDLL("Lib.dll")
# dll = ctypes.cdll.LoadLibrary("Lib.dll")

#stdcall调用约定
# dll = ctypes.windll.LoadLibrary("Lib.dll")
dll = ctypes.WinDLL("Lib.dll")
str = dll.testint()
# str = dll.testpchar()

print(str)

# rc = dll.testpchar()
# rc = ctypes.c_wchar_p(rc)
# print(rc.value)
rc = dll.teststring()
rc = ctypes.c_char_p(rc)
print(rc.value)



