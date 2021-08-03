import numpy as np
from cv2 import cv2

myVid  = cv2.VideoCapture(r'E:\ImageProcessingdenemeleri\videos\1.webm')

while(myVid.isOpened()):
    ret, frame = myVid.read()  
   
    grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edgeImg = cv2.Canny(grayImg,200,250) 
    mask = np.zeros((720,1280),np.uint8)
    roivertices = [(0,720),(480,540),(800,540),(1280,720)]
    mask = cv2.fillPoly(mask,[np.array(roivertices)],1)
    maskedImg = cv2.bitwise_and(edgeImg,edgeImg,mask = mask)    
    lines = cv2.HoughLinesP(maskedImg,6,np.pi/180,30,np.array([]),10,60)
    
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,255),2)

    cv2.imshow('Video',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

myVid.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

    
