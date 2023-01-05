#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Method 2

import cv2
from PIL import Image
from skimage import io

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 400

def create_collage(images):
    images = [io.imread(img) for img in images]
    images = [cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT)) for image in images]
    if len(images) > 2:
        half = len(images) // 2
        h1 = cv2.hconcat(images[:half])
        h2 = cv2.hconcat(images[half:])
        concat_images = cv2.vconcat([h1, h2])
    else:
        concat_images = cv2.hconcat(images)
    image = Image.fromarray(concat_images)

    image_name = "montage.png"
    image = image.convert("RGB")
    image.save(f"{image_name}")
    return image_name
images=["a.jpg","b.jpg","back.jpg","2.jpg"]
create_collage(images)


# In[2]:


#montage method 1

import skimage.io
import skimage.util

a = skimage.io.imread('b.jpg')
print(a.shape)

b = a // 2
c = a // 3
d=a//4
m = skimage.util.montage([a, b, c,d], multichannel=True)
print(m.shape)

skimage.io.imsave('C:/Users/User/Desktop/Images/done.jpg', m)


# In[3]:


import cv2
import numpy as np

image1=cv2.imread("a.jpg")
image2=cv2.imread("b.jpg")
image3=cv2.imread("1.jpg")
image4=cv2.imread("2.jpg")

image1=cv2.resize(image1,(200,200))
image2=cv2.resize(image2,(200,200))
image3=cv2.resize(image3,(200,200))
image4=cv2.resize(image4,(200,200))

Horizontal1=np.hstack([image1,image2])
Horizontal2=np.hstack([image3,image4])

Vertical_attachment=np.vstack([Horizontal1,Horizontal2])

cv2.imshow("Final Collage",Vertical_attachment)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




