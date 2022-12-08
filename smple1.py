#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
image=cv2.imread('bird.png',0)
cv2.imshow('Display image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


cv2.imwrite('C:/Users/User/Desktop/img1.png',image)


# In[3]:


from PIL import Image
filepath="bird.png"
img=Image.open(filepath)
width=img.width
height=img.height
print("Height of the image : ",height)
print("Width of the image : ",width)


# In[4]:


import numpy
img=cv2.imread("leaf.png")
print("Number of channels :" +str(img.ndim))
cv2.imshow("Channel",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


from PIL import Image
filepath="bird.png"
img=Image.open(filepath)
new=img.resize((150,150))
new


# In[6]:


from PIL import Image
filepath="bird.png"
img=Image.open(filepath)
height=300
width=300
new=img.resize((height,width),Image.ANTIALIAS)
new


# In[2]:


import matplotlib.image as image
img=image.imread('dog.jfif')
print('The shape of the image :',img.shape)
print('The image as array :')
print(img)


# In[3]:


import cv2
img=cv2.imread('cat1.png',2)
ret,bw_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


import cv2
img=cv2.imread('cat1.png',1)
B,G,R=cv2.split(img)
print(B)
print(G)
print(R)


# In[7]:


cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


img=cv2.imread("dog.jfif")
new_image=img.resize((600,200))
ar=1.0*(img.shape[1]/img.shape[0])
print("aspect ratio :")
print(ar)


# In[11]:


import cv2
img=cv2.imread("bird.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hls=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow("gray clr",gray)
cv2.imshow("hsv clr",hsv)
cv2.imshow("hls clr",hls)
cv2.imshow("lab clr",lab)
cv2.imshow("yuv clr",yuv)
cv2.imshow("rgb clr",rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[16]:


import cv2
img1=cv2.imread("1.jpg")
img2=cv2.imread("2.jpg")
add=img1 + img2
sub=img1 - img2
mul=img1 * img2
div=img1 / img2

cv2.imshow("Add",add)
cv2.imshow("Sub",sub)
cv2.imshow("MUl",mul)
cv2.imshow("Div",div)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




