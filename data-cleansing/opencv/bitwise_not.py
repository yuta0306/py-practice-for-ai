import numpy as np
import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")

# OpenCVで色を反転します
my_img = cv2.bitwise_not(img)

cv2.imshow("sample", my_img)