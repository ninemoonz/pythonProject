import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/hist_stretch.jpg', cv2.IMREAD_GRAYSCALE)

# creating histogram values - 값이 가운데 영역에 치우쳐 있음
bsize, ranges = [64], [0, 256]
hist = cv2.calcHist([image], [0], None, bsize, ranges)
print(hist.flatten())

cv2.imshow('image', image)

# 빈도수가 가장 높은 값과 가장 낮은 값을 춪기 위한 함수
def search_value_idx(hist, bias=0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        if hist[idx] > 0:
            return idx
        return -1

# 각 구간의 너비 구하기
bin_width = ranges[1]/bsize[0]

#빈도수가 높은 값과 낮은 값 찾기
high = search_value_idx(hist, bsize[0] - 1) * bin_width
low = search_value_idx(hist, 0) * bin_width
print(high)
print(low)

#histogram stretching
idx = np.arange(0, 256)
idx = (idx - low) * 255 / (high - low)
idx[0:int(low)] = 0
idx[int(high+1):] = 255
dst = cv2.LUT(image, idx.astype('uint8'))

cv2.imshow('dst', dst)

hist1 = cv2.calcHist([dst], [0], None, bsize, ranges)
print(hist1.flatten())

cv2.waitKey(0)
cv2.destroyAllWindows()
