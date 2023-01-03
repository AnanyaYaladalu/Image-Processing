#!/usr/bin/env python
# coding: utf-8

# In[2]:


# image slicing

from skimage.io import imshow,imread
import matplotlib.pyplot as plt
img1=imread('a.jpg')
imshow(img1)

fig,ax=plt.subplots(1,3,figsize=(6,4), sharey=True)
ax[0].imshow(img1[:, 0:150])
ax[0].set_title('First slice')

ax[1].imshow(img1[:, 150:300])
ax[1].set_title('second slice')

ax[2].imshow(img1[:, 300:500])
ax[2].set_title('Third slice');


# In[ ]:




