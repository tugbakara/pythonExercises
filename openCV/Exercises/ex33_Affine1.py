import numpy as np
from cv2 import cv2

myImg_ = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\h.jpg')
myImg = cv2.resize(myImg_,(550,250))

rows,clms = myImg.shape[:2]
#shift of (100,50)
translationRatio = np.float32([[1,0,100],[0,1,50]])
#Third argument of the cv2.warpAffine() function is the 
# size of the output image, which should be in 
# the form of(width, height). Remember width = number of columns, 
# and height = number of rows.
final_myImg = cv2.warpAffine(myImg,translationRatio,(clms,rows))

cv2.imshow('Original Image',myImg)
cv2.imshow('Translated Image',final_myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()