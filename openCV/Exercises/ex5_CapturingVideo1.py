import numpy as np
from cv2 import cv2

cap_vid = cv2.VideoCapture(0)
vid_codec = cv2.VideoWriter_fourcc(*'XVID')
s_video = cv2.VideoWriter('E:\\ImageProcessingdenemeleri\\savedvideos\\savedcamvid.mp4',vid_codec,20.0,(640,480))
s_video1 = cv2.VideoWriter('savedcamvid1.avi',vid_codec,20.0,(640,480))

print(cap_vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap_vid.get(cv2.CAP_PROP_FRAME_WIDTH))

# cv2.CAP_PROP_FRAME_HEIGHT gibi özelliklerin karşılık gelen sayısı vardır (3 gibi) bunları kullanarak da kodu run edebiliriz.
cap_vid.set(3,480)
cap_vid.set(4,480)
print(cap_vid.get(3))
print(cap_vid.get(4))

 
while(True):
    # Capture frame by frame
    ret, frame = cap_vid.read()
    if ret == True:
        
        s_video.write(frame)
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray,1)
        s_video1.write(gray)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  
    else:
        break 


# When everything done, release the capture
cap_vid.release()
cv2.destroyAllWindows()

