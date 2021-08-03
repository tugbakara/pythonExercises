import numpy as np
from cv2 import cv2


# mouse callback function
class MouseMovement(object):
    def __init__(self,x,):
        self.cv2.setMouseCallback('I.P project')
        self.draw_circle()
        self.draw_rectangle()
       
    def draw_circle(self,event,x,y,flags,param):
        
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(self,img,(x,y),66,(255,255,255),1)
        
    def draw_rectangle(self,event,x,y,flags,param):
        
        if event == cv2.EVENT_RBUTTONDBLCLK:
            cv2.rectangle(self,img,(x,y),(x+20,y+20),(200,200,200),1)


img = np.zeros((200,200,3),np.uint8)
obj=MouseMovement(img)

cv2.namedWindow('I.P project')

while(1):
    cv2.imshow('I.P project',obj)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
