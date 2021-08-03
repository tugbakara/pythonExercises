import numpy as np
from cv2 import cv2

def nothing(x):
    pass

myVid = cv2.VideoCapture(0)
cv2.namedWindow('Object Tracking')

cv2.createTrackbar('Lower Hue','Object Tracking',0,255,nothing)
cv2.createTrackbar('Lower Saturation','Object Tracking',0,255,nothing)
cv2.createTrackbar('Lower Value','Object Tracking',0,255,nothing)

cv2.createTrackbar('Upper Hue','Object Tracking',0,255,nothing)
cv2.createTrackbar('Upper Saturation','Object Tracking',0,255,nothing)
cv2.createTrackbar('Upper Value','Object Tracking',0,255,nothing)

while(myVid.isOpened()):
    _,frame = myVid.read()
    frame = cv2.flip(frame,1)
    
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowh = cv2.getTrackbarPos('Lower Hue','Object Tracking')
    lows = cv2.getTrackbarPos('Lower Saturation','Object Tracking')
    lowv = cv2.getTrackbarPos('Lower Value','Object Tracking')

    upperh = cv2.getTrackbarPos('Upper Hue','Object Tracking')
    uppers = cv2.getTrackbarPos('Upper Saturation','Object Tracking')
    upperv = cv2.getTrackbarPos('Upper Value','Object Tracking')

    l_color = np.array([lowh,lows,lowv])
    u_color = np.array([upperh,uppers,upperv])
        
    hsv_mask = cv2.inRange(hsv_frame,l_color,u_color)
    OTracking = cv2.bitwise_and(frame,frame,mask = hsv_mask)
    cv2.imshow('OTracking',OTracking)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break    

# WHITE : 0,0,177-255,40,255
# BLUE : 35,56,37-114,255,255
myVid.release()
cv2.destroyAllWindows()
    


