#!/usr/bin/env python
# coding: utf-8

# In[24]:


from PIL import Image, ImageDraw
img = Image.open("b.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 50) 
txt = 'Image Processing'
draw.text((250, 250), txt,font=font,align="left")
img.save('new.jpg')
img.show()


# In[14]:


import numpy as np
import cv2

img = cv2.imread('a.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(400,400),(255,255,255),35)

cv2.rectangle(img,(50,25),(400,150),(0,0,255),20)

cv2.circle(img,(100,63), 55, (0,255,0), -1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:





# In[ ]:




