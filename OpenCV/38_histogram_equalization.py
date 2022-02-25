import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/equalize.jpg', cv2.IMREAD_GRAYSCALE)

bsize, ranges = [64], [0, 256]
hist = cv2.calcHist([image], [0], None, bsize, ranges)
print(hist.flatten())

cv2.imshow('image', image)

dst = cv2.equalizeHist(image)
cv2.imshow('dst', dst)

hist = cv2.calcHist([dst], [0], None, bsize, ranges)
print(hist.flatten())

cv2.waitKey(0)
cv2.destroyAllWindows()
