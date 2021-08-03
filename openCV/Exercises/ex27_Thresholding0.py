import numpy as numpy
from cv2 import cv2
import time

fst = time.time()
def nothing(x):
    pass

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\k.jfif')
myImg1 = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\k.jfif',0)
myImg = cv2.resize(myImg,(360,180))
myImg1 = cv2.resize(myImg1,(360,180))

cv2.namedWindow('TrackBar Window')
cv2.createTrackbar('TrackBar/RGB-GRAY','TrackBar Window',0,255,nothing)


while True:
    
    trackbarValue = cv2.getTrackbarPos('TrackBar/RGB-GRAY','TrackBar Window')
    _,th1RGB = cv2.threshold(myImg,trackbarValue,255,cv2.THRESH_BINARY)
    _,th2RGB = cv2.threshold(myImg,trackbarValue,255,cv2.THRESH_TRUNC)
    _,th3RGB = cv2.threshold(myImg,trackbarValue,255,cv2.THRESH_TOZERO)
    
  
    _,th1GRY = cv2.threshold(myImg1,trackbarValue,255,cv2.THRESH_BINARY)
    _,th2GRY = cv2.threshold(myImg1,trackbarValue,255,cv2.THRESH_TRUNC)
    _,th3GRY = cv2.threshold(myImg1,trackbarValue,255,cv2.THRESH_TOZERO)

    titles = ['Image/RGB','Image/GRAY','Image/RGB th-binary','Image/RGB th-trunc','Image/RGB th-tozero',
                'Image/GRAY th-binary','Image/GRAY th-trunc','Image/GRAY th-tozero']
    images = [myImg,myImg1,th1RGB,th2RGB,th3RGB,th1GRY,th2GRY,th3GRY]

    for i in range(8):
        cv2.imshow(titles[i],images[i])    
  
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
scnd = time.time()
print(scnd - fst)