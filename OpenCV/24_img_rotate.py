import cv2

# 3차원 배열
img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')
dst = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
