#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image
import PIL
img1=Image.open('a.jpg')
img1=img1.quantize(20)
img1.show()


# In[ ]:




