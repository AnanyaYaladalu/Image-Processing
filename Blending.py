#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image

img1 = Image.open('a.jpg')
img2 = Image.open('b.jpg')

alphaBlended1=Image.blend(img1,img2,alpha=.4)
alphaBlended1.show()


# In[ ]:




