import numpy as np
import cv2

#window에 출력할 데이터
image = np.zeros((200, 400), np.uint8)
image[:] = 200

#window 생성
cv2.namedWindow('window', cv2.WINDOW_AUTOSIZE)
#window 출력
cv2.imshow('window', image)

cv2.waitKey(0)

cv2.destroyAllWindows()
