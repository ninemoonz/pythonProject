import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/Users/followthesnake/Desktop/data/plane.jpg', cv2.IMREAD_COLOR)

# OpenCV에서 color 이미지를 읽어오면 RGB 순서가 아니라 BGR 순서
# RGB로 변환
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()