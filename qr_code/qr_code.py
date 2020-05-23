# -*- coding:utf-8 -*-

import os
import qrcode  # 生成二维码
from PIL import Image      # 用来图像处理
from pyzbar import pyzbar  # 用来识别二维码


# 普通二维码 ,只需要导入qr code库
def make_qr_code(content, save_path=None):
    qr_code_maker = qrcode.QRCode(version=5,
                                  error_correction=qrcode.constants.ERROR_CORRECT_M,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    img = qr_code_maker.make_image(fill_color="red", back_color="white")
    if save_path:
        img.save(save_path)
    else:
        img.show()  # 中间图不显示


def make_qr_code_with_icon(content: object, icon_path: object, save_path: object = None):
    if not os.path.exists(icon_path):
        raise FileExistsError(icon_path)

    # 首先, 创建一个普通qr code
    qr_code_maker = qrcode.QRCode(version=5,
                                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    qr_code_img = qr_code_maker.make_image(  # 设置qr code样式.设置颜色,背景,使用R G B A 色彩空间
        fill_color="black", back_color="white").convert('RGBA')

    # 第二步,添加图标 并设置尺寸
    icon_img = Image.open(icon_path)
    code_width, code_height = qr_code_img.size
    icon_img = icon_img.resize(
        (code_width // 4, code_height // 4), Image.ANTIALIAS)

    # 最后, 把图标添加到qr code上
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
    print("1、请输入编码文本,或链接形式直接输入https://xxx.t.cn：")
    code_Data = input('>>:').strip()  # "https://www.qytang.com"
    print("正在编码：")
    # ==生成带中心图片的二维码
    make_qr_code_with_icon(
        code_Data, "qytanglogo.png", "qrcode.png")  # 内容，center图片，输出二维码图片的名字
    print("图片已保存，名称为：qrcode.png")


    results = decode_qr_code("qrcode.png")
    print("2、正在解码：")
    if len(results):
        print("解码结果是：")
        print(results[0].data.decode("utf-8"))
    else:
        print("Can not recognize.")
