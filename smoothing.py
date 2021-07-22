import cv2 as cv
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
# cv.imshow('Screenshot',img) 

#averaging
average = cv.blur(img,(3,3))
# cv.imshow('average_blur',average) 

#gaussian blur

gauss = cv.GaussianBlur(img , (3,3) , 0)
# cv.imshow('gauss blur',gauss)

#median blur

median = cv.medianBlur(img , 3)
# cv.imshow('median',median)

#bilateral blur

bilateral = cv.bilateralFilter(img,10,35,25)
# cv.imshow('bilateral',bilateral)

cv.waitKey(0)