from cv2 import cv2
import numpy as np

myImg =cv2.imread(r'E:\ImageProcessingdenemeleri\images\r.jpg')
myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
myImgCornered = cv2.goodFeaturesToTrack(myImgG,35,0.001,10)
myImgCornered = np.int0(myImgCornered)

for i in myImgCornered:
    x,y = i.ravel()
    cv2.circle(myImg,(x,y),3,(0,0,255),-1)
    cv2.imshow('Cornered Image',myImg)

cv2.waitKey(0)
cv2.destroyAllWindows()