import numpy as np
from cv2 import cv2

#OpenCV provides two transformation functions,cv2.warpAffin and 
# cv2.warpPerspective, with which you can have all kinds of transformations.
# cv2.warpAffin takes a 2x3 transformation matrix while cv2.warpPerspective 
# takes a 3x3 transformation matrix as input.

myImg_ = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\h.jpg')
myImg = cv2.resize(myImg_,(350,200))
HmyImg,WmyImg = myImg.shape[:2]
scaled_myImg = cv2.resize(myImg,(2*HmyImg,2*WmyImg),interpolation= cv2.INTER_CUBIC)

cv2.imshow('Original Image',myImg)
cv2.imshow('Scaled Image',scaled_myImg)

cv2.waitKey(0)
cv2.destoyAllWindows()