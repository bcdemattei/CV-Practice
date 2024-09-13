#thresholding

import os

import cv2


img = cv2.imread(os.path.join('.', 'data', 'boid.jpeg'))#this is read into a BGR colorspace

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_g, 80, 255, cv2.THRESH_BINARY) #All pixels below 80 will be converted to 0 and all above to 255

thresh = cv2.blur(thresh, (10,10))

cv2.imshow('img', img)
cv2.imshow('img_g', img_g)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
