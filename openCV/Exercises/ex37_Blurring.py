import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\b.jpg')
myImg = cv2.cvtColor(myImg,cv2.COLOR_BGR2RGB)

'''Most common use of smoothing/blurring in the image processing is 
removing the noises from images.
In all the filter we need to remove noises and smooth the edges.'''

kernelFilter = np.ones((7,7),np.float32)/49
final_myImg = cv2.filter2D(myImg,-5,kernelFilter) #used for homogeneous filter
myImgBlur = cv2.blur(myImg,(5,5))
myImgNorm = cv2.boxFilter(myImg,-1,(7,7))
myImgGaussian = cv2.GaussianBlur(myImg,(5,5),1)
myImgMedian = cv2.medianBlur(myImg,7)
myImgBilateral = cv2.bilateralFilter(myImg,6,66,66) #smooth yapmasına rağmen edgeler hala sharp

titles = ['Original','Filter 2D','Blurred','Gaussian','Normalized',
        'Medianed','Bilateraled']
images = [myImg,final_myImg,myImgBlur,myImgNorm,myImgGaussian,myImgMedian 
            ,myImgBilateral]

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
