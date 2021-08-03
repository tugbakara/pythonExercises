import numpy as np
from cv2 import cv2

myImg1 = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\b.jpg')
myImg2 = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\b.jpg')

#generate Gaussian pyramid for img1
myImg1Copy = myImg1.copy()
myImg1GausPyr = [myImg1Copy]

for i in range(6):
    myImg1Copy = cv2.pyrDown(myImg1Copy)
    myImg1GausPyr.append(myImg1Copy)


#generate Gaussian pyramid for img2
myImg2Copy = myImg2.copy()
myImg2GausPyr = [myImg2Copy]

for i in range(6):
    myImg2Copy = cv2.pyrDown(myImg2Copy)
    myImg2GausPyr.append(myImg2Copy)


#generate Laplacian pyramid for img1
myImg1Copy = myImg1GausPyr[5]
lp_img1 = [myImg1Copy]
for i in range(5,0,-1):
    ge = cv2.pyrUp(myImg1GausPyr[i]) #gaussian expanded
    L = cv2.subtract(myImg1GausPyr[i-1],ge) #laplacian
    lp_img1.append(L)


#generate Laplacian pyramid for img2
myImg2Copy = myImg2GausPyr[5]
lp_img2 = [myImg2Copy]
for i in range(5,0,-1):
    ge = cv2.pyrUp(myImg2GausPyr[i])
    L = cv2.subtract(myImg2GausPyr[i-1],ge)
    lp_img2.append(L)


#add left and right halves of images in each level
l_r = []
for LapImg1,LapImg2 in zip(myImg1Copy,myImg2Copy):
    rows,columns,dpt = LapImg1.shape()
    #birleştirme yapıyor yatay olarak
    lr = np.hstack((LapImg1[:,0:columns/2],LapImg2[:,columns/2:]))
    l_r.append(lr)

#reconstruction
lrFinal = l_r[0]
for i in range(1,6):
    lrFinal = cv2.pyrUp(lrFinal)
    lrFinal = cv2.add(lrFinal,l_r[i])

cv2.imshow('Final Image',lrFinal)
cv2.waitKey(0)
cv2.destroyAllWindows()









