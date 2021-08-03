import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\a.jpg',0)
rows,clms = myImg.shape[:2]

myImgPoints1 = np.float32([[60,60],[160,60],[60,90]])
myImgPoints2 = np.float32([[350,35],[300,200],[190,30]])

translationRatio = cv2.getAffineTransform(myImgPoints1,myImgPoints2)
final_myImg = cv2.warpAffine(myImg,translationRatio,(clms,rows))

plt.subplot(121), plt.imshow(myImg,cmap = 'gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(final_myImg, cmap = 'gray'), plt.title('Altered Image')
plt.show()
