import numpy as np
import cv2
import time

# ordinary way
def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            image1[i, j] = 255 - pixel
        return image1

# item function way
def pixel_access2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)
            image2.itemset((i, j), 255 - pixel)
        return image2

# lookup table
def pixel_access3(image):
    lut = [255-i for i in range(256)]
    lut = np.array(lut, np.uint8)
    image3 = lut[image]

    return image3

# OpenCV function
def pixel_access4(image):
    image4 = cv2.subtract(255, image)
    return image4

# numpy operator
def pixel_access5(image):
    image5 = 255 - image
    return image5

image = cv2.imread('/Users/followthesnake/Desktop/data/bright.jpg', cv2.IMREAD_GRAYSCALE)

# 수행 시간 체크 함수
def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(msg, "수행시간: %.2f ms" % elapsed)
    return ret_img

image1 = time_check(pixel_access1, "[방법1] 직접 접근 방식")
image2 = time_check(pixel_access2, "[방법2] item() 이용")
image3 = time_check(pixel_access3, "[방법3] 룩업 테이블")
image4 = time_check(pixel_access4, "[방법4] OpenCV 함수 이용")
image5 = time_check(pixel_access5, "[방법5] numpy vector화 된 연산 방식")

cv2.imshow('image', image)
cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('image3', image3)
cv2.imshow('image4', image4)
cv2.imshow('image5', image5)

cv2.waitKey(0)
cv2.destroyAllWindows()
