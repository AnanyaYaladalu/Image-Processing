#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
from matplotlib import pyplot as plt
img=cv2.imread('b.jpg')
plt.hist(img.ravel(),256,[0,256])
plt.show()


# In[2]:


import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('b.jpg')
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()


# In[ ]:




