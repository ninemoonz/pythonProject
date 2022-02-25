import numpy as np
import cv2

image1 = cv2.imread('/Users/followthesnake/Desktop/data/abs_test1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('/Users/followthesnake/Desktop/data/abs_test2.jpg', cv2.IMREAD_GRAYSCALE)

# Differenciation
dif_img1 = cv2.subtract(image1, image2)

# 음수 보전
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))
# 음수 보전한 데이터를 절대값으로 치환
abs_dif1 = np.absolute(dif_img2).astype('uint8')
# 차분 절대값 함수 이용
abs_dif2 = cv2.absdiff(image1, image2)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('dif_img1', dif_img1)
cv2.imshow('abs_dif1', abs_dif1)
cv2.imshow('abs_dif2', abs_dif2)

cv2.waitKey(0)
cv2.destroyAllWindows()
