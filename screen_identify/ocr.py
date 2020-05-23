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


# 初始化AipOcr对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    # 文档称必须传入的options 字段
    options = {
        "language_type": "CHN_ENG",  # 识别语言类型 CHN为中文,ENG为英文
        "detect_direction": "true",  # 检测方向: true 为横向是否检测图像朝向，
                                     # 默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括:
                                     # true：检测朝向；
                                     # false：不检测朝向。
        "detect_language": "true",   # 识别语言: true为是
        "probability": "false"       # 是否返回识别结果中每一行的置信度
    }
    # image = get_file_content(image_path)
    # 带参数调用通用文字识别
    result = client.basicGeneral(get_file_content(image_path), options)
    # result的字典
    # {'log_id': 7915507311885284247,
    #  'direction': 0,
    #  'words_result_num': 1,
    #  'words_result': [{'words': 'Welcome To Qytang Python'}],
    #  'language': 0}

    # 提取识别的文字, 可能有多行, 插入换行然后打印
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

