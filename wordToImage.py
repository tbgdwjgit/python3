__author__ = 'Test-YLL'
# -*- coding:utf-8 -*-
import os
import pygame
from pygame.locals import *
#pygame初始化
pygame.init()
text = u'PythonTab中文网'
#设置字体和字号
font = pygame.font.SysFont('Microsoft YaHei',64)#要设置支持中文的字体，不然会生成乱码
#渲染图片
ftext = font.render(text,True,(65,83,130),(255,255,255))
#保存图片
pygame.image.save(ftext,'e:\\pythontab.jpg')