from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
import skimage 
''' to find the coordinates of the peaks (local maxima) of the white areas in the image. 
For that, we will use the function peak_local_max()from the Scikit-image library. We will apply this
function to our distance_transform image and the output will give us the markers which will be used 
in the watershed function.'''
from skimage.feature  import peak_local_max
from sklearn.cluster import KMeans
'''we are processing a much more complicated image with a large number of local maximums. In some
locations, these points will be clustered (scattered) and it will be impossible to label them. 
For example, if we now apply the function ndi.label()at multiple locations we will have local
maximums labeled with the same number. if we assign local maximum points to different clusters based on 
the distance between them. For that, we can use the K-means clustering algorithm.'''
#from scipy import ndimage as ndi
'''ndimage packages provides a number of general image processing and analysis functions that are 
designed to operate with arrays of arbitrary dimensionality. The packages currently includes: 
functions for linear and non-linear filtering, binary morphology, B-spline interpolation, and object measurements.'''

'''image segmentation is much more accurate than simple object detection. By using 
the object detection, we are detecting a set of bounding boxes that correspones to each object in 
the image. However,to obtain any information about the shape of that object we need a different
approach. As you can see, the image segmentation creates a pixel-wise mask for each object of 
interest in the image that provides us more information about that object.
we need to somehow separate these two touching objects and create a border between them. 
The idea is to create a border as far as possible from the centers of the overlapping objects. 
For this, we will use the method that works very well on rounded objects and it is called a distance transform.'''

myImg_ = cv2.imread(r'E:\ImageProcessingdenemeleri\images\moon.jfif')
#print(myImg_.shape)
myImg = cv2.resize(myImg_,(760,761))

myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(myImgG,190,255,cv2.THRESH_BINARY )
#cv2.imshow('Thresh',thresh)

kernelFilter = np.ones((3,3),np.uint8)
myImgO = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernelFilter,iterations = 2)
myImgC = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernelFilter,iterations = 2)

distTransform = cv2.distanceTransform(myImgO,cv2.DIST_L2,3)
findingWhitestImgRegion = peak_local_max(distTransform)
#findingWhitestImgRegion_boolean = peak_local_max(distTransform,indices = False)
#print(findingWhitestImgRegion_boolean)
'''This algorithm aims to cluster input data points and is one of the most straightforward and intuitive 
clustering algorithms, among many others. The input data points need to be assigned to different clusters 
based on the similarity between them. The easiest way to measure the similarity between different
objects/data points is to calculate the distance between them. The most commonly used measure of
a distance between two points is the Euclidean distance. '''
settingClusters = KMeans(n_clusters = 30)
settingClusters.fit(findingWhitestImgRegion)

findingWhitestImgRegion = settingClusters.cluster_centers_.copy()
findingWhitestImgRegion = findingWhitestImgRegion.astype(int)

distTransformCopy = distTransform.copy()
for i in range(findingWhitestImgRegion.shape[0]):
    cv2.circle(distTransformCopy,(findingWhitestImgRegion[i][1],findingWhitestImgRegion[i][0]),2,(0,255,255))
cv2.imshow('DistanceTransformCopy',distTransformCopy)

markers = np.zeros_like(distTransform)
labels = np.arange(settingClusters.n_clusters)
markers[findingWhitestImgRegion[:,0],findingWhitestImgRegion[:,1]] = labels + 1
markers = markers.astype(np.uint8)
segmentedImg = cv2.watershed(myImg,markers)
cv2.imshow('Segmented Image',segmentedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

