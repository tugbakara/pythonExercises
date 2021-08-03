import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg1 = cv2.imread(r'E:\ImageProcessingdenemeleri\images\matching1.JPG',0)
myImg2 = cv2.imread(r'E:\ImageProcessingdenemeleri\images\matching2.JPG',0)

siftObjectDetector = cv2.xfeatures2d.SIFT_create()

keypoints1,descriptors1 = siftObjectDetector.detectAndCompute(myImg1,None)
keypoints2,descriptors2 = siftObjectDetector.detectAndCompute(myImg2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
search_params = dict(checks = 50)

flannObject = cv2.FlannBasedMatcher(index_params,search_params)
matches = flannObject.knnMatch(descriptors1,descriptors2,k = 2)

#need to draw only good matches,so create a mask:
matchesMask = [[0,0] for i in range(len(matches))]
for i,(m,n) in enumerate(matches):
    if m.distance < 0.6*n.distance:
        matchesMask[i] = [0,1]

draw_params = dict(matchColor = (255,0,255),
                singlePointColor = (255,255,0),
                matchesMask = matchesMask,
                flags = 0)

myImg3 = cv2.drawMatchesKnn(myImg1,keypoints1,myImg2,keypoints2,matches[:10],None,**draw_params)
plt.imshow(myImg3),plt.show()



