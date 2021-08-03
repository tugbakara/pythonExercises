from cv2 import cv2
import numpy as np

my_img = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\j.jpg', -1)
print(my_img.shape)
scalePercent = 0.5
wmy_img = int(my_img.shape[0]*scalePercent)
hmy_img = int(my_img.shape[1]*scalePercent)
print(wmy_img)
print(hmy_img)
dsize = (hmy_img,wmy_img)
my_img = cv2.resize(my_img,dsize,)
my_img = cv2.line(my_img,(470,0),(470,960),(255,255,255),2)
cv2.imshow('Frame',my_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
