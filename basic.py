import cv2 as cv
img = cv.imread('photos/Screenshot from 2021-04-29 14-44-45.png')
cv.imshow('Screenshot',img) 

#converting to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale',gray) 

#blur image 
blur = cv.GaussianBlur(img,(1,1),cv.BORDER_DEFAULT)  #here (3,3) is kernel size it is always an odd number and if we increase this then the blurness increases
# cv.imshow('BLUR',blur) 

#edge cascade   #if we run edge cascade on a blur image the number of edges will reduce

canny = cv.Canny(img , 125 , 175) #egde cascading is use to find edges 
#  cv.imshow('edge',canny)

#dialating thr image
dialated = cv.dilate(canny , (7,7), iterations =3)
# cv.imshow('dialated',dialated)

#eroding

eroded = cv.erode(dialated,(3,3),iterations = 1)
# cv.imshow('eroded',eroded)

#resize
# resized = cv.resize(img,(1000,1000),interpolation = cv.INTER_CUBIC) 
# cv.imshow('resized',resized)

#cropping

# cropped = img[400:800, 300:800]
# cv.imshow('cropped',cropped)
cv.waitKey(0)