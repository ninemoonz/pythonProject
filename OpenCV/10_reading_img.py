import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/Users/followthesnake/Desktop/data/plane.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(image, cmap="gray")
plt.axis('off')
plt.show()