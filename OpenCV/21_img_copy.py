import cv2

img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

dst = img.copy()

dst[100:400, 200:300] = 0

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()