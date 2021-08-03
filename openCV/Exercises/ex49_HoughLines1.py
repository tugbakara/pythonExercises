import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

''' every point in mc space is a line.
Hough transformation algorithm:
--Edge detection using Canny edge detector/or any edge detecion method.
--Mapping of edge points to Hough space and storage in an accumulator.
--Interpretation of the accumulator to yield lines of infnite length.The interpretation is done by
thresholding and possibly other constraints.
--Conversion of infinite lines to finite lines.
OpenCV implements two kind of Hough line transforms:
1- The standard Hough Transform (HoughLines)
2- The probabilistic Hough Line Transform (HoughLinesP)
'''
myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\r.jpg')
myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
'''plt.imshow(myImgG)
plt.show()
print(myImgG.shape) '''
#siyah bir image oluşturup ROI bölgesinin koordinatlarını zerosların içinealıyoruz. ones olarak 
#değiştiriyoruz ve sonra bitwise and operatörü ile de mask edip istediğimiz bölgeyi sudokuda 
mask = np.zeros((680,1023),np.uint8)
myROI = [(92,159),(715,54),(959,475),(204,646)]
mask = cv2.fillPoly(mask,[np.array(myROI)],1)

maskedImg = cv2.bitwise_and(myImg,myImg,mask = mask) 
myImgEdges = cv2.Canny(maskedImg,100,200,apertureSize = 3)
myImgLines = cv2.HoughLinesP(myImgEdges,1,np.pi/180,90,minLineLength = 95 ,maxLineGap = 15)
for line in myImgLines:
    x1,y1,x2,y2 = line[0]
    cv2.line(myImg,(x1,y1),(x2,y2),(0,255,255),1)

cv2.imshow('Image with Lines',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()