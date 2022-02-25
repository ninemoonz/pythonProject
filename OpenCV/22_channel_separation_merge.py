import cv2

# 3차원 배열
img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')
print(img)

# 채널 분리 - 2차원 배열 3개로 변경됨
dst = cv2.split(img)
print(dst)

# channel merge
merge = cv2.merge(dst)

cv2.imshow('img', img)

# 추출된 색상의 값만으로 이미지 출력
cv2.imshow('blue', dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red', dst[2])

cv2.imshow('merge', merge)


cv2.waitKey(0)
cv2.destroyAllWindows()

