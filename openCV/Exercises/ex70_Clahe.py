import cv2
from matplotlib import pyplot as plt
import numpy as np
myImg = cv2.imread(r'/home/tugbakara/Desktop/Dersler/ImageProcessingdenemeleri/images/b.jpg',0)
claheObject = cv2.createCLAHE(clipLimit = 2.0 ,tileGridSize = (8,8))
cll = claheObject.apply(myImg)
cv2.imwrite(r'/home/tugbakara/Desktop/Dersler/ImageProcessingdenemeleri/savedphotos/Clahe.jpg',cll)
cv2.imshow('Clahe Img',cll)
cv2.waitKey(0)
cv2.destroyAllWindows()
