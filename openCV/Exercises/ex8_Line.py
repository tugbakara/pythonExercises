import numpy as np
import cv2

#creating black image
blackimg = np.zeros((200,200,3), np.uint8)
#resmin matrix halini gösterir print ile
print(blackimg)
#drawing diagonal blue line with thickness of 1 px, 0'dan 666'ya kadar 
# 200,200,200 BGR ile oluşan enkten line çizdin
blackimg = cv2.line(blackimg, (0,0),(30,30),(200,200,200),1)

if cv2.waitKey(1):        
   cv2.destroyAllWindows()
   
cv2.imshow('Line',blackimg)

#cv2.waitKey(0) sıfır olursa kapatmak tuşuna basınca kapanır, diğer sayılar için bekler mikro saniye kadar
cv2.waitKey(0)
cv2.destroyAllWindows()

