import numpy as np
from cv2 import cv2

blackimg = np.zeros((200,200,3),np.uint8)

txtfont = cv2.FONT_HERSHEY_SIMPLEX
blackimgtxt = cv2.putText(blackimg, ' Image Processing',(50,100),txtfont,0.3,(200,200,200),1,cv2.LINE_AA)

if cv2.waitKey(1):
    cv2.destroyAllWindows()

cv2.imshow('Frame with text', blackimgtxt)

cv2.waitKey(0)    
cv2.destroyAllWindows()
