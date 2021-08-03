import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\r.jpg')

myImg64I = cv2.Sobel(myImg,cv2.CV_64F,1,0,ksize = 3)
myImg8UI = cv2.Sobel(myImg, cv2.CV_8U,1,0,ksize = 3)
myAbsolute64UI = np.absolute(myImg64I)
myAbsoluteSobel8UI = np.uint8(myAbsolute64UI)

titles = ['Original','Sobel 64 UI','Sobel 8 UI','Absolute Sobel 8 UI']
images = [myImg,myImg64I,myImg8UI,myAbsoluteSobel8UI]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i]) ,plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()    
