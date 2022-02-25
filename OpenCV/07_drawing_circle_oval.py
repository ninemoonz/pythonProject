import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8) + 255

# print(img.shape)

# 전체 영역의 가운데를 기준으로 원 생성
cv2.circle(img, (img.shape[0]//2, img.shape[1]//2), 200, color=(255, 0, 0))
cv2.circle(img, (img.shape[0]//2, img.shape[1]//2), 100, color=(255, 0, 0), thickness=-1)

cv2.imshow('img', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
