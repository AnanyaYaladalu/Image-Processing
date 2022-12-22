#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
from matplotlib import pyplot as plt
image = cv2.imread('a.jpg')
cv2.imshow("Size of image before pyrUp: ", image)
image1 = cv2.pyrUp(image)
cv2.imshow('UpSample', image1)
plt.imshow(image1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


import cv2
from matplotlib import pyplot as plt
image = cv2.imread('a.jpg')
cv2.imshow("Size of image before pyrDown: ", image)
image1 = cv2.pyrDown(image)
cv2.imshow('DownSample', image1)
plt.imshow(image1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




