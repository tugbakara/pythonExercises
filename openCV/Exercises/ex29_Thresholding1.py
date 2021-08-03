import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg = cv2.imread('E:\\Arkadaslarailekitapdosya\\DERSLER\\manyetiknotlarzekiye\\aa.jpeg',0)
_,th0 = cv2.threshold(myImg,101,255,cv2.THRESH_BINARY)
th1 = cv2.adaptiveThreshold(myImg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,17,2)
th2 = cv2.adaptiveThreshold(myImg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,17,2)

titles = ['Threshold','Adaptive Threshold with Mean','Adaptive Threshold with Gaussian']
images = [th0,th1,th2]

plt.imshow(images[0],'gray')
plt.title(titles[0])
plt.show()
plt.imshow(images[1],'gray')
plt.title(titles[1])
plt.show()
plt.imshow(images[2],'gray')
plt.title(titles[2])
plt.show()

