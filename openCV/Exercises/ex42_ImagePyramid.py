import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt
import argparse

'''Sometimes we need to work images with different resolutions. For example,
If we have an image and we want to search faces inside the image these faces can be
different with each other some of them are small compare to others using pyramids we 
can detect all of the faces thanks to pyramid functions.
pyrDown and pyrUp are the Gaussian's'''

'''Argument parser kodumuzu değiştirmeden programımıza anında farklı girdiler vermemizi 
sağlar. Sürekli script üstünde bir dosyanın yolunu göstermek için değişiklik yapmanıza 
gerek kalmayacak. Argümanlarınızı terminal üzerinden verip keyfinize bakacaksınız. '''
myImg = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\b.jpg',cv2.IMREAD_GRAYSCALE)

myImgPyramidD = cv2.pyrDown(myImg) #decreases the resolution
myImgPyramidD2 = cv2.pyrDown(myImgPyramidD)
myImgPyramidU = cv2.pyrUp(myImg) #increases the resolution
myImgPyramidU2 = cv2.pyrUp(myImgPyramidU)
myImgPyramidU3 = cv2.pyrUp(myImgPyramidD)
myImgPyramidD3 = cv2.pyrDown(myImgPyramidU)
myImgPyrLaplacianD = cv2.Laplacian(myImgPyramidD,cv2.CV_64F)
myImgPyrLaplacianU = cv2.Laplacian(myImgPyramidU,cv2.CV_64F)

titles = ['Original','Down','Down2','Up','Up2','Up3','Down3','Laplacian Pyramid UP',
            'Laplacian Pyramid DOWN']
images = [myImg,myImgPyramidD,myImgPyramidD2,myImgPyramidU,
            myImgPyramidU2,myImgPyramidU3,myImgPyramidD3,myImgPyrLaplacianU,myImgPyrLaplacianD]

for i in range(9):
    cv2.imshow(titles[i],images[i])

cv2.waitKey(0)
cv2.destroyAllWindows() 