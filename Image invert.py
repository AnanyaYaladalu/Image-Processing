#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
from PIL import ImageFilter
import os

def main():    
    inPath ="C:/Users/User/Desktop/python"
    outPath ="C:/Users/User/Desktop/py"
    for imagePath in os.listdir(inPath):
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outPath, 'invert_'+imagePath)
        img.rotate(90).save(fullOutPath)
        print(fullOutPath)

if __name__ == '__main__':
    main()


# In[ ]:




