import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\h.jpg',0)
fastObject = cv2.FastFeatureDetector_create()
keyPoints = fastObject.detect(myImg,None)
myImgWSupp = cv2.drawKeypoints(myImg,keyPoints,None,color = (255,0,0))
cv2.imwrite(r'E:\ImageProcessingdenemeleri\savedphotos\FastedImgWSupp.jpg',myImgWSupp)
fastObject.setNonmaxSuppression(False)
keyPoints = fastObject.detect(myImg,None)
myImgWoutSupp = cv2.drawKeypoints(myImg,keyPoints,None,color = (255,0,0))
cv2.imwrite(r'E:\ImageProcessingdenemeleri\savedphotos\FastedImgWOutSupp.jpg',myImgWoutSupp)


'''It is several times faster than other existing corner detectors.
But it is not robust to high levels of noise. It is dependant on a threshold.
Actually it's help for detecting corners.'''