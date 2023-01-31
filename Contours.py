#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Contouring shapes

def show_image_contour(image,contours):
    plt.figure()
    for n,contour in enumerate(contours):
        plt.plot(contour[:,1],contour[:,0],linewidth=3)
    plt.imshow(image,interpolation='nearest',cmap='gray_r')
    plt.title('contours')
    plt.axis('off')


# In[3]:


from skimage import measure,data
import matplotlib.pyplot as plt

img=data.horse()

#img=plt.imread('star.jpg')

contours=measure.find_contours(img,level=0.8)
show_image_contour(img,contours)


# In[4]:


get_ipython().system('pip install colour')


# In[5]:


def show_image_contour(image,contours):
    plt.figure()
    for n,contour in enumerate(contours):
        plt.plot(contour[:,1],contour[:,0],linewidth=3)
    plt.imshow(image,interpolation='nearest',cmap='gray_r')
    plt.title('contours')
    plt.axis('off')


# In[6]:


from skimage import measure,data
import matplotlib.pyplot as plt


# In[7]:


#Find contours of an image that is not binary

from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage import color

image_dices=plt.imread('dice.png')
plt.axis('off')
plt.imshow(image_dices)
image_dices=color.rgb2gray(image_dices)

thresh=threshold_otsu(image_dices)

binary=image_dices>thresh

contours=measure.find_contours(binary,level=0.8)
show_image_contour(image_dices,contours)


# In[8]:


import numpy as np

shape_contours=[cnt.shape[0] for cnt in contours]

max_dots_shape=50
dots_contours=[cnt for cnt in contours if np.shape(cnt)[0]<max_dots_shape]

show_image_contour(binary,contours)
print('Dice;s dots number:{}.'.format(len(dots_contours)))


# In[ ]:




