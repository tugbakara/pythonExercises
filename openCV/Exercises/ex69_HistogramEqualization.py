import cv2
from matplotlib import pyplot as plt
import numpy as np 

'''As a result, this is used as a “reference tool” to make all
images with same lighting conditions. This is useful in many cases. For example, in face recognition,
before training the face data, the images of faces are histogram equalized to make them all with same
lighting conditions. '''

myImg = cv2.imread(r'/home/tugbakara/Desktop/Dersler/ImageProcessingdenemeleri/images/b.jpg',0)
#myImg = cv2.cvtColor(myImg,cv2.COLOR_BGR2RGB)
hist, bins = np.histogram(myImg.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m-cdf_m.min())*255/(cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
myImg2 = cdf[myImg]
plt.subplot(2,2,1),plt.plot(cdf, color = 'b') ,plt.hist(myImg2.flatten(),256,[0,256],color = 'r')
plt.legend(('cdf','histogram'),loc = 'upper left')
plt.xlim([0,256])
plt.subplot(2,2,2),plt.imshow(myImg2)
plt.show()

#with openCV
equalizedImg = cv2.equalizeHist(myImg)
resultImg = np.hstack((myImg,equalizedImg))
cv2.imwrite(r'/home/tugbakara/Desktop/Dersler/ImageProcessingdenemeleri/savedphotos/Equalized Photo.jpg',resultImg)
cv2.imshow('Eq. Photo',resultImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
 


