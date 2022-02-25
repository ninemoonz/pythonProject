import cv2

# 3차원 배열
img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

# 회전
x_axis = cv2.flip(img, 0)
y_axis = cv2.flip(img, 1)
xy_axis = cv2.flip(img, -1)

# 반복복사
rep_image = cv2.repeat(img, 1, 2)

# 전치
trans_image = cv2.transpose(img)

# 객체들의 이름을 문자열 list로 생성
titles = ["img", "x_axis", "y_axis", "xy_axis", "rep_image", "trans_image"]

# eval은 문자열을 객체로 변환해서 리턴하는 함수
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)
cv2.destroyAllWindows()
