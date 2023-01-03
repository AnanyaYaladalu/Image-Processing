#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
my_image=Image.open('kit.jpg')
sharp=my_image.filter(ImageFilter.SHARPEN)
sharp.save('C:/Users/User/Desktop/Images/sharpen.jpg')
sharp.show()
plt.imshow(sharp)
plt.show()


# In[2]:


import matplotlib.pyplot as plt
img=Image.open('kit.jpg')
plt.imshow(img)
plt.show()
flip=img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('C:/Users/User/Desktop/Images/sharpen.jpg')
plt.imshow(flip)
plt.show()


# In[12]:


from PIL import Image
import matplotlib.pyplot as plt
im=Image.open('kit.jpg')
width,height=im.size
im1=im.crop((550,500,2500,2000))
im1.show()
plt.imshow(im1)
plt.show()


# In[ ]:




