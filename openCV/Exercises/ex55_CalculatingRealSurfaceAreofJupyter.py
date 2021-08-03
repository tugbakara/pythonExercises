import numpy as np
from cv2 import cv2
import math as m

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\jupiter.jpg',cv2.IMREAD_COLOR)
#myImg = cv2.resize(myImg,(455,300),)

myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
myImgBlurred = cv2.blur(myImgG,(3,3))
detectedJupyter = cv2.HoughCircles(myImgBlurred,cv2.HOUGH_GRADIENT,1,30,param1 = 50,param2 = 60,minRadius = 140,maxRadius = 300)
if detectedJupyter is not None:
    detectedJupyter = np.uint16(np.around(detectedJupyter))
    for points in detectedJupyter[0,:]:
        x,y,r = points[0],points[1],points[2]
        print(r)
        ppm = 69911 / 225 # 69911 km(yarıçap) ye denk gelen piksel (r) sayısı 225 ise 1 kmye denk geleni bulduk. 
        cv2.circle(myImg,(x,y),r,(0,255,255),1)
        surfaceArea = 4*m.pi*m.pow(r*ppm,2) 
        
        
print(surfaceArea)
cv2.imshow('Detected Jupyter',myImg)
cv2.waitKey(0)
cv2.destroyAllWidows() 
        