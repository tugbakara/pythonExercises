import datetime as dt
from cv2 import cv2

def MouseClickFunc(event,x,y,flags,param):
    global frame
    if event == cv2.EVENT_MOUSEMOVE:            
        TxtFont = cv2.FONT_HERSHEY_PLAIN
        TxtStr0 = dt.datetime.now()
        TxtStr = str(TxtStr0.strftime(" %Y-%m-%d %H:%M:%S"))
        cv2.putText(frame,TxtStr,(20,20),TxtFont,1,(0,255,255),1,cv2.LINE_AA)
        cv2.rectangle(frame,(20,40),(620,440),(255,255,255),1)    
        cv2.imshow('Frame',frame)           
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.VideoCapture(0)
        cv2.imshow('Frame',frame)

myVid = cv2.VideoCapture(0)
cv2.namedWindow('Frame')

WmyVid = int(myVid.get(3))
HmyVid = int(myVid.get(4))
VidSize = (WmyVid,HmyVid)
VidCodec = cv2.VideoWriter_fourcc(*'XVID')
savedVid = cv2.VideoWriter('E:\\ImageProcessingdenemeleri\\savedvideos\\savedVidWithFunc1.avi',VidCodec ,20.0,VidSize)

while(myVid.isOpened()):
    ret,frame1 = myVid.read()
    if ret == True:
        frame1 = cv2.flip(frame1,1)
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame1, cv2.COLOR_GRAY2BGR)
        cv2.imshow('Frame',frame)
        cv2.setMouseCallback('Frame',MouseClickFunc)
        savedVid.write(frame)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

myVid.release()
savedVid.release()
cv2.destroyAllWindows()



