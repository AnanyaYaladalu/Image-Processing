#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from skimage import io     
frame = cv2.cvtColor(io.imread('crop.png'), cv2.COLOR_RGB2BGR)
image = cv2.cvtColor(io.imread('nature.jpg'), cv2.COLOR_RGB2BGR)

mask = 255 * np.uint8(np.all(frame == [36, 28, 237], axis=2))

contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = min(contours, key=cv2.contourArea)
(x, y, w, h) = cv2.boundingRect(cnt)

frame[y:y+h, x:x+w] = cv2.resize(image, (w, h))

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




