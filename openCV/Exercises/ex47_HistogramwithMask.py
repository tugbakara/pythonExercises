from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\a.jpg')
myImg = cv2.cvtColor(myImg,cv2.COLOR_BGR2RGB)
mask = np.zeros(myImg.shape[:2],np.uint8)
mask[140:220,270:340] = 255
maskedImg = cv2.bitwise_and(myImg,myImg,mask = mask)

histogramWOutMask = cv2.calcHist([myImg],[0],None,[256],[0,256])
histogramWMask = cv2.calcHist([myImg],[0],mask,[256],[0,256])

plt.subplot(2,2,1),plt.plot(histogramWMask),plt.title('Histogram with Mask')
plt.xlim([0,256])
plt.subplot(2,2,2),plt.imshow(maskedImg),plt.title('Masked Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.plot(histogramWOutMask),plt.title('Histogram without Mask')
plt.xlim([0,256])
plt.subplot(2,2,4),plt.imshow(myImg),plt.title('Original Image')
plt.xticks([]),plt.yticks([])

plt.show()






