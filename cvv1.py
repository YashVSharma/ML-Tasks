#!/usr/bin/python
import cv2
import numpy as np
img1=cv2.imread('dog.JPG')
img2=cv2.imread('cat.jpg')
img3=img1+img2
img4=np.concatenate((img1,img2),axis=0)
print(img1)
cv2.imshow('image',img4)
cv2.waitKey(0)
