from aip import AipImageCensor
import passwd

APP_ID = passwd.sex.APP_ID  # 你的app id , 此处被隐藏,放在pass wd.py文件内,请自行申请
API_KEY = passwd.sex.API_KEY  # 你的api key
SECRET_KEY = passwd.sex.SECRET_KEY  # 你的secret key


client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

# 调用色情识别接口
result = client.imageCensorUserDefined(get_file_content('sex3.jpg'))
""" 如果图片是url调用如下 """
# result = client.imageCensorUserDefined('https://imgsa.baidu.com/forum/w%3D580/sign=559cf2cad93f8794d3ff4826e21a0ead/f3bc0ddda3cc7cd94ac925ab3401213fb90e91eb.jpg')
print(result)

# 官方测试 :https://ai.baidu.com/tech/imagecensoring
