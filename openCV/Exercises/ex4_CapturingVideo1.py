#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


myVideo = cv2.VideoCapture(0)


# In[ ]:


while(True):
    # Capture frame by frame
    ret, frame = myVideo.read()


# In[ ]:


# Our operations on the frame come here
gray_myVideo = cv2.cvtColor(frame, cv2.CLOR_BGR2GRAY)


# In[ ]:


# Display the resulting frame
cv2.imshow('frame', gray_myVideo)


# In[ ]:


if cv2.waitKey(1) & 0xFF == ord('q'):
    break


# In[ ]:


# When everything one, release the capture
myVideo.release()
cv2.destroyAllWindows()


# In[ ]:




