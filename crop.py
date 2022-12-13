#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image
img=Image.open('a.jpg')
width,height=img.size
left=5
top=height/4
right=164
bottom=3*height/4

img1=img.crop((left,top,right,bottom))
img1.show()


# In[7]:


from PIL import Image
img=Image.open('a.jpg')
img.show()
cropped = img.crop((1,2,300,300))
cropped.show()
cropped.save('cropped.jpg')


# In[ ]:




