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
# from PIL import ImageFilter
# w,h = imga.size
# img_output = Image.new('RGB',(2*w,h))
# img_output.paste(imga,(0,0))
# # b = imga.filter(ImageFilter.GaussianBlur(5))
# # img_output.paste(b,(w,0))
# # img_output.show()
#
# fltrs = []
# # fltrs.append(ImageFilter.EDGE_ENHANCE)#边缘强化
# # fltrs.append(ImageFilter.FIND_EDGES)#查找边缘
# # fltrs.append(ImageFilter.GaussianBlur(4))#高斯模糊
# fltrs.append(ImageFilter.BLUR)#模糊
# fltrs.append(ImageFilter.SHARPEN)#锐化
# fltrs.append(ImageFilter.UnsharpMask(2,150,3))#USM锐化
#
# for fltr in fltrs:
#     r = imga.filter(fltr)
#     img_output.paste(r,(w,0))
#     img_output.show()

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

#画图
# from PIL import ImageDraw
#
# # a = Image.new('RGB',(200,200),'white')
# a = imga
# drw = ImageDraw.Draw(a)
# drw.rectangle((50,50,1000,600),outline='red')
# drw.text((60,60),'My First Draw',fill='green')
# # drw.arc((500,500),0,50,fill='yellow')
# a.show()
# # a.save(r'E:\15test.jpg')#保存图片

imgc = Image.open(r'E:\中文名称.jpg')#打开图片
# imgc.show()#展示图片
# print(imgc.mode,imgc.size,imgc.format)#打印图片信息
# imgc.save("E:\测试.png","png")#保存图片
# newImg = Image.new("RGBA",(640,480),(0,255,0))#创建一个新的图片
# newImg.save(r"E:\newImg.png","PNG")#说明：“RGBA”为图片的mode，（640，480）为图片尺寸，(0,255,0)为图片颜色，颜色第四位为alpha值，可填可不填。
# smallimg = imgc.resize((128,128),Image.ANTIALIAS) #改变图片尺寸
# smallimg.show() #说明：(128,128)为更改后的尺寸，Image.ANTIALIAS有消除锯齿的效果。














