from PIL import Image

# 转换为RGB数值
def make_regular_image(img, size=(256, 256)):
    return img.resize(size).convert('RGB')

# 使用直方图算法 计算所有像素平均值
def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r)) / max(l, r)) for l, r in zip(lh, rh)) / len(lh)

# 传入两个图片, 得到相似度,取值[0.0-1.0]
def calc_similar(li, ri):
    return hist_similar(li.histogram(), ri.histogram())

# 比较相似度主函数
def compare(benchmark_img, img):
    img1 = Image.open(benchmark_img)
    img1 = make_regular_image(img1)
    img2 = Image.open(img)
    img2 = make_regular_image(img2)
    confidence = round(calc_similar(img1, img2), 5)
    print('-<<[置 信 度]>>--\t\t' + str(confidence), end='')
    return confidence

if __name__ == '__main__':  # Compare(benchmarkimg, img)
    compare('.\\test.jpg', '.\QYTang_SalesQQ_dete\\test-new.jpg')


