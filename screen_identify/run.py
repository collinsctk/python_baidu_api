from screen_identify.image_grab import *
from screen_identify import img_histogram, ocr
import os
# run
previous_confidence = 0.10086
benchmark = 'test.jpg'
imgGrab = 'test-new.jpg'
def run():
    global previous_confidence
    # run
    # 定时截图
    while True:
        run_img_grab(imgGrab)
        time.sleep(5)
        # 对比文件，算出置信度
        # 打开文件，
        # 进行比对。
        confidence = img_histogram.compare(benchmark, imgGrab)
        # 若不同，OCR检测
        if confidence > 0.55:  # 如果达到阈值，发送
            if confidence == previous_confidence:
                print('###confidence 一致 \t\t不发送')
            else:
                # 如果低于阈值, 就进行OCR识别
                ocr.run_ocr('./', imgGrab)
                # print('test\t发送成功')
                previous_confidence = confidence  # 记录已匹配的阈值
        else:
            print('###confidence 未达阈值 \t不发送')
        os.unlink(imgGrab)  # 移除文件
        print('\n\n')
run()  # 運行後對比test.jpg文件，對比左上角

