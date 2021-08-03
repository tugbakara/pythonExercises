from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\n.jpg')
myImg2 = cv2.imread(r'E:\ImageProcessingdenemeleri\images\k.jfif')

print(myImg.shape)
print(myImg2.shape)
color = ('b','g','r')
myImg_ = cv2.cvtColor(myImg,cv2.COLOR_BGR2RGB)
myImg__ = cv2.cvtColor(myImg2,cv2.COLOR_BGR2RGB)
for i,col in enumerate(color):
    myImgHist = cv2.calcHist(myImg_,[i],None,[256],[0,256])
    plt.subplot(2,2,1),plt.plot(myImgHist,color = col),plt.title('Oil in Canvas Histogram')
    plt.xlim([0,256])
    myImgHist2 = cv2.calcHist(myImg__,[i],None,[256],[0,256])
    plt.subplot(2,2,2),plt.plot(myImgHist2,color = col),plt.title('Landscape Histogram')
    plt.xlim([0,256])
    plt.subplot(2,2,3),plt.imshow(myImg_)
    plt.subplot(2,2,4),plt.imshow(myImg__)
    

plt.show()
