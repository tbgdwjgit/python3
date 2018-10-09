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

#滤镜
from PIL import ImageFilter
w,h = imga.size
img_output = Image.new('RGB',(2*w,h))
img_output.paste(imga,(0,0))
b = imga.filter(ImageFilter.GaussianBlur(5))
img_output.paste(b,(w,0))
img_output.show()














#图片合成
# from PIL import ImageChops
# img_output = Image.new('RGB',(1024,768),'red')
# img_output = ImageChops.add(imga,imgb,scale=1.0,offset=0).show()#相加
# img_output = ImageChops.subtract(imga,imgb,scale=1.0,offset=0).show()#减去
# img_output = ImageChops.darker(imga,imgb).show()#变暗
# img_output = ImageChops.lighter(imga,imgb).show()#变亮
# img_output = ImageChops.multiply(imga,imgb).show()#正片叠底
# img_output = ImageChops.screen(imga,imgb).show()#屏幕
# img_output = ImageChops.invert(imga).show()#反相
# img_output = ImageChops.difference(imga,imgb).show()#比较
# img_output = ImageChops.constant(imga,125).show()#灰度填充

#调整图像
# from PIL import ImageEnhance
# #imga = Image.open(r'E:\15.jpg')
# w,h =imga.size
# img_output = Image.new('RGB',(2*w,h))
# img_output.paste(imga,(0,0))
#
# nhc = ImageEnhance.Color(imga)
# nhb = ImageEnhance.Brightness(imga)
# for nh in [nhc,nhb]:
#     for ratio in [0.6,1.8]:
#         b = nh.enhance(ratio)
#         img_output.paste(b,(w,0))
#         img_output.show()
