import os

import cv2

import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'boid.jpeg'))

img_e = cv2.Canny(img, 100, 200)

img_e_d = cv2.dilate(img_e, np.ones((3,3), dtype=np.int8))

img_e_e = cv2.erode(img_e_d, np.ones((3,3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('img_e', img_e)
cv2.imshow('img_e_d', img_e_d)
cv2.imshow('img_e_e', img_e_e)
cv2.waitKey(0)

##Setting the Canny parameters, trial & error