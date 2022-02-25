import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/contrast.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# dummy image
noimage = np.zeros(image.shape[:2], image.dtype)

# 원본 이미지의 평균의 절반
avg = cv2.mean(image)[0]/2.0

# Decreasing contrast ratio
dst1 = cv2.addWeighted(image, 0.5, noimage, 0, avg)
# Amplifying contrast ratio
dst2 = cv2.addWeighted(image, 2.0, noimage, 0, -avg)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
