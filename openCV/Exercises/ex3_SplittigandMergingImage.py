#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[3]:


my_im5 = cv2.imread('C:\\Users\\lenovo\\Desktop\\Image Processing\\images\\e.jpg')


# In[4]:


b,g,r = cv2.split(my_im5)


# In[5]:


my_im5_new = cv2.merge([r,g,b])


# In[6]:


plt.subplot(121); plt.imshow(my_im5)


# In[7]:


plt.subplot(122); plt.imshow(my_im5_new)


# In[8]:


plt.show()


# In[12]:


cv2.imshow('bgr image', my_im5)
cv2.imshow('rgb image', my_im5_new)
cv2.waitKey()
cv2.distoryAllWindows()

