#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
from skimage.util import random_noise

nature_image=plt.imread('b.jpg')
noisy_image=random_noise(fruit_image)
plt.title('Original image')
plt.imshow(nature_image)
plt.show()

plt.title('Noisy image')
plt.imshow(noisy_image)
plt.show()


# In[6]:


import matplotlib.pyplot as plt

from skimage.restoration import denoise_tv_chambolle
noisy_image=plt.imread('n.png')
denoised_image=denoise_tv_chambolle(noisy_image,multichannel=True)

plt.title('Noisy image')
plt.imshow(noisy_image)
plt.show()

plt.title('Clear image')
plt.imshow(denoised_image)
plt.show()


# In[10]:


import matplotlib.pyplot as plt

from skimage.restoration import denoise_bilateral
landscape_image=plt.imread('bird.jpg')
denoised_image=denoise_bilateral(landscape_image,multichannel=True)

plt.title('Noisy image')
plt.imshow(landscape_image)
plt.show()

plt.title('Denoised image')
plt.imshow(denoised_image)
plt.show()


# In[ ]:




