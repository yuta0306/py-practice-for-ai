import numpy as np
import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")

# sample.jpg をぼかしてください
my_img = cv2.GaussianBlur(img, (31, 31), 0)

cv2.imshow("sample", my_img)