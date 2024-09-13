import os
import cv2

#read image
image_path = os.path.join('.', 'data', 'DSC10059.JPG')

img = cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join('.', 'data', 'bird_out.JPG'), img)

#visualize image
cv2.imshow('image', img)
cv2.waitKey(0) #telling openCV to wait until a key is pressed