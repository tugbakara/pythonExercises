from cv2 import cv2
import numpy as np

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\r.jpg')
myImgG = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
corneredImg = cv2.cornerHarris(np.float32(myImgG),3,5,0.246)
dilatedCornerImg = cv2.dilate(corneredImg,None)
dilatedCornerImg = np.uint8(dilatedCornerImg)
myImg[dilatedCornerImg > 0.001*dilatedCornerImg.max()] = [255,255,255]
ret,labels,stats,centroids = cv2.connectedComponentsWithStats(dilatedCornerImg)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,300,0.1)
'''The corners you find are in Pixel Coordinates. This means a Pixel can be 
at Position (10,10) or (11,11) but not at Position (11.3,11.2) Subpixel 
refinement allows edges at such positions and helps to find a better 
position.'''
myImgCorners = cv2.cornerSubPix(myImgG,np.float32(centroids),(5,5),(-1,-1),criteria)
finalImg = np.hstack((centroids,myImgCorners))
finalImg = np.int64(finalImg) #int0 ile int64 aynı şeydir
myImg[finalImg[:,3],finalImg[:,2]] = [0,0,255]
cv2.imshow('Cornered with SubPixel',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()