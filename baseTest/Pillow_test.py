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
# drw.arc((200,200,300,300),-360, 0, fill = (0,0,255))
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


from PIL import ImageDraw
img=Image.open(u'E:\中文名称.jpg')
# a=ImageDraw.Draw(img) #使用ImageDraw库进行画图
# a.line(((0,0),(508,493)),fill=(255,0,0))
# a.line(((0,493),(508,0)),fill=(0,255,0,0))
# a.arc((10,10,100,100),0,360,fill=255)
# #因为PIL库编译时缺少东西，所以导致字体不能更改
# #font = ImageFont.truetype ("Arial.ttf",16)
# a.text((10,10),"hello",fill=(255,0,0),font=None)
# img.save("E:\img1.png")
'''
说明：1.画图需要导入ImageDraw库。
　　　2.a=ImageDraw.Draw(img)，对img图像进行画图操作
　　　3.a.line，画直线。((0,0),(508,493))为直线左右起点的坐标。fill=(255,0,0)为直线填充的颜色。
　　　4.a.arc，画弧线。(10,20,100,300)为弧线最左侧距离左边、弧线最上面距离上面、弧线最右面距离左面、弧线最下面距离左边的距离。fill=255为填充的颜色，也可以写成(255,0,0,0)的格式。
　　　5.a.text为添加文字，(10,10)为添加文字的位置，fill=(255,0,0)为填充文字的颜色，font为文字的字体，None为没有样式，font可以自定义。自定义方法为font = ImageFont.truetype ("Arial.ttf",16)
'''

# img.getpixel((4,4))#对像素进行操作getpixel，putpixel
# img.putpixel((4,4),(255,0,0))
# img.save("E:\img1.png","png")
'''
说明：getpixel得到图片img的坐标为(4,4)的像素点。putpixel将坐标为(4,4)的像素点变为(255,0,0)颜色，即红色。
结果如下图所示（因为只有一个像素点，所以不是很清晰）：
'''

# fixedIm=img.rotate(90)#旋转图片rotate
# fixedIm.save("E:\\fixedIm.png","png") #说明：fixedIm=img.rotate(90)，将图片img逆时针旋转90度，存到fixedIm中。

#Logo
import os
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window:
    def __init__(self):
        self.root = root = tkinter.Tk()
        self.Image = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.mstatus = tkinter.IntVar()
        self.fstatus = tkinter.IntVar()
        self.pstatus = tkinter.IntVar()
        self.Image.set('bmp')
        self.mstatus.set(0)
        self.fstatus.set(0)
        self.pstatus.set(0)
        label = tkinter.Label(root,text='Logo')
        label.place(x=5,y=5)
        self.entryLogo = tkinter.Entry(root)
        self.entryLogo.place(x=50,y=5)
        self.buttonBrowserLogo = tkinter.Button(root,text='浏览',command = self.BrowserLogo)
        self.buttonBrowserLogo.place(x=200,y=5)
        self.checkM = tkinter.Checkbutton(root,text ='批量转换',command = self.OnCheckM,
                 variable = self.mstatus,
                 onvalue =1,
                 offvalue =0 )
        self.checkM.place(x=5,y=30)
        label = tkinter.Label(root,text='选择文件')
        label.place(x=5,y=55)
        self.entryFile = tkinter.Entry(root)
        self.entryFile.place(x=60,y=55)
        label = tkinter.Label(root,text='选择目录')




















