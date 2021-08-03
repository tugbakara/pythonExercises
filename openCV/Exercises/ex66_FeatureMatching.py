import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg1_ = cv2.imread(r'E:\ImageProcessingdenemeleri\images\matching1.JPG')
myImg2_ = cv2.imread(r'E:\ImageProcessingdenemeleri\images\matching2.JPG')
myImg1 = cv2.cvtColor(myImg1_,cv2.COLOR_BGR2GRAY)
myImg2 = cv2.cvtColor(myImg2_,cv2.COLOR_BGR2GRAY)
#orbObjectDetector = cv2.ORB_create()
siftObjectDetector = cv2.xfeatures2d.SIFT_create()
#keypoints1,descriptors1 = orbObjectDetector.detectAndCompute(myImg1,None)
#keypoints2,descriptors2 = orbObjectDetector.detectAndCompute(myImg2,None)
keypoints1,descriptors1 = siftObjectDetector.detectAndCompute(myImg1,None)
keypoints2,descriptors2 = siftObjectDetector.detectAndCompute(myImg2,None)
bfmMatcher = cv2.BFMatcher_create()
#matches = bfmMatcher.match(descriptors1,descriptors2)
#matches = sorted(matches, key = lambda x : x.distance)
matches = bfmMatcher.knnMatch(descriptors1,descriptors2,k = 2)

goodMatches = []
for m,n in matches:
    if m.distance < 0.6* n.distance:
        goodMatches.append([m])

# myImg3 = cv2.drawMatches(myImg1,keypoints1,myImg2,keypoints2,matches[:15],None)
myImg3 = cv2.drawMatchesKnn(myImg1,keypoints1,myImg2,keypoints2,goodMatches,None,flags = 2)
plt.imshow(myImg3),plt.show()