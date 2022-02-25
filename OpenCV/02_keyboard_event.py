# Making an event which print a or b on console, and quit on pressing esc

import numpy as np
import cv2

# ord function -> 2byte 문자의 앞부분만 추출해서 1byte ASCII code로 만들어주는 함수
switch_case = {ord('a'): 'a키 입력', ord('b'): 'b키 입력'}

# Window 에 출력할 데이터
image = np.ones((200, 300), np.float64)

# window 생성
cv2.namedWindow('Keyboard Event')
# window 출력
cv2.imshow('Keyboard Event', image)

while True:
    # 키보드 입력 대기
    key = cv2.waitKey(0)
    print(key)
    if key == 27:
        break
    try:
        result = switch_case[key]
        print(result)
    except:
        result = -1

cv2.destroyAllWindows()