import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\h.jpg',0)
starDetectorObject = cv2.FastFeatureDetector_create("STAR")
briefExtractor = cv2.DescriptorExtractor_create("BRIEF")
keyPoints = starDetectorObject.detect(myImg,None)
keyPoints, desciptors = briefExtractor.compute(myImg,keyPoints)
myImg2 = cv2.drawKeypoints(myImg,keyPoints,None,color = (255,0,0))
cv2.imwrite(r'E:\ImageProcessingdenemeleri\savedphotos\BriefedImg.jpg',myImg2)


