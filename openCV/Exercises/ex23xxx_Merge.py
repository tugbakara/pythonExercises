from cv2 import cv2
import numpy as np

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\b.jpg')
myVid = cv2.VideoCapture(0)

myImg1 = cv2.resize(myImg,(640,480))

while(myVid.isOpened()):
    ret,frame = myVid.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        frame1 = cv2.resize(frame,(640,480))       
        mergingImgVid = cv2.addWeighted(frame1,0.6,myImg1,0.4,255)
        cv2.imshow('Merging',mergingImgVid)
    else:
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()