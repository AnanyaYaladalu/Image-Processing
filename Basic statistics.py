#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image,ImageStat
img=Image.open('b.jpg')
stat=ImageStat.Stat(img)
print(stat.mean)


# In[2]:


from PIL import Image,ImageStat
img=Image.open('b.jpg')
stat=ImageStat.Stat(img)
print(stat.median)


# In[3]:


from PIL import Image,ImageStat
img=Image.open('b.jpg')
stat=ImageStat.Stat(img)
print(stat.stddev)


# In[ ]:




