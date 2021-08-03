from cv2 import cv2
import numpy as np

myImg0 = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\d.jpg')
myImg1 = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\k.jfif')

myImg0= cv2.resize(myImg0,(560,360))
myImg1= cv2.resize(myImg1,(560,360))

newImg = cv2.addWeighted(myImg0,0.5,myImg1,0.5,0)

cv2.imshow('Weighted Image', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()