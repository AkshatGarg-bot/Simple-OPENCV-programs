import cv2 as cv
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
cv.imshow('Screenshot',img) 

#bgr to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#bgr to hsv

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# bgr to l*a+b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)

#bgr to rgb

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

#hsv to bgr

hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)


# cv.imshow('hsv',hsv_bgr)
cv.waitKey(0)