from cv2 import cv2
import numpy as np

myImg_ = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\h.jpg')
myImg = cv2.resize(myImg_,(550,250))

rows,clms = myImg.shape[:2]
rotationRatio = cv2.getRotationMatrix2D((clms/2,rows/2),90,0.8)
rotatedmyImg = cv2.warpAffine(myImg,rotationRatio,(clms,rows))

cv2.imshow('Original Image',myImg)
cv2.imshow('Rotated Image',rotatedmyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()