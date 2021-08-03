import numpy as np
import cv2

points = np.array([[10,160],[60,70],[90,150],[40,40],[65,65],[80,80]], np.int32)
points = points.reshape((-4,1,2))

blackimg = cv2.polylines(blackimg,[points],True,(255,255,0))

if cv2.waitKey(1):
    cv2.destroyAllWindows()

cv2.imshow('polylines frame', blackimg)

cv2.waitKey(0)
cv2.destroyAllWindows()