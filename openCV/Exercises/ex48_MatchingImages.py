import numpy as np
from cv2 import cv2

MyImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\i.jpeg')
MyImgG = cv2.cvtColor(MyImg,cv2.COLOR_BGR2GRAY)
tempImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\i_TEMPLATE.jpeg',0)
w,h = tempImg.shape[::-1]

matchedImg = cv2.matchTemplate(MyImgG,tempImg,cv2.TM_CCORR_NORMED)
print(matchedImg)
threshold = 0.99
locationTemp = np.where(matchedImg >= threshold)
print(locationTemp)

'''zip is used to merge 2 lists together. It returns the first element of
each list, then 2nd element of each list, etc. This is a trick to consider 
the two lists as key and data to create a dictionary.'''
for pt in zip(*locationTemp[::-1]):
    cv2.rectangle(MyImg,pt,(pt[0]+w,pt[1]+h),(255,0,0),1)

cv2.imshow('Image',MyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()



