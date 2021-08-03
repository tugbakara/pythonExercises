import numpy as np
from cv2 import cv2

''' The contours are a useful tool for shape analysis and object detection and recognition. '''
myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\r.jpg')
#cv2.resize(myImg,(480,360))
myImgGray = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(myImgGray ,127,255,0)
contours,hierarchy = cv2.findContours(mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_TC89_L1)
print("Number of contours : "+ str(len(contours)))
print(contours[0])

myImg = cv2.drawContours(myImg,contours,-1,(0,255,255),1)

cv2.imshow('Image with Contours',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()