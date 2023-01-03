#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Restore damaged image

import numpy as np
import cv2

img = cv2.imread('cat_damaged.png')

mask = cv2.imread('cat_mask.png', 0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imwrite('cat_inpainted.png', dst)


# In[5]:


#Remove objects

from PIL import Image
import numpy as np	
img = Image.open(r"b.jpg").convert('RGB')
img_arr = np.array(img)
img_arr[100 : 400, 100 : 400] = (0, 0, 0)
img = Image.fromarray(img_arr)
img.show()


# In[5]:


#Remove text

import numpy as np
import cv2 
img = cv2.imread('original_image.jpg')

print(img.shape)
h,w,c =  img.shape

txt = cv2.imread("cropped_image.jpg")
print(txt.shape)
hl,wl,cl  =  txt.shape

x1 = int(w/2-wl/2)
y1 = int(h/2-hl)
x2 = int(w/2+wl/2)
y2 =  int(h/2)
cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)

cv2.imwrite("my.png",img)
cv2.imshow("text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




