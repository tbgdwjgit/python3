__author__ = 'Test-YLL'

# coding:utf-8

from PIL import Image

# imga = Image.open('E:\\15.jpg')
# imgb = Image.open('E:\\13.jpg')
imga = Image.open(r'E:\15.jpg')
imgb = Image.open(r'E:\13.jpg')

# Image.blend(imga,imgb,0.5).show()

# mask = Image.open('E:\\13.jpg')
# Image.composite(imga,imgb,mask).show()

# from PIL import ImageFilter
# img_output = Image.new('RGB',(1024,768),'red')
# b = imga.filter(ImageFilter.GaussianBlur)
# img_output.paste(b,(224,0))
# img_output.show()

#图片合成
from PIL import ImageChops
img_output = Image.new('RGB',(1024,768),'red')
# img_output = ImageChops.add(imga,imgb,scale=1.0,offset=0).show()#相加
# img_output = ImageChops.subtract(imga,imgb,scale=1.0,offset=0).show()#减去
# img_output = ImageChops.darker(imga,imgb).show()#变暗
# img_output = ImageChops.lighter(imga,imgb).show()#变亮
# img_output = ImageChops.multiply(imga,imgb).show()#正片叠底
# img_output = ImageChops.screen(imga,imgb).show()#屏幕
# img_output = ImageChops.invert(imga).show()#反相
# img_output = ImageChops.difference(imga,imgb).show()#比较
img_output = ImageChops.constant(imga,125).show()#灰度填充