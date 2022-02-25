import cv2

img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

# 컬러의 경우는 하나의 값으로 변경 가능하고 3채널로도 가능
# 특정 픽셀 값 변경
img[100, 200] = [255, 0, 0]

# 특정 범위의 데이터 변경
img[100:200, 200:300] = [0, 255, 0]

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
