#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from PIL import Image as im
  
# define a main function
def main():

   
    array = np.arange(0, 737280, 1, np.uint8)

    print(type(array))

    print(array.shape)
      
   
    array = np.reshape(array, (1024, 720))
      
    # show the shape of the array
    print(array.shape)
  
    # show the array
    print(array)
      
    # creating image object of
    # above array
    data = im.fromarray(array)

    data.save('gfg_dummy_pic.png')
  
# driver code
if __name__ == "__main__":

  main()


# In[3]:


from PIL import Image
import numpy as np
# Creating the 144 X 144 NumPy Array with random values
arr = np.random.randint(255, size=(144, 144), dtype=np.uint8)
# Converting the numpy array into image
img  = Image.fromarray(arr)
# Saving the image
img.save("Image_from_array.png")
print(" The Image is saved successfully")
img.show()


# In[5]:


from PIL import Image
import os
os.getcwd()


# In[6]:


os.listdir()


# In[7]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn, "&", fext)


# In[8]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)


# In[11]:


# Creating new Directory using OS library
os.mkdir('NewExtnsn')


# In[12]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("NewExtnsn/{}.pdf".format(fn))


# In[13]:


# Creating new multiple Directories using OS library
os.makedirs('resize//small')
os.makedirs('resize//tiny')
# Note: If you already have a directory with this name, you will get error.
size_small = (600,600) # small images of 600 X 600 pixels
size_tiny = (200,200)  # tiny images of 200 X 200 pixels
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_small)
        i.save("resize/small/{}_small{}".format(fn, fext))
        i.thumbnail(size_tiny)
        i.save("resize/tiny/{}_tiny{}".format(fn, fext))


# In[14]:


# Creating new Directory using OS library
os.mkdir('rotate')
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.rotate(90)
        im.save("rotate/{}_rot.{}".format(fn, fext))


# In[ ]:




