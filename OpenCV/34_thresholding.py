import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/heart10.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', image)
print(image[50])

# image binary
# if goes over 120 255. if not 0
ret, dst = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
print(ret)
print(dst[50])
cv2.imshow('dst', dst)

# binary after fiding threshold
ret1, dst1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(ret1)
print(dst1[50])
cv2.imshow('dst1', dst1)


cv2.waitKey(0)
cv2.destroyAllWindows()
