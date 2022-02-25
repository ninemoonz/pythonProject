import numpy as np
import cv2

def filter(image, mask):
    # 행과 열의 수 구하기
    rows, cols = image.shape[:2]

    # 원본의 행 과 열의 크기로 회선 결과를 저장할 행렬을 생성
    dst = np.zeros((rows, cols), np.float32)

    # 마스크 중심 좌표 찾아오기
    xcenter, ycenter = mask.shape[1] // 2, mask.shape[0] // 2
    # 회선 수행 - 맨 왼쪽 과 오른쪽은 회선을 돌릴 수가 없으므로 0부터 시작하면 안됨
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


# Robers Mask를 위한 함수
def differential(image, data1, data2):
    # 일차원 리스트를 행렬로 변환
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    # 회선 수행
    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)

    # 회선을 수행한 행렬의 크기 계산
    dst = cv2.magnitude(dst1, dst2)

    # 음수가 있으면 양수로 변환
    dst1, dst2 = np.abs(dst1), np.abs(dst2)

    # 255가 넘거나 0보다 작은 수가 있으면 잘라내기
    dst = np.clip(dst, 0, 255).astype("uint8")
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")

    return dst, dst1, dst2


# 이미지 가져오기 - 흑백으로 변환해서 가져오기
image = cv2.imread("/Users/followthesnake/Desktop/data/edge.jpg", cv2.IMREAD_GRAYSCALE)

# 로버츠 마스크를 생성
data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]

data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]

# 로버츠 마스크 적용
dst, dst1, dst2 = differential(image, data1, data2)

# 이미지 출력
cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

# 키보드를 누르면 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()