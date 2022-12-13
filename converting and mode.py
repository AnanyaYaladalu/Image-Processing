#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pillow')

from PIL import Image
img=Image.open('1.jpg')
img.convert('RGB')
img.save("converted.png")
print("Image converted successfully")


# In[5]:


img=Image.open('2.jpg')
print(img.mode)


# In[ ]:




