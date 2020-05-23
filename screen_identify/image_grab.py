import time
import win32api
import win32gui
import win32ui
import win32con


# 截图函数
def window_capture(filename):
    hwnd = 0                                                # 窗口的编号，0号表示当前活跃窗口
    hwnd_dc = win32gui.GetWindowDC(hwnd)                    # 根据窗口句柄获取窗口的设备上下文DC（Device Context）
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)            # 根据窗口的DC获取mfcDC
    save_dc = mfc_dc.CreateCompatibleDC()                   # mfcDC创建可兼容的DC
    save_bit_map = win32ui.CreateBitmap()                   # 创建big map准备保存图片
    # moniter_dev = win32api.EnumDisplayMonitors(None, None)  # 获取显示器信息
    # w = moniter_dev[0][2][2]
    # h = moniter_dev[0][2][3]
    # print(w, h)                                              # 屏幕分辨率
    save_bit_map.CreateCompatibleBitmap(mfc_dc, 372, 178)    # 设置bitmap画布大小

    save_dc.SelectObject(save_bit_map)                       # 高度saveDC，将截图保存到saveBitmap中
    save_dc.BitBlt((0, -50),                                 # (0,-50)截图开始位置,即左上角往下第50个像素点
                   (372, 228),                               # (372, 228) 截图结束位置, 如果改为(0, 0), (w, h)就是全屏截图
                   mfc_dc, (0, 0), win32con.SRCCOPY)
    # print('類型:', type(save_bit_map))
    save_bit_map.SaveBitmapFile(save_dc, filename)

# 这个函数主要用来计算时间
def run_img_grab(name):
    # beg = time.time()
    # for i in range(10):
    window_capture(str(name))
    # end = time.time()
    # print(end - beg)

if __name__ == '__main__':
    run_img_grab('test.jpg')