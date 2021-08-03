import numpy as np
from cv2 import cv2

blckimg = np.zeros((600,600,3),np.uint8)

blckimg = cv2.ellipse(blckimg,(300,130),(65,65),135,0,270,(0,0,255),40)
blckimg = cv2.ellipse(blckimg,(190,290),(65,65),10,0,270,(0,255,0),40)
blckimg = cv2.ellipse(blckimg,(410,290),(65,65),315,0,270,(255,0,0),40)

txtfont = cv2.FONT_HERSHEY_SIMPLEX
blckimg = cv2.putText(blckimg, 'OpenCV' ,(100,560),txtfont,3.5,(255,255,255),8,cv2.LINE_AA)


while(1):
    cv2.imshow('OpenCV frame',blckimg)
    if cv2.waitKey(1) & 0xFF == ord('q' or 'Q'):
        break

cv2.destroyAllWindows()
