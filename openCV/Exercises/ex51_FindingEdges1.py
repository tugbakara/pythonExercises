from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

myVid = cv2.VideoCapture(r'E:\ImageProcessingdenemeleri\videos\8.mp4')

ret,frame1 = myVid.read()
ret,frame2 = myVid.read()

while myVid.isOpened():
    diffFrame = cv2.absdiff(frame1,frame2)
    grayFrame = cv2.cvtColor(diffFrame,cv2.COLOR_BGR2GRAY)
    bluredFrame = cv2.GaussianBlur(grayFrame,(5,5),0)
    _,maskedFrame = cv2.threshold(bluredFrame,60,255,0)
    dilatedFrame = cv2.dilate(maskedFrame,None,iterations = 80)
    contours,hierarchy = cv2.findContours(dilatedFrame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    try:
       hierarchy = hierarchy[0]           
    except:
        hierarchy = []
    
    for cnt,hier in zip(contours,hierarchy):
        area = cv2.contourArea(cnt)
        if area < 12500:
            continue
        
        left = tuple(cnt[cnt[:,:,0].argmin()][0])
        right = tuple(cnt[cnt[:,:,0].argmax()][0])
        top = tuple(cnt[cnt[:,:,1].argmin()][0])
        buttom = tuple(cnt[cnt[:,:,1].argmax()][0])
        cv2.putText(frame1,"Edge Detected",(15,25),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),1,cv2.LINE_AA)
        cv2.circle(frame1,left,5,(100,50,255),-1)
        cv2.circle(frame1,right,5,(100,50,255),-1)
        cv2.circle(frame1,top,5,(100,50,255),-1)
        cv2.circle(frame1,buttom,5,(100,50,255),-1)

    cv2.imshow('Feed',frame1)
    frame1 = frame2
    ret,frame2 = myVid.read()

    k = cv2.waitKey(1) & 0xFF
    if k == 27 :
        break

myVid.release()
cv2.destroyAllWindows()


