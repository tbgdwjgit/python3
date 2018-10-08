__author__ = 'Test-YLL'

# coding:utf-8

from PIL import Image

imga = Image.open('E:\\15.jpg')
imgb = Image.open('E:\\13.jpg')

# Image.blend(imga,imgb,0.5).show()

# mask = Image.open('E:\\13.jpg')
# Image.composite(imga,imgb,mask).show()

from PIL import ImageFilter
img_output = Image.new('RGB',(1024,768),'red')
b = imga.filter(ImageFilter.GaussianBlur)
img_output.paste(b,(224,0))
img_output.show()