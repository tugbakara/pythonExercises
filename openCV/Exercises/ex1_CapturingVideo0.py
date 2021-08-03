import numpy as np
import cv2

myVideo = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #codec part
smyVideo = cv2.VideoWriter('mysavedvideo11.mp4',fourcc,20.0,(640,480)) # VideoWriter object


while(myVideo.isOpened()):
    ret,frame = myVideo.read()
    if ret == True:
        frame = cv2.flip(frame,2)
        smyVideo.write(frame)      
    
        cv2.imshow('video frame',frame)         

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

myVideo.release()
smyVideo.release()
cv2.destroyAllWindows()

