import numpy as np
import cv2

blackimg = np.zeros((200,200,3),np.uint8)
blackimg = cv2.ellipse(blackimg,(100,100),(66,36),0,0,360,(255,0,0),1)

if cv2.waitKey(1):
    cv2.destroyAllWindows()

cv2.imshow('Ellipse frame',blackimg)

cv2.waitKey(0)
cv2.destroyAllWindows()