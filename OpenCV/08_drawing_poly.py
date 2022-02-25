import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8) + 255

pts = np.array([[100, 100], [200, 100], [200, 200], [100, 200], [200, 50]])

cv2.polylines(img, [pts], isClosed=False, color=(0, 255, 0))

cv2.imshow('img', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
