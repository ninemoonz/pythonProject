import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8) + 255

cv2.putText(img, 'Open CV Programming', (50, 100), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)

cv2.imshow('img', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
