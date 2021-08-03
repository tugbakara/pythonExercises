import numpy as np
from cv2 import cv2

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\b.jpg')
myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)

#siftFunc = cv2.xfeatures2d.SIFT_create()
surfFunc = cv2.xfeatures2d.SURF_create()
#orbFunc = cv2.ORB_create()
keypoints,descriptors = siftFunc.detectAndCompute(myImgG,None)
'''A keypoint is the position where the feature has been detected, while the
descriptor is an array containing numbers to describe that feature.'''
myImg = cv2.drawKeypoints(myImgG,keypoints,None)
#cv2.imshow('SiftedImage',myImg)
cv2.imshow('SurfedImage',myImg)
#cv2.imshow('ORBImage',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''A blob refers to a lump. Blob analysis is image processing's most basic method 
for analyzing the shape features of an object, such as the presence, number, area,
position, length, and direction of lumps.
size = scale
In short, SURF adds a lot of features to improve the speed in every step. Analysis 
shows it is 3 times faster than SIFT while performance is comparable to SIFT.SURF is
good at handling images with blurring and rotation, but not good at handling viewpoint
change and illumination change.'''