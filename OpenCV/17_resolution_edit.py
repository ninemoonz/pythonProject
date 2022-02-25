# 흑백 이미지에서의 화소 접근

import cv2

img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png', cv2.IMREAD_GRAYSCALE)

# 흑백인 경우 하나의 값으로 변경 가능
# 특정 픽셀 값 변경
img[100, 200] = 0

# 특정 범위의 데이터 변경
img[100:200, 200:300] = 0


cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
