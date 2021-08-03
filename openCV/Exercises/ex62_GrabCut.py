from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\l.jpg')
print(myImg.shape)
#myImg = cv2.resize(myImg,(1024,768)) farklı bir fotoğraf içind,
myImg = cv2.cvtColor(myImg,cv2.COLOR_BGR2RGB)
#plt.imshow(myImg)
#plt.show()
mask = np.zeros(myImg.shape[:2],np.uint8)
bdgModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rectArea = (388,235,400,300)
cv2.grabCut(myImg,mask,rectArea,bdgModel,fgdModel,2,cv2.GC_INIT_WITH_RECT)
'''Pixels are put into 4 classes.

--background (0)

--foreground (1)

--probably background (2)

--probably foreground (3)'''
mask2 = np.where((mask == 2) | (mask == 0),0,1).astype('uint8') #mask 2 veya 1 0 yap yani background eğer değilse de 1 yap.
myImgNew = myImg*mask2[:,:,np.newaxis]
#cv2.imshow('Resized Image',myImg)
plt.imshow(myImgNew)
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()