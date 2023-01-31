#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Segmntation
from skimage.segmentation import slic
from skimage.color import label2rgb
import matplotlib.pyplot as plt
img=plt.imread('face.jpg')

#obtain the segmentation with 400 regions
segments=slic(img,n_segments=400, compactness=20)

#put segments on top of original image to compare
segmented_image=label2rgb(segments,img,kind='avg')

#Show the segmented image
plt.imshow(img.astype('uint8'))
plt.show()
plt.imshow(segmented_image.astype('uint8'))
plt.show()


# In[ ]:




