import numpy as np
import cv2

blackimg = np.zeros((200,200,3),np.uint8)

blackimg = cv2.rectangle(blackimg,(45,10),(90,190),(0,200,100),1)

if cv2.waitKey(1):
    cv2.destroyAllWindows()
    
cv2.imshow('Rectangle frame', blackimg)

cv2.waitKey(0)    
cv2.destroyAllWindows()
    
