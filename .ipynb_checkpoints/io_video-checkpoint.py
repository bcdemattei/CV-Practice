import os
import cv2

#read video #Not writing, more complex process
video_path = os.path.join('.', 'data', 'DSC10060.mp4')

video = cv2.VideoCapture(video_path)

#visualize video

ret = True
while ret:
    ret, frame = video.read() #returns two variables. ret is boolean (if the frame is read successfuly or not)

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

video.release() #Both of these are important after calling a video
cv2.destroyAllWindows() #this is how to release allocated memory