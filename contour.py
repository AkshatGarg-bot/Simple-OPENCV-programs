import cv2 as cv
import numpy as np
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
# cv.imshow('Screenshot',img) 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY',gray) 
blank = np.zeros(img.shape , dtype = 'uint8')

ret , thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY) #if the pixel intensiy if more than 125 then it is set to 255 else it is set to 0 (converting to binary)
cv.imshow('thresh',thresh)
canny = cv.Canny(img,125,175)
contours,hierarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.imshow('thresh',hierarchy)
cv.drawContours(blank,contours,-1,(0,0,255),4)
cv.imshow('contours drawn',blank)
print(f'{len(contours)}')

cv.waitKey(0)