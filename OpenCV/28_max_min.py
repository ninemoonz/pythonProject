import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/minMax.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', image)

# finding min and max value
(min_val, max_val, _, _) = cv2.minMaxLoc(image)
print(min_val, max_val)

# 255 / (max - min)
ratio = 255 / (max_val - min_val)
# 이미지를 보정해서 새로운 이미지를 생성
dst = np.round((image - min_val) * ratio).astype('uint8')
(dst_min_val, dst_max_val, _, _) = cv2.minMaxLoc(dst)
print(dst_min_val, dst_max_val)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()