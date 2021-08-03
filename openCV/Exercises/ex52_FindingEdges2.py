from cv2 import cv2
import imutils

myImg = cv2.imread(r'E:\ImageProcessingdenemeleri\images\r.jpg')
myImgGray = cv2.cvtColor(myImg,cv2.COLOR_BGR2GRAY)
bluredImg = cv2.Canny(myImgGray,100,200)
_,maskedImg = cv2.threshold(bluredImg,150,255,cv2.THRESH_BINARY)
dilatedImg = cv2.dilate(maskedImg,None,iterations = 5)
contours = cv2.findContours(dilatedImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
c = max( contours, key = cv2.contourArea)

left = tuple(c[c[:,:,0].argmin()][0])
right = tuple(c[c[:,:,0].argmax()][0])
top = tuple(c[c[:,:,1].argmin()][0])
buttom = tuple(c[c[:,:,1].argmax()][0])

cv2.circle(myImg,left,3,(60,120,240),-1)
cv2.circle(myImg,right,3,(60,120,240),-1)
cv2.circle(myImg,top,3,(60,120,240),-1)
cv2.circle(myImg,buttom,3,(60,120,240),-1)

cv2.imshow('Edged Image',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
