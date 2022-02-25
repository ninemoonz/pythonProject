import cv2

img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png', cv2.IMREAD_GRAYSCALE)
print('img.shape:', img.shape)

# 이미지를 1차원 배열로 생성
img_1 = img.flatten()
print("img_1.shape:", img_1.shape)

# 512 * 512로 나눈 만큼의 차원으로 구조를 변경
img_2 = img_1.reshape(-1, 512, 512)
print("img_2.shape:", img_2.shape)

# 크기 변경
re_img = cv2.resize(img, (64, 64))

cv2.imshow('img', img)
cv2.imshow('re_img', re_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

