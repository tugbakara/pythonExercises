from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

#matplotlib'de RGB sıralaması vardır ama openCV'de BGR.
r =[255,0,0]

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\b.jpg')

cnst = cv2.copyMakeBorder(myImg,20,20,10,10,cv2.BORDER_CONSTANT,value=r)
plt.imshow(cnst,'gray'), plt.title('Consant Border')

plt.show()