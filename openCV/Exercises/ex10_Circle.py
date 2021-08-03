import numpy as np
import cv2

blackimg = np.zeros((200,200,3),np.uint8)
blackimg = cv2.circle(blackimg,(100,100),60,(0,150,150),1)

if cv2.waitKey(1):
    cv2.destroyAllWindows()

cv2.imshow('circle frame', blackimg)
cv2.waitKey(0)
cv2.destroyAllWindows()