#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
from skimage import data
import cv2
coins = cv2.imread("a.jpg")
hist = np.histogram(coins, bins=np.arange(0, 256))
fig, (ax1) = plt.subplots()
plt.axis("off")
ax1.imshow(coins, cmap=plt.cm.gray,interpolation='nearest')


# In[11]:


from skimage.filters import sobel
elevation_map = sobel(coins)
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(elevation_map, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('elevation_map')
#Text(0.5, 1.0, 'elevation_map')


# In[ ]:




