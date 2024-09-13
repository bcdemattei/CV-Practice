import os

import cv2


img = cv2.imread(os.path.join('.', 'data', 'boid.jpeg'))#this is read into a BGR colorspace

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(img_g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30) 

cv2.imshow('img', img)
cv2.imshow('img_g', img_g)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)