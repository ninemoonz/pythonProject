import numpy as np
import cv2


def calc_histo(image, hsize, ranges=[0, 256]):
    hist = np.zeros((hsize, 1), np.float32) # histogram saving array

    # 계급간의 간격 생성
    gap = ranges[1] / hsize

    # 이미지를 순회하면서 개수 구함
    for row in image:
        for pix in row:
            idx = int(pix / gap)
            hist[idx] += 1
    return hist

image = cv2.imread('/Users/followthesnake/Desktop/data/pixel.jpg', cv2.IMREAD_GRAYSCALE)

hsize, ranges = [16], [0, 256]

hist = calc_histo(image, hsize[0], ranges)

print(hist.flatten())
