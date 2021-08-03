import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2

def nothing(x):
    pass

''' Canny edge detection algorithm is composed of 5 steps:
--Noise Reduction : to smooth the image 
--Gradient Calculation : to find  intensity gradient
--Non-max suppression : to get rid of superiors response to edge detection
--Double Thresholding : to determine the potential edges (providing for 5th step)
--Edge Tracking by Hysteresis : to track edges
Canny is the best for edge detection! '''

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\o.jpg',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Canny Image')
TrackBar1_ = cv2.createTrackbar("1st Threshold",'Canny Image',0,255,nothing)
TrackBar2_ = cv2.createTrackbar("2nd Threshold",'Canny Image',0,255,nothing)

while True:
    TrackBar1 = cv2.getTrackbarPos("1st Threshold",'Canny Image')
    TrackBar2 = cv2.getTrackbarPos("2nd Threshold",'Canny Image')
    myImgCanny = cv2.Canny(myImg,TrackBar1,TrackBar2)
    cv2.imshow('Canny Image',myImgCanny)
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

