# 百度tesseract-ocr使用
from aip import AipOcr
import time
import passwd

# APP_ID = passwd.ocr.APP_ID  # 你的app id, 此处被隐藏,放在pass wd.py文件内,请自行申请
# API_KEY = passwd.ocr.API_KEY  # 你的api key
# SECRET_KEY = passwd.ocr.SECRET_KEY  # 你的secret key


APP_ID = passwd.qinke.APP_ID  # 你的app id, 此处被隐藏,放在pass wd.py文件内,请自行申请
API_KEY = passwd.qinke.API_KEY  # 你的api key
SECRET_KEY = passwd.qinke.SECRET_KEY  # 你的secret key


# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    """ 可选参数 """
    options = {
        "language_type": "CHN_ENG",
        "detect_direction": "true",
        "detect_language": "true",
        "probability": "false"
    }
    # image = get_file_content(image_path)
    # 带参数调用通用文字识别
    result = client.basicGeneral(get_file_content(image_path), options)

    # 格式化输出-提取需要的部分
    if 'words_result' in result:
        text = ('\n'.join([w['words'] for w in result['words_result']]))
        return text

def run_ocr(path, pic_name):
    print('正在调用OCR识别', end='')
    t = time.time()
    file_path = path + str(pic_name)
    text = img_to_str(file_path)
    print('\t\t\t耗时' + str(round(time.time() - t, 3)) + ' s')
    print('< < <■■■■■■■■■■■■■■■■■■■■■■■■■■> > >')
    print(text)
    print('< < <■■■■■■■■■■■■■■■■■■■■■■■■■■> > >')
    return text
    # print("OCR_DONe")
if __name__ == '__main__':
    run_ocr('./', 'test.jpg')

