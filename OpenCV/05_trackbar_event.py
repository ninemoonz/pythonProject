import numpy as np
import cv2

# trackbar event processing function
def onChange(value):
    global img
    # 현재 값과 트랙바에서 선택한 값의 차이를 img에 적용
    add_value = value - int(img[0][0])
    img = img + add_value
    cv2.imshow('img', img)

# 출력할 데이터 생성
img = np.zeros((512, 512), np.uint8)
# 윈도우에 출력
cv2.imshow('img', img)

# 트랙바 생성
cv2.createTrackbar("trackbar", "img", img[0][0], 255, onChange)

# Until pressing keyboard
key = cv2.waitKey(0)
# Closing all windows
cv2.destroyAllWindows()