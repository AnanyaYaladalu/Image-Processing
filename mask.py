#!/usr/bin/env python
# coding: utf-8

# In[24]:


from PIL import Image,ImageDraw,ImageFilter
im1=Image.open('10.jpg')
im2=Image.open('a.jpg')
mask_im=Image.new("L",im2.size,0)
draw=ImageDraw.Draw(mask_im)
draw.ellipse((50,150,750,300),fill=250)
mask_im_blur=mask_im.filter(ImageFilter.GaussianBlur(10))
back_im=im1.copy()
back_im.paste(im2,(0,0),mask_im_blur)
back_im.show()


# In[ ]:




