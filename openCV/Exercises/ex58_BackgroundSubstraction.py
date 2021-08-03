from cv2 import cv2

myVid = cv2.VideoCapture(r'E:\ImageProcessingdenemeleri\videos\1.mp4')
foreGroundBG = cv2.bgsegm.createBackgroundSubtractorMOG(noiseSigma = 2)
#foreGroundBG = cv2.createBackgroundSubtractorMOG2(varThreshold = 100,detectShadows = False )
#foreGroundBG = cv2.bgsegm.createBackgroundSubtractorCNT()
#kernelFilter = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#foreGroundBG = cv2.bgsegm.createBackgroundSubtractorGMG()
while True:
    ret,frame = myVid.read()
    if frame is None:
        break
    fgMask = foreGroundBG.apply(frame)
    #fgMask = cv2.morphologyEx(fgMask,cv2.MORPH_OPEN,kernelFilter)
    cv2.imshow('BG Substractor',fgMask)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

myVid.release()
cv2.destroyAllWindows()

