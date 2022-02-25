import numpy as np
import cv2

# 출력할 데이터 생성
img = np.zeros((512, 512, 3), np.uint8) + 255

cv2.line(img, (120, 50), (300, 500), (255, 0, 0), 3)
cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 2)

cv2.imshow('img', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()