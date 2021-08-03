import numpy as np
from cv2 import cv2 

def nothing(x):
    pass

#Create a black image, a window
img = np.zeros((300,400,3),np.uint8)
cv2.namedWindow('TrackBar')

#Create trackbars to for color changes
cv2.createTrackbar('R','TrackBar',0,255,nothing)
cv2.createTrackbar('G','TrackBar',0,255,nothing)
cv2.createTrackbar('B','TrackBar',0,255,nothing)

#Create switch for ON / OFF functionality
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch,'TrackBar',0,1, nothing)

while(1):
    cv2.imshow('TrackBar',img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    #get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'TrackBar')
    g = cv2.getTrackbarPos('G', 'TrackBar')
    b = cv2.getTrackbarPos('B', 'TrackBar')
    s = cv2.getTrackbarPos(switch,'TrackBar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()