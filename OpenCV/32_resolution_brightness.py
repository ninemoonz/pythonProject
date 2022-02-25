import numpy as np
import cv2

image1 = cv2.imread('/Users/followthesnake/Desktop/data/add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('/Users/followthesnake/Desktop/data/add2.jpg', cv2.IMREAD_GRAYSCALE)

# numpy modulo. 255 넘는 숫자는 0 부터 다시 시작해서 값이 설정
add_image1 = image1 + image2

# opencv의 더하기. over 255 stays as 255
add_image2 = cv2.add(image1, image2)

# 가중치 다르게 적용
add_image3 = cv2.add(image1 * 0.5, image2 * 0.5)
add_image3 = np.clip(add_image3, 0, 255).astype("uint8")

add_image4 = cv2.add(image1 * 0.4, image2 * 0.6)
add_image4 = np.clip(add_image4, 0, 255).astype("uint8")

add_image5 = cv2.add(image1 * 0.7, image2 * 0.6)
add_image5 = np.clip(add_image5, 0, 255).astype("uint8")

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('add_image1', add_image1)
cv2.imshow('add_image2', add_image2)
cv2.imshow('add_image3', add_image3)
cv2.imshow('add_image4', add_image4)
cv2.imshow('add_image5', add_image5)

cv2.waitKey(0)
cv2.destroyAllWindows()