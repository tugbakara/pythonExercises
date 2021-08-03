import numpy as np
from cv2 import cv2

drawing = False #True if mouse pressed
mode = True #If True,draw rectangle .Press m to toggle to curve.
ix,iy = 0,0

#mouse callback function:
def drawWithMouse(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,255),1)
            else:
                cv2.circle(img,(x,y),6,(255,0,0),1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv2.circle(img,(x,y),16,(0,0,255),1)
            
img = np.zeros((600,600,3),np.uint8)
cv2.namedWindow('IP')
cv2.setMouseCallback('IP',drawWithMouse)

while(1):
    cv2.imshow('IP',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()