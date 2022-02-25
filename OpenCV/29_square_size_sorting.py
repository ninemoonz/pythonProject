import numpy as np
import cv2

# 행렬 생성
rands = np.zeros((5, 5), np.uint16)

# 랜덤한 좌표 추출
# 사각형의 시작점 좌표로 사용할 데이터 5개 생성
starts = cv2.randn(rands[:, :2], 100, 50)

# 사각형의 끝점 좌표로 사용할 데이터가 5개 생성
ends = cv2.randn(rands[:, 2: -1], 300, 50)

#print(starts, ends)

# 사각형의 모임을 매개변수로 받아서 내용을 출력하는 함수
def print_rects(rects):
    print("사각형 원소\t\t 사각형 정보\t\t 크기")
    # 인덱스를 i에 넘기고 원래정보를 튜플에 넘기기
    for i, (x, y, w, h, a) in enumerate(rects):
        print("rect[%i] = [(%3d, %3d) from (%3d, %3d)]%5d" % (i, x, y, w, h, a))
    print()

# 사각형 좌표 만들기
# 시작 좌표와 끝 좌표 빼기
sizes = cv2.absdiff(starts, ends)
# 차이를 곱해서 너비를 생성
areas = sizes[:, 0] * sizes[:, 1]
rects = rands.copy()
rects[:, 2: -1] = sizes
rects[:, -1] = areas

# 랜덤한 사각형 정보 출력
print_rects(rects)

# 사각형 정렬
# areas를 가지고 정렬을 한 인덱스를 가지고 rects의 내용을 출력
idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()

idx = np.argsort(areas, axis=0)

sort_rects = rects[idx.astype('int')]
print(sort_rects)

# 잘 이해 안감
