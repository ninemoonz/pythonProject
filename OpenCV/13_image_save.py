import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/Users/followthesnake/Desktop/data/plane.jpg', cv2.IMREAD_COLOR)

# image를 파일로 저장
cv2.imwrite('/Users/followthesnake/Desktop/data/plane_new.jpg', image)

