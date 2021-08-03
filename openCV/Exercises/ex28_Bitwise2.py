import numpy as np
from cv2 import cv2
''' cv2.getTickCount function returns the number of clock-cycles after a reference event
(like the moment machine was switched ON) to the moment this function is called. '''
perf1 = cv2.getTickCount()

Fimg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\h.jpg')
Simg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\j.jpg')
Fimg = cv2.resize(Fimg,(240,120))
Simg= cv2.resize(Simg,(240,120))

#creating ROI(Region of Image)
rows,columns,channels = Simg.shape
ROI = Fimg[0:rows, 0:columns]
cv2.imshow('ROI of Fimg',ROI)

#creating mask and inverse mask
Simg2GRY = cv2.cvtColor(Simg,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(Simg2GRY,58,255,cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)
cv2.imshow('mask Simg',mask)
cv2.imshow('InvMask Simg',maskInv)

#blacking out the area of girl in ROI
Fimg_ = cv2.bitwise_and(ROI,ROI,mask = maskInv)
cv2.imshow('Blackging out Fimg',Fimg_)

#taking only region of girl from girl image(Simg)
Simg_ = cv2.bitwise_and(Simg,Simg,mask = mask)
cv2.imshow('Taking girl Simg',Simg_)

#putting girl in ROI and modfying the main image
img = cv2.add(Fimg_,Simg_)
Fimg[0:rows,0:columns] = img
cv2.imwrite(r'E:\ImageProcessingdenemeleri\savedphotos\bitwisephoto.jpg',Fimg)
cv2.imshow('Result',Fimg)
cv2.waitKey(0)
cv2.destroyAllWindows

perf2 = cv2.getTickCount()
# cv2.getTickFrequency function returns the frequency 
# of clock-cycles, or the number of clock-cycles per second
perfTime = (perf2-perf1)/cv2.getTickFrequency()
print(perfTime)