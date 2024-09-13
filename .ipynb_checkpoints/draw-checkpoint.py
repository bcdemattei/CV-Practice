import os

import cv2

img = cv2.imread(os.path.join('.','data','boid.jpeg'))

print(img.shape)

#line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (250, 200), (450, 500), (255, 0, 0), -1)

#circle
cv2.circle(img, (400, 260), 150, (255,0,255), 5)

#text
cv2.putText(img, 'Hey f*****!', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 10)

cv2.imshow('img',img)
cv2.waitKey(0)