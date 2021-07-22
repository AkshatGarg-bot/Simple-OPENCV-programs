import cv2 as cv
import numpy as np
img = cv.imread('photos/cat.jpg')
# cv.imshow('Screenshot',img) 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv.imshow('laplacian',lap)

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.waitKey(0)