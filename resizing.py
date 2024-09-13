import os

import cv2

img = cv2.imread(os.path.join('.', 'data','bird_out.jpg'))

resized_img = cv2.resize(img,(540, 560))

print(img.shape) #(1080, 1920, 3)
print(resized_img.shape) #(540, 560, 3)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)