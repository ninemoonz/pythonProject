import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/filter_blur.jpg', cv2.IMREAD_GRAYSCALE)
# 이미지 출력
cv2.imshow('image', image)

# 블러링을 적용할 마스크 행렬 - 홀수의 정방행렬로 생성
# 3 x 3 행렬
data = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]
mask = np.array(data, np.float32).reshape(3, 3)
print(mask)

# 회선 수행 - 화소에 직접 접근
# 행과 열의 수 구하기
rows, cols = image.shape[:2]

# 원본의 행과 열의 크기로 회선 결과를 저장할 행렬을 생성
dst = np.zeros((rows, cols), np.float32)

# 마스크 중심 좌표 찾아오기
xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2

#회선 수행 - 맨 왼쪽과 오른쪽은 회선을 돌릴 수 가 없으므로 0부터 시작하면 안됨
for i in range(ycenter, rows - ycenter):
    for j in range(xcenter, cols - xcenter):
        sum = 0.0
        for u in range(mask.shape[0]):
            for v in range(mask.shape[1]):
                y = i + u - ycenter
                x = j + v - xcenter
                sum += image[y, x] * mask[u, v]
            dst[i, j] = sum

cv2.imshow('pixel', dst.astype('uint8'))

cv2.waitKey(0)
cv2.destroyAllWindows()
