import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg1 = cv2.imread(r'E:\ImageProcessingdenemeleri\images\matching1.JPG',0) 
myImg2 = cv2.imread(r'E:\ImageProcessingdenemeleri\images\matching2.JPG',0)

siftDetectorObject = cv2.xfeatures2d.SIFT_create()
keypoints1,descriptors1 = siftDetectorObject.detectAndCompute(myImg1,None)
keypoints2,descriptors2 = siftDetectorObject.detectAndCompute(myImg2,None)
MIN_MATCH_COUNT = 10
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE,trees = 5)
search_params = dict(checks = 50)

flannMatcherObject = cv2.FlannBasedMatcher(index_params,search_params)
matches = flannMatcherObject.knnMatch(descriptors1,descriptors2,k = 2)

goodMatches = []
for m,n in matches:
    if m.distance < 0.6*n.distance:
        goodMatches.append(m)

if len(goodMatches) > MIN_MATCH_COUNT:
    sourcePoints = np.float32([keypoints2[m.queryIdx].pt for m in goodMatches ]).reshape(-1,1,2)
    destinationPoints = np.float32([ keypoints2[m.trainIdx].pt for m in goodMatches ]).reshape(-1,1,2) 
    
    M, mask = cv2.findHomography(sourcePoints,destinationPoints,cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    
    h,w = myImg1.shape
    points = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).respahe(-1,1,2)
    destination = cv2.perspectiveTransform(points,M)
    myImg2 = cv2.polylines(myImg2,[np.int32(destination)],True,255,3,cv2.LINE_AA)
else:
    print("Not enough matches are found %d / %d " %(len(goodMatches),MIN_MATCH_COUNT))
    matchesMask = None

draw_params = dict( matchColor = (0,255,255),
                    singlePointColor = None,
                    matchesMask = matchesMask,
                    flags = 2)

myImg3 = cv2.drawMatches(myImg1,keypoints1,myImg2,keypoints2,goodMatches,None,**draw_params)
plt.imshow(myImg3, 'gray'), plt.show()

