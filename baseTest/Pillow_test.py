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
                 variable = self.mstatus,onvalue =1,offvalue =0 )
        self.checkM.place(x=5,y=30)
        label = tkinter.Label(root,text='选择文件')
        label.place(x=5,y=55)
        self.entryFile = tkinter.Entry(root)
        self.entryFile.place(x=60,y=55)
        self.buttonBrowserFile = tkinter.Button(root,text ='浏览',command = self.BrowserFile)
        self.buttonBrowserFile.place(x=200,y=55)
        label = tkinter.Label(root,text='选择目录')
        label.place(x=5,y=80)
        self.entryDir = tkinter.Entry(root,state = tkinter.DISABLED)
        self.entryDir.place(x=60,y=80)
        self.buttonBrowserDir = tkinter.Button(root,text='浏览',
                                               command = self.BrowserDir,
                                               state = tkinter.DISABLED)
        self.buttonBrowserDir.place(x=200,y=80)

        self.checkF = tkinter.Checkbutton(root,text='改变文件格式',
                                          command = self.OnCheckF,
                                          variable = self.fstatus,
                                          onvalue =1,
                                          offvalue =0)
        self.checkF.place(x=5,y=110)
        frame = tkinter.Frame(root)
        frame.place(x=10,y=130)
        labelTo = tkinter.Label(frame,text='格式')
        labelTo.pack(anchor='w')
        self.rBmp = tkinter.Radiobutton(frame,variable = self.Image,
                                        value='bmp', text = 'BMP',state=tkinter.DISABLED)
        self.rBmp.pack(anchor='w')
        self.rJpg = tkinter.Radiobutton(frame,variable = self.Image,
                                        value='jpg', text = 'JPG',state=tkinter.DISABLED)
        self.rJpg.pack(anchor='w')
        self.rGif = tkinter.Radiobutton(frame,variable = self.Image,
                                        value='gif', text = 'GIF',state=tkinter.DISABLED)
        self.rGif.pack(anchor='w')
        self.rPng = tkinter.Radiobutton(frame,variable = self.Image,
                                        value='png', text = 'PNG',state=tkinter.DISABLED)
        self.rPng.pack(anchor='w')
        pframe = tkinter.Frame(root)
        pframe.place(x=70,y=130)
        labelPos = tkinter.Label(pframe,text='位置')
        labelPos.pack(anchor='w')
        self.rLT = tkinter.Radiobutton(pframe,variable = self.pstatus,value=0,text='左上角')
        self.rLT.pack(anchor='w')
        self.rRT = tkinter.Radiobutton(pframe,variable = self.pstatus,value=0,text='右上角')
        self.rRT.pack(anchor='w')
        self.rLB = tkinter.Radiobutton(pframe,variable = self.pstatus,value=0,text='左下角')
        self.rLB.pack(anchor='w')
        self.rRB = tkinter.Radiobutton(pframe,variable = self.pstatus,value=0,text='右下角')
        self.rRB.pack(anchor='w')
        self.buttonAdd = tkinter.Button(root,text ='增加',command = self.Add)
        self.buttonAdd.place(x=180,y=175)
        self.labelStatus = tkinter.Label(root,textvariable=self.status)
        self.labelStatus.place(x=150,y=205)
    def MainLoop(self):#进入消息循环
        self.root.minsize(250,270)
        self.root.maxsize(250,270)
        self.root.mainloop()
    def BrowserLogo(self):
        file = tkinter.filedialog.askopenfilename(title='Python Music Player',
            filetypes=[('JPG','*.jpg'),('BMP','*.bmp'),('GIF','*.gif'),('PNG','*.png')])
        if file:
            self.entryLogo.delete(0,tkinter.END)
            self.entryLogo.insert(tkinter.END,file)
    def BrowserDir(self):#选择路径
        directory = tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0,tkinter.END)
            self.entryDir.insert(tkinter.END,directory)
    def BrowserFile(self): #选择文件
        file = tkinter.filedialog.askopenfilename(title='',
            filetypes =[('JPG','*.jpg'),('BMP','*.bmp'),('GIF','*.gif'),('PNG','*.png')])
        if file:
            self.entryFile.delete(0,tkinter.END)
            self.entryFile.insert(tkinter.END,file)
    def OnCheckM(self):#设置组件状态
        if not self.mstatus.get():
            self.entryDir.config(state=tkinter.DISABLED)
            self.entryFile.config(state=tkinter.NORMAL)
            self.buttonBrowserDir.config(state=tkinter.DISABLED)
            self.buttonBrowserFile.config(state=tkinter.NORMAL)
        else:
            self.entryDir.config(state=tkinter.NORMAL)
            self.entryFile.config(state=tkinter.DISABLED)
            self.buttonBrowserDir.config(state=tkinter.NORMAL)
            self.buttonBrowserFile.config(state=tkinter.DISABLED)
    def OnCheckF(self):#设置组件状态
        if not self.fstatus.get():
            self.rBmp.config(state=tkinter.DISABLED)
            self.rJpg.config(state=tkinter.DISABLED)
            self.rGif.config(state=tkinter.DISABLED)
            self.rPng.config(state=tkinter.DISABLED)
        else:
            self.rBmp.config(state=tkinter.NORMAL)
            self.rJpg.config(state=tkinter.NORMAL)
            self.rGif.config(state=tkinter.NORMAL)
            self.rPng.config(state=tkinter.NORMAL)
    def Add(self):#处理图片
        n=0
        if self.mstatus.get():
            path = self.entryDir.get()
            if path=='':
                tkinter.messagebox.showerror('Python tkinter','请输入路径')
                return
            filenames = os.listdir(path)
            if self.fstatus.get():
                f=self.Image.get()
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.addlogo(path+'/'+filename,f)
                        n =n+1
            else:
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.addlogo(path+'/'+filename)
                        n = n+1
        else:
            file = self.entryFile.get()
            if file=='':
                tkinter.messagebox.showerror('Python tkinter','请选择文件')
                return
            if self.fstatus.get():
                f = self.Image.get()
                self.addlogo(file,f)
                n=n+1
            else:
                self.addlogo(file)
                n=n+1
        self.status.set('成功添加%d张图片'% n)
    def addlogo(self,file,format=None):#向图片添加Logo
        logo = self.entryLogo.get()
        if logo=='':
            tkinter.messagebox.showerror('Python tkinter','请选择Logo')
            return
        im = Image.open(file)
        lo = Image.open(logo)
        imwidth = im.size[0]
        imheight = im.size[1]
        lowidth = lo.size[0]
        loheight = lo.size[1]
        pos = self.pstatus.get()
        if pos == 0:
            left = 0
            top = 0
            right = lowidth
            bottom = loheight
        elif pos == 1:
            left = imwidth - lowidth
            top = 0
            right = imwidth
            bottom = loheight
        elif pos == 2:
            left = 0
            top = imheight - loheight
            right = lowidth
            bottom = imheight
        else:
            left = imwidth - lowidth
            top = imheight - loheight
            right = imwidth
            bottom = imheight
        im.paste(lo,(left,top,right,bottom))
        if format:
            im.save(file[:(len(file)-4)]+'_logo.'+ format)
        else:
            im.save(file[:(len(file)-4)]+'_logo'+ file[-4:])

window = Window()
window.MainLoop()



















