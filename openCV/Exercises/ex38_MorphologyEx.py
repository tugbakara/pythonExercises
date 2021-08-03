from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\s.jpg',0)
myImgKernelFilter = np.ones((5,5),np.uint8)
myImgKernelFilter2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
''' iteration is the number of times we want to perform dilation-erosion etc. on an image
 When the erosion is applied the kernel filter we define slides through all the image 
 and pixel on the  original image either one or zero will be considered
 as one only if all the pixels under the kernel is one otherwise it is eroded and this means
 pixels set the zero '''
myImgErosion = cv2.erode(myImg,myImgKernelFilter,iterations = 1)
myImgDilation = cv2.dilate(myImg,myImgKernelFilter)
myImgOpenning = cv2.morphologyEx(myImg,cv2.MORPH_OPEN,myImgKernelFilter)
myImgOpenning2 = cv2.morphologyEx(myImg,cv2.MORPH_OPEN,myImgKernelFilter2)
myImgErosion2 = cv2.morphologyEx(myImg,cv2.MORPH_ERODE,myImgKernelFilter)
myImgClosing = cv2.morphologyEx(myImg,cv2.MORPH_CLOSE,myImgKernelFilter)
myImgMorpGradient = cv2.morphologyEx(myImg,cv2.MORPH_GRADIENT,myImgKernelFilter)
myImgTopHat = cv2.morphologyEx(myImg,cv2.MORPH_TOPHAT,myImgKernelFilter)
myImgBlackHat = cv2.morphologyEx(myImg,cv2.MORPH_BLACKHAT,myImgKernelFilter)
myImgHitmiss = cv2.morphologyEx(myImg,cv2.MORPH_HITMISS,myImgKernelFilter,iterations = 1)

titles = ["Original Image","Erosion Filtering","Dilation Filtering","Openning Filtering",
            "Erosion2 Filtering","Closing Filtering","Morphological Gradient Filtering",
            "TopHat Filtering","BlackHat Filtering","Hitmiss Filtering"]

images = [ myImg,myImgErosion,myImgDilation,myImgOpenning,myImgOpenning2,myImgErosion2,myImgClosing,
            myImgMorpGradient,myImgTopHat,myImgBlackHat,myImgHitmiss]

for i in range(10):
    plt.subplot(3,4,i+1), plt.imshow(images[i], cmap = 'gray'),plt.title(titles[i])

plt.show()
