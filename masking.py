import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('Screenshot',img) 
blank = np.zeros(img.shape,dtype = 'uint8')
circle = cv.circle(blank,(img.shape[1]//2+45 + 30, img.shape[0]//2 + 45),200,(255,255,255),-1)

masked = cv.bitwise_and(img,circle)
cv.imshow('mask',masked)
cv.waitKey(0)