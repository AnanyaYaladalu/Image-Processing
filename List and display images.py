#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list of png image names only

import os
from os import listdir

folder_dir = "C:/Users/User/Desktop/python"
for images in os.listdir(folder_dir):

    if (images.endswith(".png")):
        print(images)


# In[2]:


#list of all image names

import os
from os import listdir

folder_dir = "C:/Users/User/Desktop/python"
for images in os.listdir(folder_dir):

    if (images.endswith("")):
        print(images)


# In[5]:


import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
get_ipython().run_line_magic('matplotlib', 'inline')

images = []
for img_path in glob.glob('C:/Users/User/Desktop/python/*'):
    images.append(mpimg.imread(img_path))

plt.figure(figsize=(20,10))
columns = 5
for i, image in enumerate(images):
    plt.subplot(len(images) / columns + 1, columns, i + 1)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])


# In[ ]:




