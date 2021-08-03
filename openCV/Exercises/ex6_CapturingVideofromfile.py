import numpy as np
from cv2 import cv2

myvid = cv2.VideoCapture('E:\\ImageProcessingdenemeleri\\videos\\1.mp4')

while(myvid.isOpened()):
    ret,frame = myvid.read()
    print(myvid.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(myvid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1)  == ord('q'):
        break

myvid.release()
cv2.destroyAllWindows()






