'''
# pip install qrcode pillow image zxing

import qrcode

# 二维码内容
data = "https://www.baidu.com"
# 生成二维码
img = qrcode.make(data=data)
# 直接显示二维码
img.show()
# 保存二维码为文件
img.save("baidu.jpg")



import qrcode
# 实例化二维码生成类
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# 设置二维码数据
data = "https://www.baidu.com"
qr.add_data(data=data)

# 启用二维码颜色设置
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white")

# 显示二维码
img.show()
img.save("baidu1.jpg")

'''

'''
import zxing

reader = zxing.BarCodeReader()
barcode = reader.decode("baidu1.jpg")
print(barcode.parsed)

'''

# -*- coding:utf-8 -*-

'''
====================================
test2:生成二维码保存及对二维码解码输出
====================================
'''
import os
import qrcode
from PIL import Image
from pyzbar import pyzbar


def make_qr_code(content, save_path=None):
    qr_code_maker = qrcode.QRCode(version=5,
                                  error_correction=qrcode.constants.ERROR_CORRECT_M,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    img = qr_code_maker.make_image(fill_color="black", back_color="white")
    if save_path:
        img.save(save_path)
    else:
        img.show()  # 中间图不显示


def make_qr_code_with_icon(content, icon_path, save_path=None):
    if not os.path.exists(icon_path):
        raise FileExistsError(icon_path)

    # First, generate an usual QR Code image
    qr_code_maker = qrcode.QRCode(version=5,
                                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    qr_code_img = qr_code_maker.make_image(
        fill_color="black", back_color="white").convert('RGBA')

    # Second, load icon image and resize it
    icon_img = Image.open(icon_path)
    code_width, code_height = qr_code_img.size
    icon_img = icon_img.resize(
        (code_width // 4, code_height // 4), Image.ANTIALIAS)

    # Last, add the icon to original QR Code
    qr_code_img.paste(icon_img, (code_width * 3 // 8, code_width * 3 // 8))

    if save_path:
        qr_code_img.save(save_path)  # 保存二维码图片
        qr_code_img.show()  # 显示二维码图片
    else:
        print("save error!")


def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)

    # Here, set only recognize QR Code and ignore other type of code
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])


if __name__ == "__main__":
    print("============QRcodetest===============")
    print("         1、Make a QRcode            ")
    print("         2、Scan a QRcode            ")
    print("=====================================")
    print("1、请输入编码信息：")
    code_Data = input('>>:').strip()
    print("正在编码：")
    # ==生成带中心图片的二维码
    #make_qr_code_with_icon(code_Data, "QRcodeCenter.jpg", "qrcode.png")  # 内容，center图片，生成二维码图片
    make_qr_code_with_icon(code_Data, "2.jpg", "qrcode.png")  # 内容，center图片，生成二维码图片
    print("图片已保存，名称为：qrcode.png")
    results = decode_qr_code("qrcode.png")
    print("2、正在解码：")
    if len(results):
        print("解码结果是：")
        print(results[0].data.decode("utf-8"))
    else:
        print("Can not recognize.")
