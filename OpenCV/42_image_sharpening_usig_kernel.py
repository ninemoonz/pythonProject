import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/plane.jpg', cv2.IMREAD_GRAYSCALE)

#커널 생성
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
print(kernel)

image_kernel = cv2.filter2D(image, -1, kernel)

#이미지 출력
cv2.imshow('image', image)
cv2.imshow('image_kernel', image_kernel)

cv2.waitKey(0)
cv2.destroyAllWindows()
