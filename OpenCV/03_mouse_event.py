import numpy as np
import cv2

image = np.ones((200, 300), np.float64)

cv2.namedWindow('Mouse Event')
cv2.imshow('Mouse Event', image)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        print(flags)
        print(x, ":", y)

cv2.setMouseCallback('Mouse Event', onMouse)

cv2.waitKey(0)

cv2.destroyAllWindows()