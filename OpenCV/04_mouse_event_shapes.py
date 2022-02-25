# 마우스 왼쪽 버튼이나 오른쪽 버튼을 누르면 원을 그리고
# shift 키와 button을 같이 누르면 사각형
# 왼쪽 버튼을 두번 누르면 화면을 클리어
# 키보드를 누르면 윈도우 종료

import numpy as np
import cv2
import time

# 마우스 클릭한 시간 저장
last_time = None

#마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    #함수 외부에 있는 데이터를 가져와서 사용
    #global img

    global last_time

    if event == cv2.EVENT_LBUTTONDOWN:
        #마지막 마우스를 클릭한 시간과 현재 시간의 차이가 1보다 작으면
        if last_time is not None and time.time() - last_time < 1:
            param[0] = np.zeros(param[0].shape, np.uint8) + 255
            last_time = None
        else:
            last_time = time.time()
            cv2.rectangle(param[0], (x-5, y-5), (x+5, y+5), (255, 0, 0))
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (255, 0, 0), 3)

    # double click 이벤트 처리 - 캡쳐가 안되느 경우 클릭 이벤트의 시간 사용 가능
    #elif event == cv2.EVENT_LBUTTONDBLCLK:
    #    param[0] = np.zeros(param[0].shape, np.uint8) + 255

    cv2.imshow('img', param[0])

img = np.zeros((512, 512, 3), np.uint8) + 255

cv2.imshow('img', img)

cv2.setMouseCallback('img', onMouse, [img])

key = cv2.waitKey(0)
print(key)

cv2.destroyAllWindows()