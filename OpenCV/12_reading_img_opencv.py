import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/Users/followthesnake/Desktop/data/plane.jpg', cv2.IMREAD_COLOR)

cv2.imshow('plane', image)
cv2.waitKey(0)
cv2.destroyAllWindows()