import numpy as np
import cv2
from matplotlib import pyplot as plt

src = np.array([[0, 0, 0, 0], [1, 1, 3, 5], [6, 1, 1, 3], [4, 3, 1, 7]], dtype=np.uint8)

# 0~7 까지를 4개의 구간으로 나누어서 히스토그램을 구함
hist1 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[4], ranges=[0, 8])
print(hist1)

# 0~3 까지를 4개의 구간으로 나누어서 ㅎ스토그램을 구함
hist2 = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[4], ranges=[0, 4])
print(hist2)

src = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

# 각채널 색상
histColor = ('b', 'g', 'r')

for i in range(3):
    hist = cv2.calcHist(images=[src], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=histColor[i])
plt.show()