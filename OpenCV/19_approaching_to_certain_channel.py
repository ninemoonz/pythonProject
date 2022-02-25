# 컬럼 이미지의 화소 안의 채널 접근
import cv2

img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

img[100:400, 200:300, 0] = 255
img[200:400, 300:300, 1] = 255
img[100:400, 400:500, 2] = 255

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()