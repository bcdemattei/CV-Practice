import cv2

#read webcam

webcam = cv2.VideoCapture(0)

#visualize webcam

while True: 
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): #second conditional here waits until user presses q to exit the while loop
        break ##The process is a bit slower than reading a video, so the amount of time you have to wait is slightly more complex than videos. 
              ###The amount of time you should wait depends on how long it takes for the webcam to read and fps
    
webcam.release()
cv2.destroyAllWindows()
    