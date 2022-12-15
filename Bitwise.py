#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
img1=cv2.imread("1.jpg")
img2=cv2.imread("2.jpg")

and_img=cv2.bitwise_and(img1,img2)
or_img=cv2.bitwise_or(img1,img2)
not_img=cv2.bitwise_not(img1,img2)

cv2.imshow('Bitwise AND', and_img)
cv2.imshow('Bitwise OR', or_img)
cv2.imshow('Bitwise NOT', not_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




