from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

''' GRADIENT : An image gradient is a directional change in the intensity or color in an image.
These are functions to find gradients and analyze the image.
CV_64F : datatype. 
Canny is the best for edge detection!  '''

myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\r.jpg',0)

myImgSobelX = cv2.Sobel(myImg,cv2.CV_64F,1,0,ksize = 1)
myImgSobelX = np.uint8(np.absolute(myImgSobelX))
myImgSobelY = cv2.Sobel(myImg,cv2.CV_64F,0,1,ksize = 1)
myImgSobelY = np.uint8(np.absolute(myImgSobelY))
myImgLaplacian = cv2.Laplacian(myImg,cv2.CV_64F)
myImgLaplacian = np.uint8(np.absolute(myImgLaplacian))
myImgCanny = cv2.Canny(myImg,100,200)
myImgCanny = np.uint8(np.absolute(myImgCanny))
myImgSobelXYor = cv2.bitwise_or(myImgSobelX,myImgSobelY)
myImgSobelXYand = cv2.bitwise_and(myImgSobelX,myImgSobelY)
myImgSobelXNOT = cv2.bitwise_not(myImgSobelX)

titles = ["Original","Sobel X","Sobel Y","Laplacian","Canny","BITWISE OR Sobel X/Y","BITWISE AND Sobel X/Y"
        ," BITWISE NOT SobelX "]
images = [myImg,myImgSobelX,myImgSobelY,myImgLaplacian,myImgCanny,myImgSobelXYor,myImgSobelXYand,myImgSobelXNOT]

for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i], cmap = 'gray'), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show() 