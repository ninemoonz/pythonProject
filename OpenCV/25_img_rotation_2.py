import cv2

src = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

# 이미지 정보 가져오기
rows, cols, channels = src.shape

# 변환 행렬 생성 - 기준좌표, 각도, 크기 비율
M1 = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.5) # center, angle, scale
M2 = cv2.getRotationMatrix2D((rows/2, cols/2), -45, 1.0)
print(M1)

# 변환 행렬을 가지고 결과를 생성
dst1 = cv2.warpAffine(src, M1, (rows, cols))
dst2 = cv2.warpAffine(src, M2, (rows, cols))

# 이미지 출력
cv2.imshow('source', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
