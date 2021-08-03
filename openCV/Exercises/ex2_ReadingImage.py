#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
from matplotlib  import pyplot as plt


# In[2]:


my_im4 = cv2.imread('C:\\Users\\lenovo\\Desktop\\Image Processing\\images\\d.jpg',-1)


# In[3]:


plt.imshow(my_im4, cmap = 'gray', interpolation = 'bicubic')


# In[4]:


plt.xticks([]), plt.yticks([]) # to hide the tick values on x and y axis


# In[6]:


plt.show()


# In[ ]:




