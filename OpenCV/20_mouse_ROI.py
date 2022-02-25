# ROI = Region Of Interest
import cv2

img = cv2.imread('/Users/followthesnake/Desktop/data/Lena.png')

roi = cv2.selectROI(img, showCrosshair=False)
print(roi)

select_img = img[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]

cv2.imshow('img', select_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
