from cv2 import cv2
import numpy as np

def CopyPixWithMouse(event,x,y,flags,param):
    
    if event == cv2.EVENT_MOUSEMOVE:
        b = img.item(x,y,0)
        g = img.item(x,y,1) 
        r = img.item(x,y,2)
        cv2.circle(img,(x,y),15,(b,g,r),-1)
        coordinates.append((y,x,3))
        newWin = np.zeros((614,500,3),np.uint8)
        newWin1 = cv2.addWeighted(newWin,1.0,img,0.0,0,dtype = -1)
        newWin = cv2.add(newWin1,img,(b,g,r))           
        cv2.imshow(' C-Image',newWin)

    

img = cv2.imread('E:\\ImageProcessingdenemeleri\\images\\a.jpg',-1)
cv2.imshow('O-Image',img)

print(img.size)
print(img.shape)
coordinates = []
cv2.setMouseCallback('O-Image',CopyPixWithMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
