import numpy as np
from cv2 import cv2

def draw(event,x,y,flags,param):
    txtfont = cv2.FONT_ITALIC      
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),16,(26,250,5),1)    
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+20,y+20),(10,110,210),1)
    elif event == cv2.EVENT_MOUSEWHEEL:
        cv2.putText(img,"Am I looking like a robot?",(30,100),txtfont,0.35,(255,255,55),1,cv2.LINE_AA)
            
img = np.zeros((200,200,3),np.uint8)

cv2.namedWindow('I.P project')


while(1):
    cv2.setMouseCallback('I.P project',draw)
    cv2.imshow('I.P project',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()