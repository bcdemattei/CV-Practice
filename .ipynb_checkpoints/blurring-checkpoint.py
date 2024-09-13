import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'boid.jpeg'))

#classical blur
k_size = 7
img_blur = cv2.blur(img,(k_size, k_size))

#gaussian
img_gaus = cv2.GaussianBlur(img, (k_size, k_size), 3) 

#median
img_med = cv2.medianBlur(img, k_size)


cv2.imshow('img', img)
cv2.imshow('blur_img', img_blur)
cv2.imshow('gaus_img', img_gaus)
cv2.imshow('med_img', img_med)
cv2.waitKey(0)