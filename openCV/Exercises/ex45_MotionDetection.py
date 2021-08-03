from cv2 import cv2
import numpy as np

myVid = cv2.VideoCapture(r'E:\ImageProcessingdenemeleri\videos\7.mp4')
WmyVid = int(myVid.get(3))
HmyVid = int(myVid.get(4))
VidSize = (WmyVid,HmyVid)
VidCodec = cv2.VideoWriter_fourcc(*'MPEG')
savedVid = cv2.VideoWriter(r'E:\ImageProcessingdenemeleri\savedvideos\movementRecognition.mp4',VidCodec,20.0,VidSize) 
ret, frame1 = myVid.read()
ret, frame2 = myVid.read() 

while myVid.isOpened():
    difference = cv2.absdiff(frame1,frame2)
    grayFrame = cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY) 
    bluredFrame = cv2.GaussianBlur(grayFrame,(13,13),0)
    _, maskedFrame = cv2.threshold(bluredFrame,90,255,cv2.THRESH_BINARY)
    dilatedFrame = cv2.dilate(maskedFrame,None,iterations = 100)
    contours , hierarchy = cv2.findContours(dilatedFrame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #print(hierarchy)

    try:
       hierarchy = hierarchy[0]           
    except:
        hierarchy = []

    for contour,hier in zip(contours,hierarchy):
        (x,y,w,h) = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if  area < 12500:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.putText(frame1,"Status : {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),1)
       
    savedVid.write(frame1)
    cv2.imshow('Feed',frame1)
    frame1 = frame2
    ret, frame2 = myVid.read()
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27 :
        break

myVid.release()
#savedVid.release()
cv2.destroyAllWindows()

