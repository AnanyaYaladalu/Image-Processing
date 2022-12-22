#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np

img = cv2.imread('10.jpg')
near_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST)
cv2.imshow('Near',near_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


import cv2
import numpy as np

img = cv2.imread('10.jpg')
bilinear_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Bilinear',bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


import cv2
import numpy as np

img = cv2.imread('10.jpg')
bicubic_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Bicubic',bicubic_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




