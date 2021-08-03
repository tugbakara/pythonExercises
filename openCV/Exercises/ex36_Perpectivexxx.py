import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\r.png',0)
rows,clms = myImg.shape[:]

myImgPoints1 = np.float32([[404,395],[793,395],[793,794],[399,789]])
myImgPoints2 = np.float32([[0,0],[400,0],[0,400],[400,400]])

trasnlationRatio = cv2.getPerspectiveTransform(myImgPoints1,myImgPoints2)

final_myImg = cv2.warpPerspective(myImg,trasnlationRatio,(400,400))

plt.subplot(121) , plt.imshow(myImg,cmap = 'gray') ,plt.title('Original Image')
plt.subplot(122) , plt.imshow(final_myImg, cmap = 'gray') ,plt.title('Altered Image')
plt.show()