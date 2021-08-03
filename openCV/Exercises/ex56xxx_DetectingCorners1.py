from cv2 import cv2
import numpy as np

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\r.jpg')
myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
'''myImgG = np.float32(myImgG)
mask = np.zeros((680,1023),np.uint8)
myROI = [(92,159),(715,54),(959,475),(204,646)]
mask = cv2.fillPoly(mask,[np.array(myROI)],1)
maskedImg = cv2.bitwise_and(myImg,myImg,mask = mask)
maskedImg = np.float32(maskedImg)'''
corneredImg = cv2.cornerHarris(np.float32(myImgG),3,1,0.246)
dilatedCornerImg = cv2.dilate(corneredImg,None)
dilatedCornerImg = np.uint8(dilatedCornerImg)
ret,labels,stats,centroids = cv2.connectedComponentsWithStats
myImg[dilatedCornerImg > 0.01*dilatedCornerImg.max()] = [0,255,255]
cv2.imshow('Cornered Image', myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()