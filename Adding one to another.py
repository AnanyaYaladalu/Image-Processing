#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
from PIL import Image
img1 = Image.open("back.jpg")
img2 = Image.open("fore.png")

img1.paste(img2,(0,0),mask=img2)
img1.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




