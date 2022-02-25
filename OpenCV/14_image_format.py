# 8비트 영상을 16비트와 32비트 영상 포맷으로 저장 하기
import numpy as np
import cv2
from matplotlib import pyplot as plt

image8 = cv2.imread('/Users/followthesnake/Desktop/data/read_color.jpg', cv2.IMREAD_COLOR)

image16 = np.uint16(image8 * (65535/255)) #16비트는 0 ~ 65535 사이의 정수로 표현
image32 = np.float32(image8 * (1/255)) #32비트는 0 부터 1 사이의 실수로 표현

cv2.imwrite("/Users/followthesnake/Desktop/data/write_test_16.tif", image16)
cv2.imwrite("/Users/followthesnake/Desktop/data/write_test_32.tif", image32)

cv2.imshow("image8", image8)
cv2.imshow("image16", image16)
cv2.imshow("image32", (image32 * 255).astype("uint8"))

cv2.waitKey(0)
cv2.destroyAllWindows()
