import datetime as dt
from cv2 import cv2

myVid = cv2.VideoCapture(0)
WmyVid = int(myVid.get(3))
HmyVid = int(myVid.get(4))
VidSize = (WmyVid,HmyVid)

vidCodec = cv2.VideoWriter_fourcc(*'XVID')

sVid = cv2.VideoWriter('E:\\ImageProcessingdenemeleri\\savedvideos\\savedVidWithTime.mp4',vidCodec,20.0,VidSize)

while(myVid.isOpened()):
    ret,frame = myVid.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        vidFont = cv2.FONT_HERSHEY_PLAIN
        vidTxt = 'Width : '+ str(myVid.get(3)) + ' Height : '+ str(myVid.get(4))
        dateTimeOfvid = dt.datetime.now()

        frame = cv2.putText(frame, vidTxt,(20,40),vidFont,1,
        (255,255,255),1, cv2.LINE_AA)
        frame = cv2.putText(frame, dateTimeOfvid.strftime("%Y-%m-%d %H:%M:%S"),(20,20),vidFont,1,
        (255,255,255),1, cv2.LINE_AA)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Renkli şekili siyah-beyaza koyabilmek için yapıldı
        frameWihColoredRec = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        frameWihColoredRec = cv2.rectangle(frameWihColoredRec, (50,50),(580,430),(0,255,255),1)
        
        cv2.imshow('Video',frameWihColoredRec)
        sVid.write(frameWihColoredRec)
        
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    else:
        break

myVid.release()
sVid.release()
cv2.destroyAllWindows()
        