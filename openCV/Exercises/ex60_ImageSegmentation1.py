import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
#Image segmentation is dividing the image into various regions and boundraries of the region is marked.
myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\m.jpg')
print(myImg.shape)
myImg = cv2.resize(myImg,(762,760))
#myImg = cv2.cvtColor(myImg, cv2.COLOR_BGR2RGB)
myImg_ = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(myImg_,110,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
myImgO = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,(3,3),iterations = 2)
myImgC = cv2.morphologyEx(myImgO,cv2.MORPH_CLOSE,(3,3),iterations = 10)

exactBG = cv2.dilate(myImgC,(3,3),iterations = 5)
disTransform = cv2.distanceTransform(myImgC,cv2.DIST_L1,5)
print(disTransform.max())
_,exactFG = cv2.threshold(disTransform,0.45*disTransform.max(),255,0)
exactFG = np.uint8(exactFG)
unknownRegion = cv2.subtract(exactBG,exactFG)
_,markerLabel = cv2.connectedComponents(exactFG)
markerLabel = markerLabel + 1
markerLabel[unknownRegion == 255] = 0
markerLabel = cv2.watershed(myImg,markerLabel)
myImg[markerLabel == -1] = [255,0,0]
cv2.imshow('Segmented Image',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' titles = ['Distance Transform Image','Segmented Image']
images = [disTransform,myImg]
for i in range(2):
    plt.subplot(1,2,i+1) , plt.imshow(images[i]) , plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])
plt.show() '''
