from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt


myNoisyImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\p.jpg',0)


#global thresholding
ret1,fmyNoisyImg = cv2.threshold(myNoisyImg,120,255,cv2.THRESH_BINARY)

#OTSU's thresholding
ret2,smyNoisyImg = cv2.threshold(myNoisyImg,0,255,(cv2.THRESH_BINARY + cv2.THRESH_OTSU))

#OTSU's thresholding after Gaussian filtering
gfmyNoisyImg = cv2.GaussianBlur(myNoisyImg,(5,5),0) 
ret3,tmyNoisyImg = cv2.threshold(gfmyNoisyImg,0,255,(cv2.THRESH_BINARY+cv2.THRESH_OTSU))

#plot all the images

images = [myNoisyImg,0,fmyNoisyImg,
          myNoisyImg,0,smyNoisyImg,
          gfmyNoisyImg,0,tmyNoisyImg]

titles = ['Original Noisy Image','Histogram','Global Thresholded Image',
           'Original Noisy Image','Histogram',"Otsu's Thresholding",
           'Gaussian Filtering Image','Histogram',"Otsu's Image after Gaussian Filtering"]

for i in range(3):
    plt.subplot(3,3,i*3+1) ,  plt.imshow(images[i*3],cmap = 'gray')
    plt.title(titles[i*3]) , plt.xticks([]) , plt.yticks([])
    plt.subplot(3,3,i*3+2) ,  plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]) , plt.xticks([]) , plt.yticks([])
    plt.subplot(3,3,i*3+3) ,  plt.imshow(images[i*3+2], cmap = 'gray')
    plt.title(titles[i*3+2]) , plt.xticks([]) , plt.yticks([])

plt.show()




