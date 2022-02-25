import numpy as np
import cv2

image = cv2.imread('/Users/followthesnake/Desktop/data/filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)
#image 출력
cv2.imshow('image', image)

# 2개의 마스크 생성
data1 = [0, -1, 0,
         -1, 5, -1,
         0, -1, 0]

data2 = [-1, -1, -1,
         -1, 9, -1,
         -1, -1, -1]

mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32).reshape(3, 3)

#sharpening을 위한 회선 수행 function
def filter(image, mask):
    #행과 열의 수 구하기
    rows, cols = image.shape[:2]

    #원본의 행과 열의 크기로 회선 결과를 저장할 행렬을 생성
    dst = np.zeros((rows, cols), np.float32)

    # 마스크 중심 좌표 찾아오기
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2

    # 회선 수행 - 맨 왼쪽 과 오른쪽은 회선을 돌릴 수 가 없으므로 0부터 시작하면 안됨
    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y = i + u - ycenter
                    x = j + v - xcenter
                    sum += image[y, x] * mask[u, v]
                dst[i, j] = sum
    return dst

# sharpening - 가중치의 합이 1이 넘기 때문에 255가 넘는 수가 나올 수 있음
sharpen1 = filter(image, mask1)
sharpen2 = filter(image, mask2)
# 정규화 수행
sharpen1 = cv2.convertScaleAbs(sharpen1)
sharpen2 = cv2.convertScaleAbs(sharpen2)

cv2.imshow('sharpen1', sharpen1)
cv2.imshow('sharpen2', sharpen2)

cv2.waitKey(0)
cv2.destroyAllWindows()

