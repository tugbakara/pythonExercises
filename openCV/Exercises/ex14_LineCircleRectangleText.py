import numpy as np
from cv2 import cv2

pts = np.array([[10,95],[35,125],[125,10]],np.int32)
pts = pts.reshape(-3,2,1)

blckimgFont=cv2.FONT_HERSHEY_SIMPLEX

blckimg = np.zeros((600,600,3),np.uint8)

blckimg = cv2.line(blckimg,(599,599),(0,0),(255,255,255),1)
blckimg = cv2.rectangle(blckimg,(125,125),(250,250),(0,255,0),1)
blckimg = cv2.circle(blckimg,(300,300),20,(0,0,255),1)
blckimg = cv2.ellipse(blckimg,(450,450),(50,80),0,0,360,(66,66,66),2)
blckimg = cv2.polylines(blckimg,[pts],True,(60,90,120),3)
blckimg = cv2.putText(blckimg,'Image Processing',(230,20),blckimgFont,0.5,(150,0,250),1,cv2.LINE_AA)

if cv2.waitKey(1):
    cv2.destroyAllWindows()

cv2.imshow('Frame of I.P',blckimg)

cv2.waitKey(0)
cv2.destroyAllWindows()