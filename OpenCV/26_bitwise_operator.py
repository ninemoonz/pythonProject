import numpy as np
import cv2

image1 = np.zeros((300, 300), np.uint8)
image2 = image1.copy()

# 높이와 너비 저장
h, w = image1.shape[:2]
#print(h, w)

# 중앙점의 좌표
cx, cy = w//2, h//2
print(cx, cy)

# 원 그리기
cv2.circle(image1, (cx, cy), 100, 255, -1)
# 사각형 그리기
cv2.rectangle(image2, (0, 0, cx, h), 255, -1)

image3 = cv2.bitwise_or(image1, image2)
image4 = cv2.bitwise_and(image1, image2)
image5 = cv2.bitwise_xor(image1, image2)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)

# 합집합
cv2.imshow('or', image3) # 0 or 0 = 0, 0 or 1 = 1

# 교집합
cv2.imshow('and', image4) # 0 and 0 = 1, 1 and 0 = 0

# 교집합 영역은 검정색 교집합이 아닌 영역은 흰색
cv2.imshow('xor', image5) # 0 xor 0 = 1 xor 1 = 0 = ???

cv2.waitKey(0)
cv2.destroyAllWindows()
