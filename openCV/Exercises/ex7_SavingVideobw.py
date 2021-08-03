import numpy as np
from cv2 import cv2

myVideo = cv2.VideoCapture(0)
codecvid = cv2.VideoWriter_fourcc(*'MJPG') #codec part

smyVideo = cv2.VideoWriter('C:\\Users\\lenovo\\Desktop\\Image Processing\\savedvideos\\my1stsaved.mp4',codecvid,20.0,(640,480)) # VideoWriter object


while(myVideo.isOpened()):
    ret,frame = myVideo.read()
    if ret == True:
        grayvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayvid = cv2.flip(grayvid,1)
        smyVideo.write(grayvid)      
    
        cv2.imshow('video',grayvid)         

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

myVideo.release()
smyVideo.release()
cv2.destroyAllWindows()

